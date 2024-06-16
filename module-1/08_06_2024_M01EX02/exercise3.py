from collections import defaultdict

def word_count(file_path):
    file = open(file_path, 'r')
    mapping_word_freq = defaultdict(int)
    
    for line in file.readlines():
        for word in line.split():
            mapping_word_freq[word.lower()] += 1
            
    file.close()
    return mapping_word_freq


if __name__ == '__main__':
    file_path = './P1_data.txt'
    res = word_count(file_path)
    print(res['man'])
