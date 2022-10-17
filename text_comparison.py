import json
import re
from string import punctuation
with open("files/vacancies2.json", "r", encoding="utf8") as file:
    lines = json.loads(file.read())


def get_words_list(line: str):
    line = line.lower()
    line = re.sub(f"[{punctuation}]", "", line)

    return line.split()


def get_matrix_of_vectors():
    texts = list(map(get_words_list, [i["Description"] for i in lines.values()]))
    unique_words = set(sum(texts, []))
    dict_words = {key : i for i, key in enumerate(unique_words)}
    matrix = []

    for text in texts:
        vec = [0]*len(unique_words)
        for word in text:
            index = dict_words[word]
            vec[index] += 1
        matrix.append(vec)

    return matrix


def hamming_distance(vec1, vec2):
    distance = 0
    for i in range(len(vec1)):
        if vec1[i] ^ vec2[i]:
            distance += 1
    return distance


def compare_text():
    matrix = get_matrix_of_vectors()
    dict_distances = dict()

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i > j:
                dict_distances[(i, j)] = hamming_distance(matrix[i], matrix[j])

    max_value = max(dict_distances.values())
    for i in dict_distances.keys():
        dict_distances[i] /= max_value

    print(sorted([(k, v) for k, v in dict_distances.items()], key=lambda x: x[1]))


compare_text()

