from src.featurizers import skipthoughts
from src.utils.normalize import normalize_and_remove_stop_words

def gen_vocab(features, corpus_dict):
    # This conditional needs to be made compatible with the cosine and bog options
    result = [None, None]
    if features.skipthoughts:
        result[1] = skipthoughts.load_model()
    if features.cos_similarity or features.bag_of_words:
        # needs preferred vocabulary size passed in (ex: vocabsize=500)
        # needs 'src.utils.normalize.normalize_and_remove_stop_words'
        # vocabdict contains the most frequently occurring words in the corpus from #1 to n, with n going as far as vocabsize if possible
        # we should be able to use vocabulary=vocabdict when setting up the CountVectorizer for clusters and new docs
        print("making vocabulary...")
        vocabsize = 500
        index = 0
        vocabdict = dict()
        for word in corpus_dict:
            if len(vocabdict) < vocabsize:
                cleantext = normalize_and_remove_stop_words(word)
                if cleantext != '':
                    if not cleantext in vocabdict:
                        vocabdict[cleantext] = index
                        index+=1
            else: break
        result[0] = vocabdict

    return result

def main(argv):
    features, corpus_dict = argv
    vocab, encoder_decoder = gen_vocab(features, corpus_dict)
    return vocab, encoder_decoder
