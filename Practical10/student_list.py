#student list
class Student (object): #create a class
    def __init__(self, first_name, last_name, programme): #define three attributes
        self.first_name = first_name
        self.last_name = last_name
        self.programme = programme
    def __str__ (self): #align the input information with defined attributes
        return "name:%s %s programme:%s" % (self.first_name, self.last_name, self.programme)
a = Student('Chen','Yijia','BMS') #use an example to test the codes
print(a)
