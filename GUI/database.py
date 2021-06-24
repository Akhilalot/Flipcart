import sqlite3

data = sqlite3.connect("D:\\School\Minor Project\\GUI\\NewCustomers.db")

cursor = data.cursor()

cursor.execute("""CREATE TABLE customers (
    username text not null primary key,
    password text not null,
    segment int,
    isFillSurvey int
)
""")

cursor.execute("""CREATE TABLE survey (
    name text,
    age int,
    gender text,
    dependant_count int,
    income_category text,
    marital_status text,
    education_level text
)
""")

data.commit()

data.close()
