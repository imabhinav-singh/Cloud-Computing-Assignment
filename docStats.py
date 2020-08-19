# implement this
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

    stopWords = ['a', 'an', 'the', 'how', 'who', 'what', 'of', 'for', 'is', 'was', 'are', 'do', 'if', 'could',
                 'would', 'should', 'then', 'than', 'be', 'as', 'or', 'and', 'it', 'will', 'shall', 'we', 'us',
                 'he', 'him', 'his', 'her', 'she', 'they', 'them', 'because', 'as']
    print("Top 10 keywords:- " + str(topTenKeyWords(contents, stopWords)))
    filename.close()

if __name__ == '__main__':
    main()
