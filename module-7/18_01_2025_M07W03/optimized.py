import os
import argparse
import cv2
import numpy as np
from collections import defaultdict, deque
from tqdm import tqdm
from ultralytics import YOLO, solutions
from loguru import logger

def load_config():
    """Load and return configuration settings"""
    return {
        'model_path': 'yolo11x.pt',
        'track_history_length': 120,
        'batch_size': 64,
        'line_thickness': 4,
        'track_color': (230, 230, 230),
        # For rectangle region counting: top left, top right, bottom right, bottom left
        'region_points': [(20, 400), (1080, 400), (1080, 850), (20, 850)],
    }

def init_video(video_path):
    """Initialize video capture and writer objects"""
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    video_name = video_path.split('/')[-1]
    output_path = f"./run/{video_name.split('.')[0]}_tracked.mp4"
    
    os.makedirs("./run", exist_ok=True)
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    if not out.isOpened():
        raise ValueError('Failed to create output video writer')
    
    return cap, out, output_path, fps

def update_track_history(
    track_history,
    last_seen,
    track_ids,
    frame_count,
    batch_size,
    frame_idx,
    history_length,
):
    """Update tracking history and remove old tracks"""
    current_tracks = set(track_ids)
    for track_id in list(track_history.keys()):
        if track_id in current_tracks:
            last_seen[track_id] = frame_count - (batch_size - frame_idx - 1)
        elif frame_count - last_seen[track_id] > history_length:
            del track_history[track_id]
            del last_seen[track_id]
            
def draw_tracks(
    frame,
    boxes,
    track_ids,
    track_history,
    config
):
    """Draw traking lines on frame"""
    if not track_ids:
        return frame
    
    for box, track_id in zip(boxes, track_ids):
        x, y, w, h = box
        track = track_history[track_id]
        track.append((float(x), float(y)))
        if len(track) > config['track_history_length']:
            track.popleft()
            
        points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
        cv2.polylines(
            frame,
            [points],
            isClosed=False,
            color=config['track_color'],
            thickness=config['line_thickness']
        )
    return frame

def process_batch(model, batch_frames, track_history, last_seen, frame_count, config):
    """Process a batch of frames through YOLO model"""
    results = model.track(
        batch_frames,
        persist=True,
        tracker='botsort.yaml',
        show=False,
        verbose=False,
        iou=0.5,
    )
    
    processed_frames = []
    for frame_idx, result in enumerate(results):
        boxes = result.boxes.xywh.cpu()
        track_ids = (
            result.boxes.id.int().cpu().tolist()
            if result.boxes.id is not None else []
        )
        
        update_track_history(
            track_history,
            last_seen,
            track_ids,
            frame_count,
            len(batch_frames),
            frame_idx,
            config['track_history_length']
        )
        
        annotated_frame = result.plot(font_size=4, line_width=2)
        annotated_frame = draw_tracks(
            annotated_frame,
            boxes,
            track_ids,
            track_history,
            config
        )
        processed_frames.append(annotated_frame)
    return processed_frames

def main(video_path):
    """Main function to process video"""
    CONFIG = load_config()
    model = YOLO(CONFIG.get('model_path', 'yolo11x.pt'))
    
    cap, out, output_path, fps = init_video(video_path)
    track_history = defaultdict(lambda: deque())
    last_seen = defaultdict(int)
    # Calculate frames for 3 seconds
    frames_to_process = int(fps * 3)
    counter = solutions.ObjectCounter(
        show=False, # Display the output
        region=CONFIG.get('region_points', []), # Pass region points
        model=CONFIG.get('model_path', 'yolo11x.pt')
    )
    
    with tqdm(
        total=frames_to_process,
        desc='Processing frames',
        unit='frame',
        colour='green'
    ) as pbar:
        frame_count = 0
        batch_frames = []
        
        while cap.isOpened() and frame_count < frames_to_process:
            success, frame = cap.read()
            if not success:
                break
            
            frame_count += 1
            batch_frames.append(frame)
            out.write(counter.count(frame))
            
            if len(batch_frames) == CONFIG['batch_size'] or frame_count == frames_to_process:
                try:
                    processed_frames = process_batch(
                        model,
                        batch_frames,
                        track_history,
                        last_seen,
                        frame_count,
                        CONFIG,
                    )
                    for frame in processed_frames:
                        out.write(frame)
                        pbar.update(1)
                    batch_frames = []
                except Exception as e:
                    logger.error(
                        f'Error when handling frames {frame_count - len(batch_frames) + 1} to {frame_count}: {str(e)}'
                    )
                    batch_frames = []
                    continue
                
    try:
        cap.release()
        out.release()
        cv2.destroyAllWindows()
    except Exception as e:
        logger.error(f'{str(e)}')
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video-path', type=str, default='./samples/vietnam.mp4')
    args = parser.parse_args()
    
    video_path = os.path.abspath(args.video_path)
    if not os.path.exists(video_path):
        logger.error(f"Video file not found: {video_path}")
        exit(1)
        
    main(args.video_path)