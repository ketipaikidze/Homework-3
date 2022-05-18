import json
import sqlite3
import requests

# დავალება 1

connection = sqlite3.connect("persons.db")
cursor = connection.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS employees(
                                    name TEXT NOT NULL,
                                    lastname TEXT,
                                    age INTEGER,
                                    city TEXT NOT NULL,
                                    payment INTEGER NOT NULL)''')

connection.commit()

select_city = " SELECT  distinct city, avg(payment) FROM employees"
cursor.execute(select_city)

# დავალება 2

SERVICE_URL = "https://httpbin.org/post"
header = {"content-type": "application/json"}

car = {
    "mark": "mercedes",
    "model": "E-class",
    "builder": "Germany",
    "price": 60000
}

response = requests.post(SERVICE_URL + "/car", json=car, headers=header)
print(response.json())

# დავალება 3

URL = "https://httpbin.org/image/webp"
response = requests.get(URL)
open("image.jpg", "wb").write(response.content)