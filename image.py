import cv2
from PIL import Image

def rotate_function():
    im1 = Image.open("nelson.jpg")
    im2 = im1.rotate(derece)
    im2.show()
    im2.save("/home/alperen/Masaüstü/alperenexercise/nelson3.jpg")

def open_function():
	resim = cv2.imread("nelson.jpg")
	cv2.imshow("nelson",resim)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def crop_function():
    im = Image.open("nelson.jpg") 
    left = 155
    top = 65
    right = 360
    bottom = 270
    im1 = im.crop((left, top, right, bottom))
    im1.show()
    im1.save("/home/alperen/Masaüstü/alperenexercise/nelson4.jpg")

print("1 - Resmi Aç")
print("2 - Resmi Döndür")
print("3 - Resmi Kırp")

secenek = input("Seç: ")

if secenek == "2":
    derece = int(input("Kaç Derece Dönsün: "))
    rotate_function()

elif secenek == "1":
    open_function()

elif secenek == "3":
    crop_function()

else:
    exit()
