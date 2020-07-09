# Basado en: https://github.com/udacity/CVND---Image-Captioning-Project (Recuperado en enero, 2020)
import nltk
import pickle
import os.path
#from pycocotools.coco import COCO
from collections import Counter

class Vocabulary(object):

    def __init__(self,
        vocab_threshold,
        vocab_file,
        start_word="<start>",
        end_word="<end>",
        unk_word="<unk>",
        annotations_file='',
        vocab_from_file=False):
        """Initialize the vocabulary.
        Args:
          vocab_threshold: Minimum word count threshold.
          vocab_file: File containing the vocabulary.
          start_word: Special word denoting sentence start.
          end_word: Special word denoting sentence end.
          unk_word: Special word denoting unknown words.
          annotations_file: Path for train annotation file.
          vocab_from_file: If False, create vocab from scratch & override any existing vocab_file
                           If True, load vocab from from existing vocab_file, if it exists
        """
        self.vocab_threshold = vocab_threshold
        self.vocab_file = vocab_file
        self.start_word = start_word
        self.end_word = end_word
        self.unk_word = unk_word
        self.annotations_file = annotations_file
        self.vocab_from_file = vocab_from_file
        self.get_vocab()

    def get_vocab(self):
        """Load the vocabulary from file OR build the vocabulary from scratch."""
        print('the path: ',self.vocab_file)
        if os.path.exists(self.vocab_file) & self.vocab_from_file:
            with open(self.vocab_file, 'rb') as f:
                vocab = pickle.load(f)
                self.word2idx = vocab.word2idx
                self.idx2word = vocab.idx2word
            print('Vocabulary successfully loaded from vocab.pkl file!')
        #else:
         #   self.build_vocab()
          #  with open(self.vocab_file, 'wb') as f:
           #     pickle.dump(self, f)
        
    #def build_vocab(self):
    #    """Populate the dictionaries for converting tokens to integers (and vice-versa)."""
     #   self.init_vocab()
      #  self.add_word(self.start_word)
       # self.add_word(self.end_word)
        #self.add_word(self.unk_word)
        #self.add_captions()

    #def init_vocab(self):
     #   """Initialize the dictionaries for converting tokens to integers (and vice-versa)."""
      #  self.word2idx = {}
       # self.idx2word = {}
        #self.idx = 0

    #def add_word(self, word):
        """Add a token to the vocabulary."""
     #   if not word in self.word2idx:
      #      self.word2idx[word] = self.idx
       #     self.idx2word[self.idx] = word
        #    self.idx += 1


            #entender que hace este metodo
    #def add_captions(self):
        """Loop over training captions and add all tokens to the vocabulary that meet or exceed the threshold."""
     #   coco = COCO(self.annotations_file)#annotations files se mandan a coco coco devuelve todos los annotations
      #  counter = Counter()#se crea counter
       # ids = coco.anns.keys()#los ids de los captions
        #for i, id in enumerate(ids):#se itera por cada caption
         #   caption = str(coco.anns[id]['caption'])
          #  tokens = nltk.tokenize.word_tokenize(caption.lower())#se tokenizan las palabras del caption
           # counter.update(tokens)#se mandan los tokens para que se cuenten cuanto salen en el total

            #if i % 100000 == 0:
             #   print("[%d/%d] Tokenizing captions..." % (i, len(ids)))

        #words = [word for word, cnt in counter.items() if cnt >= self.vocab_threshold]
        #se guarda en words la palabras que cumplan con el vocabthreshold

        #se agregan las palabras a word2ind y idx2dword
        #for i, word in enumerate(words):
         #   self.add_word(word)

    #def __call__(self, word):
     #   if not word in self.word2idx:
      #      return self.word2idx[self.unk_word]
       # return self.word2idx[word]

    #def __len__(self):
     #   return len(self.word2idx)
