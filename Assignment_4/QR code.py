import qrcode

name = input("Enter your name PLZ : ")
phone_numer = input("Enter your phone number : ")

pic = qrcode.make(name +"\n"+ phone_numer)

pic.save(" Your _ QRcode.png")