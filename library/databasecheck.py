from homepage.models import PhotoTb, ProfileTb
from datetime import date as dt


def checkUsrName(usr):
    usrcolumn = list(ProfileTb.objects.values_list('username'))
    usrcolumn = [list(elem) for elem in usrcolumn]
    usrlist = []
    [usrlist.append(elem[0]) for elem in usrcolumn]
    if usr in usrlist:
        return True
    return False


def SubmitSignUp(usr, pwd, usrstory, firstn, lastn, eml, edu, dob):
    if checkUsrName(usr) == False:
        signUpQuery = ProfileTb(username=usr, password=pwd, userstory=usrstory,
                                firstname=firstn, lastname=lastn, email=eml, education=edu,
                                dateofbirth=dob)
        signUpQuery.save()
        return True
    return False

def logIn(usr, pwd):
    if checkUsrName(usr):
        login_row = ProfileTb.objects.get(username=usr)
        if login_row.password == pwd:
            return {'firstname':login_row.firstname,
                    'lastname':login_row.lastname,
                    'userstory':login_row.userstory,
                    'email':login_row.email,
                    'education':login_row.education,
                    'dateofbirth':login_row.dateofbirth}
    return False

def homepgView(usr):
    profile = ProfileTb.objects.get(username=usr)
    usrProfileDic = {'userstory':profile.userstory, 'firstname':profile.firstname,
                     'lastname':profile.lastname, 'email':profile.email,
                     'education':profile.education, 'dateofbirth':profile.dateofbirth }
    return usrProfileDic


def editProfile(usr, firstn, lastn, eml, dob, edu):
    profile_edit = ProfileTb.objects.get(username=usr)
    profile_edit.firstname = firstn
    profile_edit.lastname = lastn
    profile_edit.email = eml
    profile_edit.dateofbirth = dob
    profile_edit.education = edu
    profile_edit.save()
    return 'Profile edited!'

def submitImage(usr, img, cap):
    d = str(dt.today())
    uploadimage = PhotoTb(username=usr, image=img, date=d, caption=cap)
    uploadimage.save()
    return 'image uploaded!'

## return false if friend's username does not exist
## return false if friend's username already in friend list
## return true if successfully add friend
def addFriend(usr, friendusr):
    print(usr, friendusr)
    if checkUsrName(friendusr):
        profile = ProfileTb.objects.get(username=usr)
        originalFriends = profile.friends
        if any(originalFriends is c for c in('', None)):
            profile.friends = friendusr
        elif originalFriends == usr:
            return False
        else:
            if friendusr in originalFriends.split('-'):
                return False
            else:
                profile.friends = originalFriends+'-'+friendusr
        profile.save()
        return True
    return False
##return a list of friends' username
def friendsList(usr):
    profile = ProfileTb.objects.get(username=usr)
    friendsString = profile.friends
    if friendsString is None:
        return False
    else:
        return friendsString.split('-')

def adduserstory(usr, msg):
    profile = ProfileTb.objects.get(username=usr)
    userstoryv = profile.userstory
    userstoryv = userstoryv + '-' + msg
    profile.userstory = userstoryv
    profile.save()
    return userstoryv

def userstory(usr):
    profile = ProfileTb.objects.get(username=usr)
    userstring = profile.userstory
    if userstring is None:
        return False
    else:
        return userstring.split('-')
