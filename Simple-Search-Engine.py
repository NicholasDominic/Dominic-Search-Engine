from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer
from nltk.chunk import ne_chunk

sentences = [
'Natural language processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics concerned with the interactions between computers and human (natural) languages',
'Modern NLP algorithms are based on machine learning, especially statistical machine learning', 
'NLP research is gradually shifting from lexical semantics to compositional semantics and, further on, narrative understanding',
'The learning procedures used during machine learning automatically focus on the most common cases, whereas when writing rules by hand it is often not obvious at all where the effort should be directed',
'Produce a readable summary of a chunk of text. Often used to provide summaries of text of a known type, such as articles in the financial section of a newspaper'
]

stopword_set = set(stopwords.words('english'))

def preprocessing(sentence):
    tokenized = set(word_tokenize(sentence))
    tokenized = tokenized - stopword_set
    stemmed = [(PorterStemmer().stem(i)) for i in tokenized]
    lemmatized = [(WordNetLemmatizer().lemmatize(i)) for i in stemmed]
    return set(lemmatized)

def menu_1():
    global user_sentences

    while True:
        inp = input('Input Sentence : ')
        if len(inp) > 10:
            break
    
    user_sentences = inp
    inp = preprocessing(inp)

    no = 1
    for sentence in sentences:
        before = preprocessing(sentence)
        after = before - inp
        if len(before) != len(after):
            print(no, '.', sentence)
            no = no + 1

def menu_2():
    tokenized = word_tokenize(user_sentences)
    pt = pos_tag(tokenized)
    fd = FreqDist(tokenized).most_common()

    print('Part of Speech')
    for word, tag in pt:
        print(word, '-', tag)

    print('Frequency')
    for word, count in fd:
        print(word, '-', count)

    while True:
        show = input('Want draw show tree Y/N : ')
        if show == 'Y' or show == 'N':
            break
   
    if show == 'Y':
        ne_chunk(pt).draw()

while True:
    for i in range(0,25):
        print('')

    print('DOMINIC Search Engine')
    print('-----------------------')
    print('1. Search')
    print('2. Frequency')
    print('3. Exit')
    try:
        inp = input('Choose Menu : ')
        inp = int(inp)
    
    except:
        print('Input Must be Numeric')
        inp = -1

    if inp == 1:
        menu_1()

    elif inp == 2:
        menu_2()

    elif inp == 3:
        break

    input()