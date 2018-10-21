import string
from library import databasecheck
from library.usermodel import User
import re

class Check:

    error = ''

    def checkusername(uname):
        while len(uname) <= 12:
            for loop in uname:
                if loop == '1':
                    return False
                elif loop == '2':
                    return False
                elif loop == '3':
                    return False
                elif loop == '4':
                    return False
                elif loop == '5':
                    return False
                elif loop == '6':
                    return False
                elif loop == '7':
                    return False
                elif loop == '8':
                    return False
                elif loop == '9':
                    return False
                elif loop == '0':
                    return False
                elif loop == '!':
                    return False
                elif loop == '@':
                    return False
                elif loop == '#':
                    return False
                elif loop == '%':
                    return False
                elif loop == '$':
                    return False
                elif loop == '&':
                    return False
                elif loop == '*':
                    return False
                elif loop == '.':
                    return False
                elif loop == ',':
                    return False

            else:
                if len(uname) == 0:
                    return False
                else:
                    return True

    def checknickname(niname):
        if len(niname) > 16 or len(niname) == 0:
            return False
        for c in niname:
            if c.isdigit():
                return False
            if c in set(string.punctuation):
                return False

        return True

    def checkpassword(pword):
        while (len(pword) >= 8) and (len(pword) <= 16):
            for loop_i in pword:
                if loop_i == '*':
                    return False
                elif loop_i == '#':
                    return False
                elif loop_i == '!':
                    return False
                elif loop_i == '&':
                    return False
                elif loop_i == '%':
                    return False
                elif loop_i == '$':
                    return False
                elif loop_i == '@':
                    return False
                elif loop_i == ',':
                    return False
                elif loop_i == '.':
                    return False
                elif not any(loop_i.isupper() for loop_i in pword):
                    return False
                elif not any(loop_i.islower() for loop_i in pword):
                    return False
                elif not any(loop_i.isdigit() for loop_i in pword):
                    return False
            else:
                return True

    def checkdateofbirth(self, birth):
        month = int(birth[0:2])
        day = int(birth[2:4])
        year = int(birth[4:8])
        if len(birth) > 8 or len(birth) == 0:
            return False
        if month < 1 or month > 12:
            return False
        if any(month == c for c in(1, 3, 5, 7, 8, 10, 12)):
            if day > 31 or day < 1:
                return False
        if any(month == c for c in(4, 6, 9, 11)):
            if day > 30 or day < 1:
                return False
        if year > 2018:
            return False
        if month == 2 and (day != 28 or day != 29):
            return False
        if month == 2 and day == 28 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            return False
        if month == 2 and day == 29 and ((year % 4 != 0 or year % 100 == 0) or (year % 400 != 0)):
            return False
        return True

    def checkemail(self, email):
        while "@" and "." not in email:
            return False
        else:
            email_pattern = re.search("(^[a-z0-9A-Z-.]+\@[a-z0-9A-Z-.]+\.[a-zA-Z0-9-.])", email)
            return bool(email_pattern)

    def checkhomepage(self, uname, pword):
        global error
        if (self.checkusername(uname) and self.checkpassword(pword)) is False:
            error = 'You entered invalid Username or Password!!!!!'
            return False
        if self.checkdatabasehomepage(uname, pword) is False:
            return False
        else:
            return True

    def checkdatabasehomepage(uname, pword):
        global error
        if databasecheck.checkUsrName(uname):
            if databasecheck.logIn(uname, pword) is False:
                error = 'You entered invalid Username or Password!!!!!'
                return False
            else:
                User.setInfo(User, uname, pword)
                return True
        else:
            error = 'You need to sign Up!!!!!'
            return False


    def geterror(self):
        return error

    def checkeditpage(self, emailv, birthv):
        global error
        print('I am Here!!!!!!!!!!!!!!!!!!!!!!!')
        if self.checkemail(Check, emailv) and self.checkdateofbirth(Check, birthv):
            return True
        else:
            error = 'You have invalid input'
            return False

    def checksignuppage(self,uname,pword,email,birth):
        global error
        if self.checkusername(uname) and self.checkpassword(pword) and self.checkemail(Check,email) and self.checkdateofbirth(Check, birth):
            if databasecheck.checkUsrName(uname) is False:
                return True
            else:
                error = 'The username you have entered is already taken by someone!!!!'
                return False
        else:
            error = 'You have entered invalid information!!!!'
            return False


