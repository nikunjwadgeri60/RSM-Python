import pytesseract as tess
from PIL import Image
import mysql.connector
from datetime import date
from datetime import datetime

now = datetime.now()

today = date.today()

path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
tess.pytesseract.tesseract_cmd = path
img = Image.open("IMAGES0.jpg")
text = tess.image_to_string(img)
mystring = "" + text
print(mystring)
d1 = today.strftime("%d/%m/%Y")
mystring1 = "" + d1
print(mystring1)
time = now.strftime("%H:%M:%S")
mystring2 = "" + time
print(mystring2)

# query to establish a connection to the database
mydb = mysql.connector.connect(host="localhost", user="root", password="1234", database="anpr")

# to create a database
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE anpr")

# to create a table in anpr database
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE vehiclerecords (NumberPlate VARCHAR(255), Date VARCHAR(255) , Time VARCHAR(255))")

# query to insert the data into database
sql = "INSERT INTO vehiclerecords VALUES (%s, %s, %s)"
val = (mystring, mystring1, mystring2)
mycursor.execute(sql, val)
mydb.commit()