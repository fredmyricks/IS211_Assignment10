import sqlite3
#connecting to database

conn=sqlite3.connect("pets.db")

#creating tables
conn.execute('''CREATE TABLE person(
id INT PRIMARY KEY NOT NULL,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INT NOT NULL);''')

conn.execute('''CREATE TABLE pet(
id INT PRIMARY KEY,
name TEXT,
breed TEXT,
age INT,
dead INT);''')

conn.execute('''CREATE TABLE person_pet(
person_id INT,
pet_id INT);''')

#DO NOT CREATE pets.db separately. It will be created automatically.
cur=conn.cursor()
#inserting data into person table
cur.execute("INSERT INTO person (id,first_name,last_name,age) VALUES (1,'James','Smith',41);")
cur.execute("INSERT INTO person (id,first_name,last_name,age) VALUES (2,'Diana','Greene',23);")
cur.execute("INSERT INTO person (id,first_name,last_name,age) VALUES (3,'Sara','White',27);")
cur.execute("INSERT INTO person (id,first_name,last_name,age) VALUES (4,'William','Gibson',23);")
#inserting data into pet table
cur.execute("INSERT INTO pet (id,name,breed,age,dead) VALUES (1,'Rusty','Dalmation',4,1);")
cur.execute("INSERT INTO pet (id,name,breed,age,dead) VALUES (2,'Bella','AlaskanMalamute',3,0);")
cur.execute("INSERT INTO pet (id,name,breed,age,dead) VALUES (3,'Max','CockerSpaniel',1,0);")
cur.execute("INSERT INTO pet (id,name,breed,age,dead) VALUES (6,'Spot','Bloodhound',2,1);")
#inserting data into person_pet table
cur.execute("INSERT INTO person_pet (person_id,pet_id) VALUES (1,2);")
cur.execute("INSERT INTO person_pet (person_id,pet_id) VALUES (2,3);")
cur.execute("INSERT INTO person_pet (person_id,pet_id) VALUES (2,4);")
cur.execute("INSERT INTO person_pet (person_id,pet_id) VALUES (3,5);")
cur.execute("INSERT INTO person_pet (person_id,pet_id) VALUES (4,6);")
conn.commit()
conn.close()