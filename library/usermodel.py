
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
    msg_list = ''

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

    def setmsg_list(self, msg):
        global msg_list
        msg_list = msg

    def getmsg_list(self):
        return msg_list

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
        print(databasecheck.editProfile(self.getusername(User), self.getfirstname(User), self.getlastname(User), self.getemail(User), self.getdobirth(User), self.geteducation(User)))
        pass

    def setfriend_list(self, f_list):
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
        self.setmsg_list(self, databasecheck.userstory(uname))

    def saveInfo(self, firstn, lastn, email, dob, edu):
        self.setfirstname(self, firstn)
        self.setlastname(self, lastn)
        self.setemail(self, email)
        self.setdobirth(self, dob)
        self.seteducation(self, edu)
        self.packInfo(self)
        pass

    def clearInfo(self):
        self.setfirstname(self, '')
        self.setlastname(self, '')
        self.setemail(self, '')
        self.setdobirth(self, '')
        self.seteducation(self, '')
        self.setmsg_list(self, '')
        self.setfriend_list(self, '')
        self.setnickname(self, '')
        self.setuserstory(self, '')
        self.setusername(self, '')
        pass




