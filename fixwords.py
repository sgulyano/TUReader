ranks = {'ศาสตราจารย์':['ศาสตรจารย์', 'ศาสตราจารย์', 'ศาสตร์ตราจารย์', 'Professor','ศ.(AIT)','ศ.(มจธ.)','ศ.(มทม.)','ศ.(มทส.)','ศ.(มวล.)','ศ.*','ศ.','ศ*','ศ'], 
         'ศาสตราจารย์เกียรติคุณ':['ศาสตราจารย์ กิตติคุณ'], 
         'รองศาสตราจารย์':["รองศาสตร์ตราจารย์", "Associate Professor",'รศ.'],
         "ผู้ช่วยศาสตราจารย์" : ['Assistant Professor','ผศ.','รด.','รศ.ดร.'],
         "ศาสตราจารย์ (พิเศษ)" : ["ศาสตราจารย์พิเศษ",'ศ.พิเศษ']}

def fixranks(word):
    return fixword(word, ranks)

phd = {'ดร.':['ดร','Dr.'] }

def fixphd(word):
    return fixword(word, phd)

status = {'เกษียณ':['กษ.','0','(เกษียณ)','จฬ.','มข.','เกษียณ (ต่ออายุ ราชการ)','เกษียณ (ต่อเวลา ราชการ)','เกษียณ (อาจารย์ พิเศษ)','เกษียณ วุฒิสมาชิก','เกษียน','์'],
          'ลาออก':['ลาออก (พำนักอยู่ อังกฤษ)', 'ลาออก(อยู่ต่างประเทศ)']}
def fixstatus(word):
    return fixword(word, status)

uni = {'มหาวิทยาลัยคริสเตียน':['ม.คริสเตียน'], 
       'จุฬาลงกรณ์มหาวิทยาลัย':['จฬ.'] }
def fixuni(word):
    return fixword(word, uni)


def fixword(word, vocab):
    word = word.strip()
    for key, value in vocab.items():
        if word in value:
            return key
    return word