import streamlit as st
from lenvenshtein_distance import cal_levenshtein_distance


def load_vocab(file_path):
    with open(file_path, 'rt') as f:
        lines = f.readlines()

    words = sorted(set([line.strip() for line in lines]))
    return words


vocabs = load_vocab(file_path="./vocab.txt")


def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input("Word: ")

    if st.button("Compute"):
        leven_distances = dict()
        for vocab in vocabs:
            leven_distances[vocab] = cal_levenshtein_distance(word, vocab)

        sorted_distances = dict(
            sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distances.keys())[0]
        st.write("Correct word: ", correct_word)

        col1, col2 = st.columns(2)
        col1.write("Vocabulary: ")
        col1.write(vocabs)

        col2.write("Distances: ")
        col2.write(sorted_distances)


if __name__ == "__main__":
    main()
