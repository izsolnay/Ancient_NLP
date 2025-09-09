import re
import string
import nltk
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')  
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


"""
Simple cleaning function that
    1. Replaces multiple whitespace characters with a single space
    2. Removes leading and trailing whitespace
"""

def simple_cleaning(text):

    text = re.sub(r'\s+', ' ', text) 
    text = text.strip() 
    
    return text


"""
This script creates an extended set of stop words by combining
the default English stop words from NLTK with a custom set of 
stop words specific to transliterated Sumerian texts. 
It also removes specific words from the final set of stopwords.
"""

def ancient_stopwords():
    # Define and remove stopwords
    stop_words = set(stopwords.words('english'))
    
    # Create a set of custom stop words
    custom_stopwords = {
        '-……', '…….', '………', '……',
        '--', '``', "'", '...', '..',
        ' l.', '...b', '...y', '...ni',
        '...c', '...d', '-', 'aa',
        'yy', 'a', 'b', 'c', 'd',
        'p.', 'u', 'n', 'th',
        'a-p.', 'rd', 'nd', 'a-p',
        'q-v'
    }
    
    # Union 'custom_stopwords' with stopwords
    ancient_stopwords = stop_words.union(custom_stopwords)
     
    # Create list of words to discard from stopwords (= to keep)
    words_to_discard = ['i', 'you', 'not', 'she', 'he', 'they', 'we', 'us']
        
    # Remove the specified stop words (words_to_discard)
    for word in words_to_discard:
    	ancient_stopwords.discard(word)
     
    return ancient_stopwords


# Get ancient stopwords set
ancient_stopwords_set = ancient_stopwords()

# Remove "-" from punctuation list, since it is a part of hyphenated names
custom_punct = string.punctuation.replace('-', '')


""" This function works with ancient_stopwords and preprocesses input text for NLP tasks by:
    1. Tokenizing the text into words
    2. Removing stop words and punctuation
    3. Lemmatizing the tokens to their base forms
    4. Filtering out specific apostrophe-related tokens
    5. Joining the processed tokens back into a single string
    
    Arg:
        text (str): The input text to be processed
    
    Return:
        str: The cleaned and processed text
"""
 
def prepare_text(text):

    # Tokenize text
    tokens = word_tokenize(text)
    
    # Remove stop words and punctuation
    filtered_tokens = [token for token in tokens if token not in ancient_stopwords_set and
                       token not in custom_punct
                      ]
        
    # Lemmatize tokens
    # Initialize lemmatizer
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    
    # Filter out tokens that are just an apostrophe or start with an apostrophe
    lemmatized_tokens = [token for token in lemmatized_tokens if not (token.startswith("'") or token == "'s" or token == "n't")]
    
    # Join tokens back into a spaced string
    processed_text = ' '.join(lemmatized_tokens)
    
    return processed_text
    
    
    
    
    
    
    
    
    
    
    