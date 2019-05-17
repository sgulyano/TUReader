from string import punctuation, whitespace

ranks = {'Mr.':[''],
         'Miss':[''],
         'ทพ.':[''],
         'ม.ร.ว.':['มรว.'],
         'พ.ต.ต.':[''],
         'พ.ต.':[''],
         'ทพญ.':[''],
         'น.ท.' :[''],
         'น.ลพ.' :[''],
         'พ.ต.ท.' :[''],
         'น.ส.' :[''],
         'น.อ.' :[''],
         'นพ.' :[''],
         'พ.ต.อ.' :[''],
         'พ.อ.' :[''],
         'พญ.' :[''],
         'ภก.' :[''],
         'ภญ.' :[''],
         'มล.' :[''],
         'ร.ต.อ. ดร.' :[''],
         'ร.อ.' :[''],
         'รศ.' :[''],
         'ลพ.ญ.' :[''],
         'ว่าที่ ร.ต.' :[''],
         'ศ.' :[''],
         'สพ.ญ.':['']}


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
