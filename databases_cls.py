# pip install pymysql---
# 30/04/2024

import pymysql

# connecting to the db server..

db_conn=pymysql.connect(user='root',password='Swati@123',host='localhost',database='python_ban')

db_cur=db_conn.cursor()

#create the database..
# db_cur.execute('create database python_8am')

# print(db_cur.execute('show tables'))

# print(db_cur.fetchall())

# db_cur.execute("create table player_info(p_name varchar(30),p_team varchar(4),p_age integer,p_price varchar(6))")

# db_cur.execute("insert into player_info(p_name,p_team,p_age,p_price) values('kohli','RCB',36,'15 cr')")

# db_cur.execute("insert into player_info(p_name,p_age,p_price,p_team)  values('Rohith',36,'16 CR','MI'),('Rahul',34,'17 cr','KKR'),('Dhoni',38,'15 cr','CSK')")

# print(db_cur.execute("select * from player_info"))

# print(db_cur.fetchall())

# db_cur.execute("update player_info SET p_age=35, p_name='RCB'' where p_name='Rahul'")

# db_cur.execute("alter table player_info add p_role varchar(15) NOT NULL DEFAULT 'ALLrounder'")

# db_cur.execute("drop table player_info")

db_cur.execute("drop databse python_ban")
db_conn.commit()
db_conn.close()