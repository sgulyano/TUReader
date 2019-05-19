# TU Reader รายชื่อผู้ทรงคุณวุฒิเสนอสภามหาวิทยาลัย

เพื่อแก้ปัญหารายชื่อผู้ทรงคุณวุฒิไม่ถูกต้องหรือไม่อัพเดท

---
## Instruction
* รัน readTUfile.ipynb
เพื่อ Clean ข้อมูลที่ทาง มธ. เป็นผู้จัดเก็บ และแยกข้อมูลที่ไม่สามารถแก้ไขได้ลงในไฟล์ *_broken.xlsx
* รัน readMUAfile.ipynb
เพื่อ Clean ข้อมูลที่ สกอ. เป็นผู้จัดเก็บ และแยกข้อมูลที่ไม่สามารถแก้ไขได้ลงในไฟล์ *_broken.xlsx
* รัน combine_csv.ipynb
เพื่อรวมข้อมูลจากทั้งสองแหล่งเข้าด้วยกัน และลบรายชื่อที่ซ้ำกัน

---
## Library Dependency
* NumPy
* Pandas
* [PyThaiNLP](https://github.com/PyThaiNLP/pythainlp)

### วิธี Install PyThaiNLP
พิมพ์ใน Command Line/Terminal
```
pip install pythainlp
```
สำหรับ Windows: ต้อง Install marisa-trie wheels ก่อน ซึ่ง Download ได้ที่ https://www.lfd.uci.edu/~gohlke/pythonlibs/#marisa-trie 
แล้ว Install โดยใช้ pip ให้พิมพ์ว
```
pip install marisa_trie-0.7.5-cp36-cp36m-win32.whl
```
ดูรายละเอียดได้ที่ https://pypi.org/project/pythainlp/
