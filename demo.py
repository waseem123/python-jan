import mysql.connector as connector

connection = connector.connect(host="localhost", user="root", password="", database="school")


def insertion():
    try:
        sql = f"INSERT INTO tbl_student(studname,class,dob,marks)VALUES('Alex','6','2010-05-17',0)"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        print("DATA INSERTION SUCCESFUL")
    except:
        print("EXCEPTION OCCURED")


def updation():
    try:
        rollno = int(input("ENTER ROLL NO - "))
        marks = int(input("ENTER MARKS - "))
        email = input("ENTER EMAIL - ")

        sql = f"UPDATE tbl_student SET email='{email}',marks={marks} where rollno={rollno}"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        print("DATA UPDATION SUCCESFUL")
    except:
        print("EXCEPTION OCCURED")


# updation()

def selectAll():
    sql = "SELECT rollno,studname,class from tbl_student;"
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    # print(data)
    for row in data:
        print(f"ROLL NO - {row[0]}")
        print(f"NAME    - {row[1]}")
        print(f"Class   - {row[2]}")
        print(f"________________________")
    cursor.close()
    connection.close()


selectAll()
