import mysql.connector

myDB = mysql.connector.connect(
    host ="localhost",
    user = "root",
    passwd = "0786",
    database = "Movies",
)
# print(myDB)

my_cursor = myDB.cursor()

# my_cursor.execute("CREATE DATABASE Movies")

# my_cursor.execute("SHOW DATABASES")
# my_cursor.execute("CREATE TABLE Favorite_Movies(movie_name VARCHAR(255), Lead_Actor VARCHAR(255), Lead_Actress VARCHAR(255), Release_Year YEAR (4), Director_Name VARCHAR(255), movie_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
# my_cursor.commit()

"""
my_cursor.execute("SHOW TABLES")
for table in my_cursor:
    print(table[0])
"""
# sqlStuff = "INSERT INTO favorite_movies(movie_name, Lead_Actor, Lead_Actress, Release_Year, Director_Name) VALUES(%s,%s,%s,%s,%s)"
# record1= ("Bombay", "Arvind Swamy","Manisha Koirala",1995,"Mani Ratnam")

#my_cursor.execute(sqlStuff,record1)
#myDB.commit()


# insert__movies_query="""INSERT INTO favorite_movies(movie_name, Lead_Actor, Lead_Actress, Release_Year, Director_Name) 
# VALUES
#("Criminal", "Akkineni Nagarjuna", "Manisha Koirala", 1995, "Mahesh Bhatt"),
#("Tum Mile", "Emraan Hashmi", "Soha Ali Khan", 2010, "Mahesh Bhatt"),
#("Badmaa$h Company", "Shahid Kapoor", "Anushka Sharma", 2010, " Parmeet Sethi")
#"""
#my_cursor.execute(insert__movies_query)
#myDB.commit()


select_movies_query ="SELECT * FROM movies.favorite_movies"
my_cursor.execute(select_movies_query)
result=my_cursor.fetchall()
for row in result:
    print(row)
