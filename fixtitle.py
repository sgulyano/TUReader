from pythainlp.tokenize import word_tokenize

def fix_title(word):
    word = word.strip()
    if not word:
        return word
    tokens = word_tokenize(word, engine='newmm')
    if tokens[0] in ['นาย', 'นาง', 'นางสาว']:
        return ''.join(tokens[1:])
    else:
        return word