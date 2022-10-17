import json
import re
from string import punctuation
from scipy.spatial.distance import cosine, euclidean, hamming

with open("files/vacancies2.json", "r", encoding="utf8") as file:
    lines = json.loads(file.read())


def get_words_list(line: str):
    line = line.lower()
    line = re.sub(f"[{punctuation}]", "", line)

    return line.split()


def get_matrix_of_vectors():
    texts = list(map(get_words_list, [i["Description"] for i in lines.values()]))
    unique_words = set(sum(texts, []))
    dict_words = {key: i for i, key in enumerate(unique_words)}
    matrix = []

    for text in texts:
        vec = [0] * len(unique_words)
        for word in text:
            index = dict_words[word]
            vec[index] += 1
        matrix.append(vec)

    return matrix


def compare_text():
    matrix = get_matrix_of_vectors()
    dict_distances = dict()

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i > j:
                dict_distances[(i, j)] = euclidean(matrix[i], matrix[j])

    max_value = max(dict_distances.values())
    for i in dict_distances.keys():
        dict_distances[i] /= max_value

    sorted_distances = sorted(
        [(k, v) for k, v in dict_distances.items()], key=lambda x: x[1]
    )

    return sorted_distances[0][0][0], sorted_distances[0][0][1]


def print_to_most_similar_vacancies():
    id1, id2 = compare_text()

    print(lines[str(id1)], "\n_____________\n", lines[str(id2)])


print_to_most_similar_vacancies()

"""def hamming_distance(vec1, vec2):
    distance = 0
    for i in range(len(vec1)):
        if vec1[i] ^ vec2[i]:
            distance += 1
    return distance"""
