class Students:
    count=0
    def __init__(self,id,fname,lname,course,year,gpa,university,mobile):
        self.StudentID=id
        self.StudentFirstName=fname
        self.StudentLastName=lname
        self.Course=course
        self.Year=year
        self.Gpa=gpa
        self.University=university
        self.Email=self.Gen_Email()
        self.Mobile=mobile
        Students.count+=1
    def Gen_Email(self):
        return self.StudentFirstName+self.StudentLastName+'@'+self.University+'.in'
    def StudentDetails(self):
        out="ID = "+self.StudentID+"\n"+"FirstName = "+self.StudentFirstName+"\n"+"LastName = "+self.StudentLastName+"\n"+"University = "+self.University+"\n"+"Email = "+self.Email
        return out
    
if __name__=="__main__":
    st1=Students('190031187','Nerella','Radhakrishna','CSE',2,9.67,'kluniversity',7286009239)
    print("count= ",Students.count)
    print(st1.StudentDetails())
    print()
    st2=Students('190031134','Nerella','Pavan','CSE',2,9,'kluniversity',9866341486)
    print("count= ",Students.count)
    print(st2.StudentDetails())
    print()
    st3=Students('190031249','Panapakam','Mohith','CSE',2,9,'kluniversity',8328130161)
    print("count= ",Students.count)
    print(st3.StudentDetails())
