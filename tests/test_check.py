from unittest import TestCase
from library.checkinput import Check


class TestCheck(TestCase):
    def test_checkusernameA(self):
        s = Check
        self.assertTrue(s.checkusername('fasdfs'))

    def test_checkusernameB(self):
        s = Check
        self.assertTrue(s.checkusername('fafsdsdfs'))


    def test_checknicknameA(self):
        s = Check
        self.assertTrue(s.checknickname('fdsad'))

    def test_checknicknameB(self):
        s = Check
        self.assertTrue(s.checknickname('fdsadfdsfsd'))

    def test_checknicknameC(self):
        s = Check
        self.assertFalse(s.checknickname('fdsad32'))

    def test_checknicknameD(self):
        s = Check
        self.assertFalse(s.checknickname('fdsad!/.'))

    def test_checknicknameE(self):
        s = Check
        self.assertTrue(s.checknickname('William'))

    def test_checkdateofbirthA(self):
        s = Check
        self.assertTrue(s.checkdateofbirth(Check, '08201996'))

    def test_checkdateofbirthB(self):
        s = Check
        self.assertFalse(s.checkdateofbirth(Check, '01361996'))

    def test_checkdateofbirthC(self):
        s = Check
        self.assertFalse(s.checkdateofbirth(Check, '13201996'))

    def test_checkdateofbirthD(self):
        s = Check
        self.assertFalse(s.checkdateofbirth(Check, '03321996'))

    def test_checkdateofbirthE(self):
        s = Check
        self.assertFalse(s.checkdateofbirth(Check, '02281996'))

    def test_checkdateofbirthF(self):
        s = Check
        self.assertFalse(s.checkdateofbirth(Check, '02291997'))

    def test_checkdateofbirthG(self):
        s = Check
        self.assertFalse(s.checkdateofbirth(Check, '06202020'))

