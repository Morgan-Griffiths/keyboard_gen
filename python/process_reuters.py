import os
from bs4 import BeautifulSoup
import nltk
import string
from nltk.stem.porter import *
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
import regex


###############################################################################
###################### class definition for word list #########################
###############################################################################

class WordList:
    def __init__(self):
        """ function: constructor
            ---------------------
            instantiate word list object
        """
        self.title = []
        self.body = []

###############################################################################
##################### class definition for document object ####################
###############################################################################

class Document:
    def __init__(self,article):
        """ function: constructor
            ---------------------
            instantiate document object;
            :param article: bs4 child node of parse tree representing article;
        """
        # instantiate document fields
        self.topics = []
        self.places = []
        self.words = WordList()
        # populate document fields
        self.__populate_class_labels(article)

    ###########################################################################
    ############ class label words not permitted in feature vector ############
    ###########################################################################

    banned_words = set()

    ###########################################################################
    ######### method to pre-populate class labels for document object #########
    ###########################################################################

    def __populate_class_labels(self,article):
        """ function: populate_class_labels
            -------------------------------
            fill self.topics and self.places; update @banned_words concurrently;
            :param article: bs4 child node of parse tree representing article;
        """
        for topic in article.topics.children:
            topic_label = topic.text.encode('ascii','ignore')
            self.topics.append(topic_label)
            Document.banned_words.add(topic_label)
        for place in article.places.children:
            place_label = place.text.encode('ascii','ignore')
            self.places.append(place_label)
            Document.banned_words.add(place_label)

    ###########################################################################
    ######## method(s) for post-populating word lists w/o class labels ########
    ###########################################################################

    def populate_word_list(self,article):
        """ function: populate_word_list
            ----------------------------
            generate token list from title/body text blocks of @article
            non-private method - must execute after @banned_words is filled
            :param article: bs4 child node of parse tree representing article
        """
        text = article.find('text')
        title = text.title
        body = text.body
        if body != None:
            self.words.body = body.text
            self.words.title = title.text

        # if title != None:
        #     self.words.title = self.__tokenize(title.text)
        # if body != None:
        #     self.words.body = self.__tokenize(body.text)

    def __tokenize(self,text):
        """ function: tokenize
            ------------------
            generate list of tokens given a block of @text
            :param text: string representing article text field
            :returns: list of tokens with various modifications
        """
        ascii = text.encode('ascii', 'ignore')
        # remove digits & punctuation
        no_digits = ascii.translate(None, string.digits)
        no_punctuation = no_digits.translate(None, string.punctuation)
        # separate text blocks into tokens
        tokens = nltk.word_tokenize(no_punctuation)
        # remove class labels, stopwords, and non-english words
        no_class_labels = [w for w in tokens if not w in Document.banned_words]
        no_stop_words = [w for w in no_class_labels if not w in stopwords.words('english')]
        eng = [y for y in no_stop_words if wordnet.synsets(y)]
        # lemmatization
        lemmas = []
        lmtzr = WordNetLemmatizer()
        for token in eng:
           lemmas.append(lmtzr.lemmatize(token))
        # stemming
        stems = []
        stemmer = PorterStemmer()
        for token in lemmas:
            stem = stemmer.stem(token).encode('ascii', 'ignore')
            if len(stem) >= 4:
                stems.append(stem)
        return stems

###############################################################################
##################### class definition for lexicon object #####################
###############################################################################

class Lexicon:
    def __init__(self,documents):
        """ function: constructor
            ---------------------
            instantiate lexicon object
            :param documents: list of document objects used to build lexicon
        """
        self.title = set()
        self.body = set()
        self.__build_lexicon(documents)

    ###########################################################################
    ############# method to populate title/body sets for lexicon ##############
    ###########################################################################

    def __build_lexicon(self,documents):
        """ function: build_lexicon
            -----------------------
            populate word sets for title/body given list of @documents
            :param documents: list of document objects used to build lexicon
        """
        for document in documents:
            for term in document.words.title:
                self.title.add(term)
            for term in document.words.body:
                self.body.add(term)


###############################################################################
############ function(s) for generating parse tree from .sgm files ############
###############################################################################

def __generate_tree(text):
    """ function: generate_tree
        -----------------------
        extract well-formatted tree from poorly-formatted sgml @text
        :param text: string representing sgml text for a set of articles
        :returns: parsetree @tree of the structured @text
    """
    return BeautifulSoup(text, "html.parser")

###############################################################################
########## function(s) for generating parse trees & document objects ##########
###############################################################################

def __parse_documents(datapath):
    """ function: parse_document
        ------------------------
        extract list of Document objects from token list
        :returns: list of document entities generated by generate_document()
    """
    documents = []
    pairs = dict([])
    # generate well-formatted document set for each file
    for file in os.listdir(datapath):
        if not file.endswith(".sgm"):
            continue
        try:
            # open 'reut2-XXX.sgm' file from /data directory
            path = os.path.join(datapath, file)
            data = open(path, 'r')
            text = data.read()
            data.close()
            tree = __generate_tree(text.lower())
            # separate segments & generate documents
            for reuter in tree.find_all("reuters"):
                document = Document(reuter)
                pairs[document] = reuter
            # generate tokenized word list for each document
            for document, reuter in pairs.items():
                document.populate_word_list(reuter)
                documents.append(document)
            print("Finished extracting information from file:", file)
        except Exception as e:
            print("Error in file:", file)
            print(e)
        break
    return documents

###############################################################################
################## main function - single point of execution ##################
###############################################################################

def begin(datapath='data'):
    """ function: begin
        ---------------
        sanitize input files into well-formatted, processable objects
        generate dataset (feature vectors, class labels) for .sgm file set:
    """
    # generate list of document objects for feature selection
    print('\nGenerating document objects. This may take some time...')
    documents = __parse_documents(datapath)
    # generate lexicon of unique words for feature reduction
    print('Document generation complete. Building lexicon...')
    # lexicon = Lexicon(documents)
    # return lexicon
    with open('reuters.txt', 'w') as f:
        for document in documents:
            body = document.words.body
            if body:
                body = regex.sub(r'[^0-9a-z\.,/\[\]\\;\'\s]', '', body)
                print('body:', body)
                f.write(str(body) + '\n')
if __name__ == '__main__':
    begin('/Users/Shuza/Downloads/reuters21578')