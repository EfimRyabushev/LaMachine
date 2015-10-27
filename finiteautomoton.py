__author__ = 'student'

class FiniteAutomon():
    def __init__(self, alfabet, start, finish, switches):
        self.alfabet = alfabet
        self.start = start
        self.current = start
        self.finish = finish
        self.switches = switches
    def getChar(self, char):
        if char in self.alfabet:
            for i in self.switches:
                if self.current == i[0] and char == i[1]:
                    self.current = i[2]
                    return True
        self.current = self.start
        return False
    def getString(self, string):
        for i in string:
            if self.getChar(i):
                pass
            else:
                return False
        if self.current in self.finish:

           self.current = self.start
           return True
        else:
            self.current = self.start
            return False

start = '0'
finish = '1'
ways = [['0', 'a', '1'], ['1', 'b', '0']]
automon = FiniteAutomon('ab', start, finish, ways)
test = automon.getString('aba')
print (test)