class Student:
    def __init__(self,studentID, studentName, math, physic, chemistry):
        self.studentID = studentID
        self.studentName = studentName
        self.math = math
        self.physic = physic
        self.chemistry = chemistry

    def setStudentID(self, studentID):
        if len(studentID) != 0:
            self.studentID = studentID
        else:
            print("Id student không hợp lệ")

    def getStudentID(self):
        if len(self.studentID) != 0:
           return self.studentID
        else:
           return "Không tồn tại"
    
    def setStudentName(self, studentName):
        self.studentName = studentName

    def getStudentName(self):
        return self.studentName
    
    def setMath(self, math):
        self.math = math

    def getMath(self):
        return self.math
    
    def setPhysic(self, physic):
        self.physic = physic

    def getPhysic(self):
        return self.physic
    
    def setChemistry(self, chemistry):
        self.chemistry = chemistry

    def getChemistry(self):
        return self.chemistry

    def getInfo(self):
        return str(self.studentID) +' '+self.studentName +' ' +str(self.physic) +' '+ str(self.math) +' '+str(self.chemistry)
    
    def getAverageMark(self):
        return (self.math + self.chemistry + self.physic)/3
    
