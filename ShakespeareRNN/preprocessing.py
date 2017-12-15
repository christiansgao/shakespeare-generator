import itertools
import nltk
import numpy as np
import re


class Preprocessing:

    def __init__(self):
        self.unknown_token = "UNKNOWN_TOKEN"
        self.sentence_start_token = "SENTENCE_START"
        self.sentence_end_token = "SENTENCE_END"


    def create_tokens(self, vocab_size, filepath):

        print "Reading file..."
        nltk.download('punkt')

        with open(filepath, 'r') as f:
            # chain is used to flatten small arrays into one big aray
            raw_sentences = [x.decode("utf-8-sig").encode("utf-8").rstrip().lower() for x in f.readlines()]

            sentences = itertools.chain(*[nltk.sent_tokenize(x) for x in raw_sentences])

            # Append SENTENCE_START and SENTENCE_END
            sentences = ["%s %s %s" % (self.sentence_start_token, x, self.sentence_end_token) for x in sentences]

            sentences = [str(x) for x in sentences]

            print("Tokenize the sentences into words...")
            tokenized_sentences = [nltk.word_tokenize(sent) for sent in sentences]

            print("Counting the word frequencies...")
            word_freq = nltk.FreqDist(itertools.chain(*tokenized_sentences))
            print "Found %d unique words tokens." % len(word_freq.items())

            # Get the most common words and build index_to_word and word_to_index vectors
            vocab = word_freq.most_common(vocab_size - 1)
            self.index_to_word = [x[0] for x in vocab]
            self.index_to_word.append(self.unknown_token)
            self.word_to_index = dict([(w, i) for i, w in enumerate(self.index_to_word)])

            print "Using vocabulary size %d." % vocab_size
            print "The least frequent word in our vocabulary is '%s' and appeared %d times." % (
            vocab[-1][0], vocab[-1][1])

            # Replace all words not in our vocabulary with the unknown token
            for i, sent in enumerate(tokenized_sentences):
                tokenized_sentences[i] = [w if w in self.word_to_index else self.unknown_token for w in sent]

            x_train = np.asarray([[self.word_to_index[w] for w in sent[:-1]] for sent in tokenized_sentences])
            y_train = np.asarray([[self.word_to_index[w] for w in sent[1:]] for sent in tokenized_sentences])

            print "\nExample sentence: '%s \n %s'" % (sentences[0], str(x_train[0]))

            return x_train, y_train
