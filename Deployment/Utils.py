import re
import emoji
import string
from nltk.corpus import stopwords


def preprocess(text):
    # First we define a list of arabic and english punctiations that we want to get rid of in our text
    punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ''' + string.punctuation

    # Arabic stop words with nltk
    stop_words = stopwords.words('arabic')

    arabic_diacritics = re.compile("""
                             ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)   
    # Remove usernames
    text = re.sub(r'@[^\s]+','',text)
    
    # Remove URL
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', ' ', text)
    
    # Remove None arabic 
    text = re.sub(u"[^\u0621-\u063A\u0640-\u0652 ]", " ", text)
    
    # Remove punctuations
    translator = str.maketrans('', '', punctuations)
    text = text.translate(translator)
    
    # Remove repeating character
    text = re.sub(r'(.)\1+', r'\1', text)

    # Remove tashkeel
    text = re.sub(arabic_diacritics, '', text)
    
    #Remove elongation
    text = re.sub("[إأآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "ء", text)
    text = re.sub("ئ", "ء", text)
    text = re.sub("ة", "ه", text)
    text = re.sub("گ", "ك", text)
    
    # Remove emojis
    text=  emoji.demojize(text)
    text= re.sub(r'(:[!_\-\w]+:)', ' ', text)
    
    # Remove numbers
    text = ''.join(i for i in text if not i.isdigit())
    
    # Remove stop words
    text = ' '.join(word for word in text.split() if word not in stop_words)

    return text
