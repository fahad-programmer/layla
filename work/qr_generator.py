# Run "pip install pyqrcode" before running this program
import pyqrcode

data = input("Enter the text or link to generate QR code: ")

# Using pyqrcode.create() to create a qr code of the input data 
qr = pyqrcode.create(data)

file_name = input("Enter name of file: ")
# Using .svg method to save the qr code as SVG file of provided name & scale 
qr.svg(file_name + '.svg', scale = 8)
