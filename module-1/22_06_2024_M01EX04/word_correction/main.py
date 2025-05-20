import streamlit as st


def load_vocab(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words


def levenshtein_distance(token1, token2):
    len_token1 = len(token1)
    len_token2 = len(token2)
    distances = [[0] * (len_token2 + 1) for _ in range(len_token1 + 1)]

    for i in range(len_token1 + 1):
        distances[i][0] = i

    for j in range(len_token2 + 1):
        distances[0][j] = j

    for t1 in range(1, len_token1 + 1):
        for t2 in range(1, len_token2 + 1):
            if token1[t1 - 1] == token2[t2 - 1]:
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                distances[t1][t2] = (
                    min(
                        distances[t1][t2 - 1],  # insert
                        distances[t1 - 1][t2],  # delete
                        distances[t1 - 1][t2 - 1],  # replace
                    )
                    + 1
                )
    return distances[len_token1][len_token2]


def word_correction(word, vocab):
    candidates = [w for w in vocab if levenshtein_distance(word, w) <= 2]
    return candidates


def main():
    st.title("Word Correction using Levenshstein Distance")
    word = st.text_input("Enter a word: ")
    vocabs = load_vocab("data/vocab.txt")

    if st.button("Compute"):
        leven_distances = dict()
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(word, vocab)

        sorted_distances = dict(
            sorted(leven_distances.items(), key=lambda item: item[1])
        )
        corrected_word = list(sorted_distances.keys())[0]
        st.write("Correct word: ", corrected_word)

        col1, col2 = st.columns(2)
        col1.write("Vocabulary:")
        col1.write(vocabs)
        col2.write("Levenshtein Distance:")
        col2.write(sorted_distances)


if __name__ == "__main__":
    main()
