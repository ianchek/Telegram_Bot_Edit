from aiogram.types import InputFile

a = InputFile(r'C:\Users\Acer\Desktop\f\1.mp3')
b = InputFile(r'C:\Users\Acer\Desktop\f\2.mp3')
c = InputFile(r'C:\Users\Acer\Desktop\f\3.mp3')
d = InputFile(r'C:\Users\Acer\Desktop\f\4.mp3')
e = InputFile(r'C:\Users\Acer\Desktop\f\5.mp3')

class Make:
    def __init__(self, art, zanr, name, put):
        self.art = art
        self.zanr = zanr
        self.name = name
        self.put = put
    def __str__(self):
        return f"<InputFile 'attach://{self.attachment_key}' with file='{self.put}'>"

a1 = Make('Blaze', 'Hip-hop', 'Music_1234', a)
b1 = Make('PORCHY', 'Rap', 'Trak_28', b)
c1 = Make('Blaze', 'Pop', 'North-abc', c)
d1 = Make('PORCHY', 'Hip-hop', '26-83', d)
e1 = Make('Blaze', 'Pop', 'Abnov', e)

spis = [a1, b1, c1, d1, e1]