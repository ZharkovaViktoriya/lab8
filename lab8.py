from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
def z1():
    image=Image.open('otkritka.jpg')
    crop=image.crop((0, 257, 564,846 ))
    crop.show()
    crop.save('new otkritka.jpg')

def z2():
    otkritki={"Новый год":"ng.jpg","День рождения":"dr.jpg","8 марта":"8marta.jpg"}
    prazdnik=str(input("К какому празднику нужна открытка? "))
    name=otkritki[prazdnik]
    image=Image.open(name)
    image.show()

def z3():
    image = Image.open('otkritka.jpg')
    crop = image.crop((0, 257, 564, 846))
    name=str(input("Введите имя: "))
    text=name+", поздравляю!"
    draw = ImageDraw.Draw(crop)
    font = ImageFont.truetype("ofont.ru_Futurespore.ttf", 50)
    x,y=crop.size
    t_x=draw.textlength(text,font=font)
    x=(x-t_x)/2
    draw.text((x,0),text, fill=(0, 255, 0), font=font,stroke_width=2,stroke_fill=(0,255,0))
    crop.show()
    crop.save('new_otkritka.png')
z1()
z2()
z3()