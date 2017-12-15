import gensim
import string
from random import *

print(random())
def getWordsList(words_file):
    open_file = open(words_file, 'w')
    words_list =[]
    words_list2 = []
    contents = open_file.readlines()
    for i in range(len(contents)):
        words_list.append(contents[i].strip('\n'))

    for words in words_list:
        if words != '':
            words_list2.append(words.split(' '));

    open_file.close()

    return words_list2

def writeWords(words_file, words_list):
    open_file = open(words_file, 'w')

    for words in words_list:
        if words != '':
            open_file.write(' '.join(words) + "\n")

    open_file.close()
    return True


words_list = getWordsList("data/farewelltraining.txt")

# Load Google's pre-trained Word2Vec model.
model = gensim.models.KeyedVectors.load_word2vec_format('/home/christian/Documents/MLML/shakespeare-generator/markdown-paper/models/GoogleNews-vectors-negative300.bin.gz', binary=True)

for i in list(range(100)):
    words_list_boot = []
    for words in words_list:
        words_boot = []
        for word in words:
            if word != '' and random() < .3 and word in model.vocab:
                most_similar_word = model.wv.most_similar_cosmul(word)[0][0]
                words_boot.append(most_similar_word)
            else:
                words_boot.append(word)

        print(words_boot)
        if words_boot.__len__() != 0:
            words_list_boot.append(words_boot)

    writeWords(string.Format("data/farewellbootstrapped{}.txt",i), words_list_boot)

#print(most_similar_word)