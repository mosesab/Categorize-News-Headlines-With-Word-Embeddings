
import re
import unicodedata
import os 

def strip_accents(text):
    """
    Strip accents from input String.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)
    
def strip_digitsAndSpecialChars(text):
    """
    Convert input text to id.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    text = re.sub('[ ]+', ' ', text)
    #substitute values that aren't letters,numbers,underscore or dot
    text = re.sub('[^0-9a-zA-Z_.]', ' ', text)
    # seperate dot from text by adding whitespace to it
    text =  re.sub('[.]', ' . ', text)
    #substitute digits with whitespace
    text =  re.sub('[0-9]', ' ', text)
    #substitute single letter words with white_space
    text = re.sub(r'(?:^| )\w(?:$| )', ' ', text)

    return text
    

def clean_text(text):
    """
    Applies all the filters to input text.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :return type: String.
    """
    text = text.lower()
    text = strip_accents(text)
    text = strip_digitsAndSpecialChars(text)
      
    return text

