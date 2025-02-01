import sys
import uuid
from pathlib import Path

import cv2
from loguru import logger
from ultralytics import YOLOWorld
from ultralytics.engine.results import Boxes

logger.remove()
logger.add(sys.stderr, level="INFO")
logger.add("run/log.log", level="INFO", rotation="100kb")

# Create run directory if it doesn't exist
Path("./run").mkdir(parents=True, exist_ok=True)


def save_detection_results(results: Boxes) -> list[str]:
    """
    Save detection results as images if detections were found.

    :param results: Detection results from YOLO model prediction, containing bounding boxes and other metadata
    :return: List of paths where annotated images were saved as strings
    """
    # Initialize empty list to store paths of saved images
    saved_paths = []

    # Iterate through each detection result
    for i, result in enumerate(results):
        # Check if any detections were made by looking at number of bounding boxes
        if len(result.boxes) > 0:
            # Plot the detection results with bounding boxes and labels on the image
            annotated_image = result.plot()

            # Generate unique filename using UUID to avoid overwrites
            output_path = f"./run/img_{uuid.uuid4()}.jpg"

            # Save the annotated image to disk using OpenCV
            cv2.imwrite(output_path, annotated_image)

            # Get absolute path and convert to string for consistency
            saved_path = Path(output_path).resolve()
            print(f"Image saved to {saved_path}")
            saved_paths.append(str(saved_path))

    return saved_paths

# Initialize a YOLO-World model
model = YOLOWorld("yolov8x-world.pt")

# Define custom classes
model.set_classes(
    ["phone", "mask", "glasses"]
)  # <--------- Change this to the class you want to detect

# Execute prediction on an image
results: Boxes = model.predict(
    "samples/vietnam-3.jpg", max_det=100, iou=0.01, conf=0.01
)

# Save detection results as images
save_detection_results(results)