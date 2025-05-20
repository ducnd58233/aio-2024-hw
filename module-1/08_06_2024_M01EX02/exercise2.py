from collections import defaultdict


def count_char(s):
    mapping_freq = defaultdict(int)

    for c in s:
        mapping_freq[c] += 1

    return mapping_freq


if __name__ == "__main__":
    string = "Happiness"
    print(count_char(string))

    string = "smiles"
    print(count_char(string))
