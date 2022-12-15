import qrcode

name=input(" what's your name?   ")

phone_number=input("what's your phone number?  ")

info= name + phone_number

img=qrcode.make(info)

img.save("info.png")