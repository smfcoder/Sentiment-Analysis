import string
from collections import Counter
import matplotlib.pyplot as plt

text = open("read2.txt", encoding='utf-8').read()
lowerCase = text.lower()
print(lowerCase)

cleanText = lowerCase.translate(str.maketrans('', '', string.punctuation))
print(cleanText)


token = cleanText.split()
stopWords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]



finalWords = list()
for word in token:
    if word not in stopWords:
        finalWords.append(word)


emotions = list()
with open("emotion.txt", 'r') as file:
    for line in file:
        cleanLine = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = cleanLine.split(':')

        if word in finalWords:
            emotions.append(emotion)

count = Counter(emotions)
print(count)

plt.bar(count.keys(), count.values())
plt.show()

