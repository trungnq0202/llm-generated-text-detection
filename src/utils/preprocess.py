from bs4 import BeautifulSoup
import re

chars_to_remove = ['{', '£', '\x97', '¹', 'å', '\\', '\x85', '<', '\x99', \
                  'é', ']', '+', 'Ö', '\xa0', '>', '|', '\x80', '~', '©', \
                  '/', '\x93', '$', 'Ó', '²', '^', ';', '`', 'á', '*', '(', \
                  '¶', '®', '[', '\x94', '\x91', '#', '-', 'ó', ')', '}', '=']

def remove_html_tags(text):
    bsoup = BeautifulSoup(text, "html.parser")
    return bsoup.get_text()

def remove_multiple_whitespace_chars(text):
    return re.sub(r'\s+', ' ', text)

def remove_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)

def remove_special_chars(text):
    for c in chars_to_remove:
        text = text.replace(c, '')

    return text
    # return re.sub('[^a-zA-z0-9\s]', '', text)

def remove_end_of_text_token(text):
    return text.replace("<|end_of_text|>", "")

def preprocess_essay(text):
    # pre-process -----
    text = remove_end_of_text_token(text)

    text = text.encode("ascii", "ignore").decode('ascii')        
    text = text.strip()
    text = text.strip("\"")

    text = remove_special_chars(text)

    if text[-1]!=".":
        text = text.split(".")
        text = ".".join(text[:-1])
        text += "."
    
    text = remove_html_tags(text)
    # text = remove_multiple_whitespace_chars(text)
    text = remove_square_brackets(text)

    return text


