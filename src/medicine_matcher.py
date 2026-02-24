from rapidfuzz import process
import re

def load_medicine_list(filepath="data/medicine_list.txt"):
    with open(filepath, "r") as f:
        medicines = [line.strip() for line in f.readlines()]
    return medicines


def correct_medicine_names(text):
    medicines = load_medicine_list()
    words = re.findall(r'\b[A-Za-z]{4,}\b', text)

    corrected = []

    for word in words:
        match, score, _ = process.extractOne(word, medicines)
        if score > 80 :  # similarity threshold
            corrected.append(match)

    return list(set(corrected))