# user -- Username,password,email
records = []

from MySqlConnection import cursor,cnx
from hash import verify

class Users():
    def Login(self,username="",password="",email=""):
        if (self.email==email or self.username==username) and  self.password==password:
           print("running")
           return True
        return False



class Authentication():

    def Register(username="",password="",email="",role="user"):
        query = "insert into  users value(%s,%s,%s,%s);"
        cursor.execute(query,(username,password,email,role))
        empno=cursor.lastrowid
        print(empno)
        cnx.commit()

    def Login(username="",userpassword="",email=""):
        query = "select * from users where username=%s"
        cursor.execute(query,[username])
        k = cursor.fetchall()
        for (username,password,email,role) in k:
            if verify(password,userpassword):
                return True
        return False

