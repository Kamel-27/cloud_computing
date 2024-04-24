import nltk
from nltk.corpus import stopwords
from collections import Counter
nltk.download("punkt")
nltk.download('stopwords')
with open(r"random_paragraphs.txt") as file:
    text = file.read()

words = nltk.word_tokenize(text)
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]
word_freq = Counter(filtered_words)
for word, freq in word_freq.items():
    print(f'{word}: {freq}')
