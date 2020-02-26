from string import punctuation, whitespace

ranks = {'Mr.':[''],
         'Miss':[''],
         'ทพ.':[''],
         'ทพญ.':[''],
         'ม.ร.ว.':['มรว.'],
         'มล.' :[''],
         'พ.ต.ต.':[''],
         'พ.ต.อ.' :[''],
         'พ.ต.ท.' :[''],
         'พ.ต.':[''],
         'พ.อ.' :[''],
         'พญ.' :[''],
         'น.ท.' :[''],
         'น.ลพ.' :[''],
         'น.ส.' :[''],
         'น.อ.' :[''],
         'นพ.' :[''],
         'ภก.' :[''],
         'ภญ.' :[''],
         'ร.ต.อ.' :[''],
         'ร.อ.' :[''],
         'ลพ.ญ.' :[''],
         'ว่าที่ ร.ต.' :[''],
         'สพ.ญ.':[''],
         '' : ['ศ.', 'รศ.', 'ดร.']}

from pythainlp.tokenize import word_tokenize

def get_title(word):
    DONE = False
    title = ''
    while not DONE:
        word = word.strip(punctuation + whitespace)
        DONE = True
        for key, value in ranks.items():
            for a in [key]+value:
                if a:
                    if word.startswith(a):
                        title = title + key
                        word = word[len(a):]
                        DONE = False
                        #print('start with ', a)
                        break
            if not DONE:
                break
    # in case of no special title, only mr, mrs, ms.
    if not title:
        word = word.strip()
        if word:
            tokens = word_tokenize(word, engine='newmm')
            if tokens[0] in ['นาย', 'นาง', 'นางสาว']:
                title = tokens[0]
    return title


def fix_name(word):
    DONE = False
    while not DONE:
        word = word.strip(punctuation + whitespace)
        DONE = True
        for key, value in ranks.items():
            for a in [key]+value:
                if a:
                    if word.startswith(a):
                        word = word[len(a):]
                        DONE = False
                        #print('start with ', a)
                        break
            if not DONE:
                break
    return word
