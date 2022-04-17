import mysql.connector as mysql

mydb = mysql.connect(
    host="localhost",
    user="",
    password="",
    port="3306",
    db="python_cookbook"
)

mycursor = mydb.cursor()

mycursor.execute("INSERT into recipes (id, uri, label) values (?, ?, ?)", (id, recipe_uri , recipe_label)
