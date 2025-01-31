class StringManipulator:
    def _init_(self):
        self.text = ""

    def getString(self):
        self.text = input("Введите строку: ")

    def printString(self):
        print(self.text.upper())

s = StringManipulator()
s.getString() 
s.printString()