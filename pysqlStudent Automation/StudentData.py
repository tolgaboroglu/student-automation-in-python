import sqlite3

connection = sqlite3.connect('students.db')

class StudentData:
    def __init__(self,ad):
        self.ad=ad
        self.student=True

    def program(self):
        choose=self.menuChoose()
        
        if choose ==1:
            self.add()
        if choose==2:
            self.show()
        if choose == 3:
            self.delete()
            
    def menuChoose(self):     
        choose=int(input("\nWhat do you want to do?\n0-Exit Program\n1-Add student\n2-Show student\n3-Delete the student\n\nChoose: ".format(self.ad)))
        print("\nPlease choose 0,1,2 or 3 ")
        if choose ==0:
            {
                
                exit("Exit.")

            }
        while choose < 0 or choose >7:
                choose = int(input("Choose 0-3"))           
        return choose

    def show(self):
        
        dataProgram=connection.cursor().execute("select * from Student")
        print(dataProgram.fetchall())
        print(dataProgram)
        connection.commit()    
        


    def add(self):
        Sno=int(input("Enter student no: "))
        SnameS=input("Enter student name and surname: ")
        Sdep=input("Enter student department : ")
        Smail=input("Enter student e-mail adress: ")
        Syear=int(input("Enter student start to school year : "))
        Sfi=int(input('Enter the finish the school year'))
        Sage=int(input("Enter student age : "))
        con=connection.cursor()
        con.execute("insert into Student values(?,?,?,?,?,?)",(Sno,SnameS,Sdep,Smail,Syear,Sfi,Sage))
        connection.commit()
        
        print("Data Succesful")

    def delete(self):
         dataProgram=connection.cursor().execute('select * from Student')
         print(dataProgram.fetchall())
         print(dataProgram)
         Sno=int(input('Enter deleted Student no:'))
         conn = connection.cursor()
         conn.execute("Delete from Student where Student School Number=?", (Sno,))
         connection.commit()
        
         print("Deleted Student.")

student = StudentData("Welcome Program")
while student.program:
    student.program()


