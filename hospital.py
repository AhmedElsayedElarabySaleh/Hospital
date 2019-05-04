
# Importing Models
from mysql.connector import *


############################################## Coding App ###################################################
print ("*"*25)
while True:
    print ('')
    print ("****************************************** ^-^ Welcome In Hospital App ^-^ **************************************************")
    print ('')
    print (" $- If You want Add Doctor Press < 1 > ")
    print ('')
    print (" $- If You Want Display All Hurts Press < 2 > ")
    print ('')
    print (" $- If You want Display All Doctor Who Are More Than 15 Years Experence Press < 3 > ")
    print ('')
    print (" $- If You Wnat Delete A Doctor Prss < 4 > ")
    print ('')
    print (" $- If You Want Display All Doctors In Our Databases Press < 5 > ")
    print ('')

    class Hospital():
        def __init__(self,):
            self.ask()


        def ask(self):
            a = input("Command <>")

            if a == '1' :
                self.add_doctor()
            elif a == '2':
                self.Display_All_Hurt()
            elif a == '3':
                self.Display_All_doctor_who()

            elif a == '4':
                self.Delete_Doctor()
            elif a == '5':
                self.Display_All_doctor()



        def add_doctor(self):
            try:
                cdb = connect(user = 'root',
                    password = "",
                    host = 'localhost',
                    database = 'hospital'
                                )
                a = input (" Enter The Name Doctor : " )
                b = input (" Enter The Salary :" )
                c = input (" Enter The Year Of Experience : " )
                d = input (" Enter The Specialty : " )
                cu = cdb.cursor()
                print ("Connection Done!!!") 
                sql = "INSERT INTO doctor (name,salary,year_o_e,specialty) VALUES ('%s', '%s','%s','%s')"%(a, b,c,d)
                cu.execute(sql)
                cdb.commit()
                print("Add Successfull")

                cdb.close()
                print("close")
            except Exception:
                print ("####### Error Please Close App And Try Again #######")


        def Display_All_Hurt(self):

            try:
                cdb = connect(user = 'root',
                    password = "",
                    host = 'localhost',
                    database = 'hospital'
                                )
                cu =cdb.cursor()
                sql = ''' SELECT * FROM doctor  WHERE specialty = 'hurt' '''
                cu.execute(sql)
                var = cu.fetchall()
                a = (var)
                for i in a :
                    print ('id : '+str(i[0])+' -'+ ' Name ' +' : ' +str(i[1])+' - '  + str(i[4])+' specialty')

                    print (' ')
            except Exception():
                print ("####### Error Please Close App And Try Again #######")



        def Display_All_doctor_who(self):#Display All Doctor Who have Experinces more than 15 

            try:
                cdb = connect(user = 'root',
                    password = "",
                    host = 'localhost',
                    database = 'hospital'
                                )
                cu =cdb.cursor()
                sql = ''' SELECT * FROM doctor  WHERE year_o_e >= 15 '''
                cu.execute(sql)
                var = cu.fetchall()
                a = (var)
                print ("The Doctors Who Have More Than 15 years Experinces")
                print ("____________________________________________________")
                for i in a :
                    print ('id : '+str(i[0])+' -'+ ' Name ' +' : ' +str(i[1])+' - ' +' Expreinces is > ' + str(i[3])+' years')
                    print (' ')
                print ("____________________________________________________")
            except Exception():
                print ("####### Error Please Close App And Try Again #######")
        
        


        def Delete_Doctor(self):

            try:
                cdb = connect(user = 'root',
                    password = "",
                    host = 'localhost',
                    database = 'hospital'
                                )
                cu =cdb.cursor()
                a = input("Input Name For Delete : ")
                c = input("Input Id Of Doctors : ")
                sql=cu.execute('''DELETE FROM doctor WHERE name ='%s'  AND id = '%s' ''' % (a,c))
                cu.execute(sql)
                cdb.commit()
                print (" ")
                print ("Delete :" + a + ': Succssefull.')
                
            except Exception():
                print ("####### Error Please Close App And Try Again #######")


        def Display_All_doctor(self):#Display All Doctor  

            try:
                cdb = connect(user = 'root',
                    password = "",
                    host = 'localhost',
                    database = 'hospital'
                                )
                cu =cdb.cursor()
                sql = ''' SELECT * FROM doctor   '''
                cu.execute(sql)
                var = cu.fetchall()
                a = (var)
                print ("This is All Doctor In Our DataBase")
                print ("____________________________________________________")
                for i in a :
                    print ('id : '+str(i[0])+' -'+ ' Name ' +' : ' +str(i[1])+' - ' + 'Salary' + ' : ' + str(i[2]) + 'Expreinces is > ' + str(i[3])+' years'+' - '  + str(i[4])+' specialty')
                    print (' ')
                print ("____________________________________________________")
            except Exception():
                print ("####### Error Please Close App And Try Again #######")




    a=Hospital()
