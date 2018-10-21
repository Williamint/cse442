
from library import databasecheck


class User:
    username = ''
    nickname = ''
    password = ''
    dateofbirth = ''
    email = ''
    education = ''
    firstname = ''
    lastname = ''
    userstory = ''
    friend_listn = ''

    def setusername(self, uname):
        global username
        username = uname

    def setnickname(self, niname):
        global nickname
        nickname = niname

    def setfirstname(self, firstn):
        global firstname
        firstname = firstn

    def setlastname(self, lastn):
        global lastname
        lastname = lastn

    def setpassword(self, pword):
        global password
        password = pword

    def setdobirth(self, birth):
        global dateofbirth
        dateofbirth = birth

    def setemail(self, mail):
        global email
        email = mail

    def seteducation(self, edu):
        global education
        education = edu

    def getusername(self):
        return username

    def getnickname(self):
        return nickname

    def getfirstname(self):
        return firstname

    def getlastname(self):
        return lastname

    def getpassword(self):
        return password

    def getdobirth(self):
        return dateofbirth

    def getemail(self):
        return email

    def geteducation(self):
        return education

    def setuserstory(self, ustory):
        global userstory
        userstory = ustory

    def getuserstory(self):
        return userstory

    def exactInfo(self, dictInfo):
        self.setfirstname(self, dictInfo['firstname'])
        self.setlastname(self, dictInfo['lastname'])
        self.setuserstory(self, dictInfo['userstory'])
        self.setemail(self, dictInfo['email'])
        self.seteducation(self, dictInfo['education'])
        self.setdobirth(self, dictInfo['dateofbirth'])

    def packInfo(self):
        databasecheck.editProfile(self.getusername(self), self.getfirstname(self), self.getlastname(self), self.getemail(self), self.getdobirth(self), self.geteducation(self))

    def setfriend_list(self, f_list):
        print(f_list)
        global friend_listn
        if f_list is False:
            friend_listn = ''
        else:
            friend_listn = f_list

    def getfriend_list(self):
        return friend_listn

    def setInfo(self, uname, pword):
        self.setusername(self, uname)
        self.exactInfo(self, databasecheck.homepgView(uname))
        self.setfriend_list(self, databasecheck.friendsList(uname))

    def saveInfo(self, uname, firstn, lastn, email, dob, edu):
        self.setusername(self, uname)
        self.setfirstname(self, firstn)
        self.setlastname(self, lastn)
        self.setemail(self, email)
        self.setdobirth(self, dob)
        self.seteducation(self, edu)
        self.packInfo(self)

    def clearInfo(self):
        return True






