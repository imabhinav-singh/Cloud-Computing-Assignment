import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

def readFile(filename):
    return filename.read()

def topTenWords(wordCountDict):
    return wordCountDict.split()[0:10]

def topTenKeyWords(contents, stopWords):
    count = 0
    keywords = []
    for word in contents.split():
        if word not in stopWords:
            keywords.append(word)
            count += 1
        if count == 10:
            break
    return keywords

def wordCount(contents):
    return len(contents.split())

def main():
    filename = open("C:\\Users\\Tanishq\\Documents\\sample.txt", "r")
    contents = readFile(filename)
    print("Number of words:- "+str(wordCount(contents)))
    print("Top 10 words:- "+str(topTenWords(contents)))

    stopWords = set(stopwords.words('english'))
    print("Top 10 keywords:- ")
    count = 0
    for w in contents.split():
        if w not in stopWords:
            print(w)
            count += 1
        if count == 10:
            break
    filename.close()

if __name__ == '__main__':
    main()
