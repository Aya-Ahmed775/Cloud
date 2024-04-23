import re
from collections import Counter
import nltk
from nltk.corpus import stopwords


nltk.download('stopwords')

def read_file(random_paragraphs):
    with open(random_paragraphs, 'r') as file:
        return file.read()


def remove_stopwords(text, stopwords_set):
    words = re.findall(r'\b\w+\b', text.lower())
    return ' '.join(word for word in words if word not in stopwords_set)

def count_frequencies(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)


def main():
    
    filename = "random_paragraphs.txt"  
    par = read_file("random_paragraphs.txt")

    nitk_stopwords = set(stopwords.words('english'))

    filtered= remove_stopwords(par, nitk_stopwords)

    frequencies = count_frequencies(filtered)

    for word, count in frequencies.items():
        print(f'{word}: {count}')

if __name__ == "__main__":
    main()