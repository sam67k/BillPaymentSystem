import datetime
import time
user = 0
user += 1

def Start():
    with open("log.csv","a") as f:
        f.write(str(user))
        f.write(",")
        f.write(str(datetime.datetime.now()))
        f.write(",")
        f.write("Program Started")
        f.write("\n")
    print("\t\tWelcome!\n")
    time.sleep(0.75)
    print("\n\tLoading")
    for i in range(30):
        print(".",end="")
        time.sleep(0.1)
    print("\n\tLoading Complete")
    print("\n\tWelcome Again!")
    Main()
    
def Main():
    with open("log.csv","a") as f:
        f.write(str(user))
        f.write(",")
        f.write(str(datetime.datetime.now()))
        f.write(",")
        f.write("Main Menu")
        f.write("\n")
    print("\n1 : Utiliy Bill\n2 : Mobile Load\n0 : Terminate")
    i1 = str(input("\t"))
    if(i1 == "1"):
        Bill()
    elif(i1 == "2"):
        Load()
    elif(i1 == "admin"):
        Login()
    elif(i1 == "0"):
        Terminate()
    else:
        Main()
        
def Terminate():
    print("\nProgram Terminated!")
    with open("log.csv","a") as f:
        f.write(str(user))
        f.write(",")
        f.write(str(datetime.datetime.now()))
        f.write(",")
        f.write("Program Terminated")
        f.write("\n")

def AdminLogin():
    with open("log.csv","a") as f:
        f.write(str(user))
        f.write(",")
        f.write(str(datetime.datetime.now()))
        f.write(",")
        f.write("Admin Login")
        f.write("\n")
    print("\nWelcome my Admin")
    Administrator()
        
def Administrator():
    with open("log.csv","a") as f:
        f.write(str(user))
        f.write(",")
        f.write(str(datetime.datetime.now()))
        f.write(",")
        f.write("Admin Menu")
        f.write("\n")
    def Options():
        print("\n1 : Check Records\n2 : Change Records\n0 : Terminate")
        i2 = int(input("\t"))
        if(i2 == 1):
            CheckRecords()
        elif(i2 == 2):
            ChangeRecords()
        elif(i2 == 0):
            Terminate()
        else:
            Main()
    Options()

def CheckRecords():
    i1 = 0
    def PrintRecord(file):
        with open(file,"r") as f:
            for line in f:
                print(line)
    def CallRecord():
        print("\n1 : Print Log\n2 : Print Electricity Bill Records\n3 : Print Water Bill Records\n4 : Print Gas Bill Records\n5 : Print Telephone Bill Records\n6 : Print Mobile Load Records\n0 : Back to Admin Menu")
        i3 = int(input("\t"))
        if(i3 == 1):
            PrintRecord("log.csv")
            CallRecord()
        elif(i3 == 2):
            PrintRecord("ElectricityBillRecords.csv")
            CallRecord()
        elif(i3 == 3):
            PrintRecord("WaterBillRecords.csv")
            CallRecord()
        elif(i3 == 4):
            PrintRecord("GasBillRecords.csv")
            CallRecord()
        elif(i3 == 5):
            PrintRecord("TelephoneBillRecords.csv")    
            CallRecord()
        elif(i3 == 6):
            PrintRecord("MobileLoadRecords.csv")
            CallRecord()
        elif(i3 == 0):
            Administrator()
        else:
            Main()
    CallRecord()
    
def ChangeRecord():
    print("\n1 : Update Electricity Bill Records\n2 : Update Water Bill Records\n2 : Update Gas Bill Records\n4 : Update Telephone Bill Records\n0 : Back to Admin Menu")
    i3 = int(input("\t"))
    if(i3 == 1):
        RecordUpdater("ElectricityBillRecords.csv","Electircity")
        ChangeRecord()
    elif(i3 == 2):
        RecordUpdater("WaterBillRecords.csv","Water")
        ChangeRecord()
    elif(i3 == 3):
        RecordUpdater("GasBillRecords.csv","Gas")
        ChangeRecord()
    elif(i3 == 4):
        RecordUpdater("TelephoneBillRecords.csv","Telephone")    
        ChangeRecord()
    elif(i3 == 0):
        Administrator()
    else:
        Main()

def RecordUpdater(filename,utility):
    print("\nAdmin is now in",utility,"Bill Record Updater Menu")
    with open("log.csv","a") as f:
        f.write(str(user))
        f.write(",")
        f.write(str(datetime.datetime.now()))
        f.write(",")
        f.write(utility)
        f.write(" Bill Record Updating Menu")
        f.write("\n")
    def UpdateRecords():
        with open(filename,"w") as f:
            for r in range(len(lst)):
                f.write(str(lst[r][0]))
                f.write(",")
                f.write(str(lst[r][1]))
                f.write("\n")
    lst = []
    def RecordCheck(i3):
        with open(filename,"r") as f:
            for line in f:
                lst.append(line.strip().split(","))
            for r in range(len(lst)):
                if(i3 == int(lst[r][0])):
                    return True
    def RecordUpdated():
        with open("log.csv","a") as f:
            f.write(str(user))
            f.write(",")
            f.write(str(datetime.datetime.now()))
            f.write(",")
            f.write(utility)
            f.write(" Bill Record Updated")
            f.write("\n")
        print("\n1 : Update Anothr Bill Record\n0 : Admin Menu")
        c = int(input("\t"))
        if(c == 0):
            Administrator()
        elif(c == 1):
            RecordFounder()
        else:
            Main()
    def payment(i3):
        for r in range(len(lst)):
            if(i3 == int(lst[r][0])):
                print("\nRecord Found")
                break
        print("\nBill Amount in Record : ",lst[r][1])
        print("\n1 : Add/Sub from current Bill\n2 : Change Current Bill\n0 : Back")
        i4 = int(input("\t"))
        if(i4 == 1):
            print("\n1 : Add to Current Bill\n2 : Sub from Current Bill\n0 : Back")
            i5 = int(input("\t"))
            if(i5 == 1):
                print("\nAmount you want to add to : ",lst[r][1])
                i6 = int(input("\t"))
                nb = int(lst[r][1]) + i6
                lst[r][1] = nb
                print("\nNew Amount to Records : ",lst[r][1])
                UpdateRecords()
                RecordUpdated()
            elif(i5 == 2):
                print("\nAmount you want to sub from :", lst[r][1])
                i6 = int(input("\t"))
                while(i6 > int(lst[r][1])):
                    print("\nAmount more than in Record")
                    print("\nAmount you Want to Pay from", lst[r][1])
                    i6 = int(input("\t"))
                nb = int(lst[r][1]) - i6
                lst[r][1] = nb
                print("\nNew Amount to Records : ",lst[r][1])
                UpdateRecords()
                RecordUpdated()
            else:
                Main()
        elif(i4 == 2):
            print("\nCurrent Amount in Record : ",lst[r][1])
            print("\nChange current amount with")
            i5 = int(input("\t"))
            lst[r][1] = i5
            print("\nNew Amount to Records : ",lst[r][1])
            UpdateRecords()
            RecordUpdated()
        elif(i4 == 0):
            RecordFounder()
        else:
            Main()
    def RecordFounder():
        print("\nEnter Bill Number")
        i3 = int(input("\t"))
        if(RecordCheck(i3)):
            condition = True
            payment(i3)
        else:
            condition = False
        while(condition != True):
            print("\nEnter Bill Number Again")
            i3 = int(input("\t"))
            if (RecordCheck(i3)):
                condition = True
                payment(i3)
            else:
                condition = False
    RecordFounder()

def Login():
    import getpass
    def login(): 
        lst = []
        user = input("\nUsername: ")
        password = getpass.getpass("Password: ")
        with open("Login.csv","r") as f:
            for line in f:
                lst.append(line.strip().split(","))
        for r in range(2):
            for c in range(1):
                if(user == lst[r][c]) and (password == lst[r][c+1]):
                    print("\nLogin successful!")
                    return True
                else:
                    print("\nWrong username/password")
                    print("\tTry Again")
                    return False
    count = 0
    if(login()):
        condition = True
    else:
        count += 1
        condition = False
    while(condition != True and count < 3):
        if(login()):
            condition = True
        else:
            count += 1
            condition = False
    AdminLogin()

#Fuction for Utility Bill
def Bill():
    with open("log.csv","a") as f:
        f.write(str(user))
        f.write(",")
        f.write(str(datetime.datetime.now()))
        f.write(",")
        f.write("All Utilities Bill Menu")
        f.write("\n")
    print("\n1 : Electricity Bill\n2 : Gas Bill\n3 : Water Bill\n4 : Telephone\n0 : Back to Main Menu")
    i2 = int(input("\t"))
    if(i2 == 1):
        BillPayment("ElectricityBillRecords.csv","Electricity")
    elif(i2 == 2):
        BillPayment("GasBillRecords.csv","Gas")
    elif(i2 == 3):
        BillPayment("WaterBillRecords.csv","Water")
    elif(i2 == 4):
        BillPayment("TelephoneBillRecords.csv","Telephone")
    elif(i2 == 0):
        Main()
    else:
        Main()

#Function for Utility Bill Payment 
def BillPayment(filename,utility):
    print("\nUser Number \"",user,"\" is now in",utility,"Bill Payment Menu")
    with open("log.csv","a") as f:
        f.write(str(user))
        f.write(",")
        f.write(str(datetime.datetime.now()))
        f.write(",")
        f.write(utility)
        f.write(" Bill Payment Menu")
        f.write("\n")
    def UpdateRecords():
        with open(filename,"w") as f:
            for r in range(len(lst)):
                f.write(str(lst[r][0]))
                f.write(",")
                f.write(str(lst[r][1]))
                f.write("\n")
    lst = []
    def RecordCheck(i3):
        with open(filename,"r") as f:
            for line in f:
                lst.append(line.strip().split(","))
            for r in range(len(lst)):
                if(i3 == int(lst[r][0])):
                    return True
    def BillPayed():
        with open("log.csv","a") as f:
            f.write(str(user))
            f.write(",")
            f.write(str(datetime.datetime.now()))
            f.write(",")
            f.write(utility)
            f.write(" Bill Paid")
            f.write("\n")
        print("\n1 : Pay Another Bill\n0 : Bill Menu")
        c = int(input("\t"))
        if(c == 0):
            Bill()
        elif(c == 1):
            Pay()
        else:
            Main()
    def payment(i3):
        for r in range(len(lst)):
            if(i3 == int(lst[r][0])):
                print("\nRecord Found")
                break
        print("\nYour Remaining Bill : ",lst[r][1])
        print("\nAmount you Want to Pay from", lst[r][1])
        i4 = int(input("\t"))
        while(i4 > int(lst[r][1])):
            print("\nAmount more than due")
            print("\nAmount you Want to Pay from", lst[r][1])
            i4 = int(input("\t"))
        nb = int(lst[r][1]) - i4
        lst[r][1] = nb
        if(nb == 0):
            print("\nBill Cleared")
            UpdateRecords()
            BillPayed()
        elif(nb != 0):
            print("\nYour Remaining Dues : ",nb)
            UpdateRecords()
            BillPayed()
        else:
            Main()
    def Pay():
        print("\nEnter Bill Number")
        i3 = int(input("\t"))
        if(RecordCheck(i3)):
            condition = True
            payment(i3)
        else:
            condition = False
        while(condition != True):
            print("\nBill Number",i3,"not Found in Record")
            print("\nEnter Bill Number Again")
            i3 = int(input("\t"))
            if (RecordCheck(i3)):
                condition = True
                payment(i3)
            else:
                condition = False
    def UserCheck():
        print("\n1 : Pay Bill\n0 : Bill Menu(Go Back)")
        ci = int(input("\t"))
        if(ci == 0):
            Bill()
        elif(ci == 1):
            Pay()
        else:
            Main()
    UserCheck()

#Function for Mobile Load
def Load():
    with open("log.csv","a") as f:
        f.write(str(user))
        f.write(",")
        f.write(str(datetime.datetime.now()))
        f.write(",")
        f.write("Mobile Load Menu")
        f.write("\n")
    def RecordUpdater(i2,i3):
        with open("MobileLoadRecords.csv","a+") as f:
            f.write(str(i2))
            f.write(",")
            f.write(str(i3))
            f.write(",")
            f.write(str(datetime.datetime.now()))
            f.write("\n")
    import re
    def NumberValidTest(i2):
        Pattern = re.compile("^((\+92)|(0092))-{0,1}\d{3}-{0,1}\d{7}$|^\d{11}$|^\d{4}-\d{7}$")
        return Pattern.match(i2)
    def Process():
        print("\nEnter Cellphone Number")
        i2 = (input("\t"))
        if (NumberValidTest(i2)):
            condition = True
        else:
            condition = False
        while(condition != True):
            print("\nNumber not Valid Pakistan Cell Number")
            print("\nEnter Cellphone Number Again")
            i2 = (input("\t"))
            if (NumberValidTest(i2)):
                condition = True
            else:
                condition = False
        print("\nEnter Amont to Add to",i2,"Account")
        i3 = int(input("\t"))
        RecordUpdater(i2,i3)
        print("\nDear Customer\n\t",i3," has been Added to",i2,"Account\n")
        time.sleep(1)
        LoadDone()
    def LoadDone():
        with open("log.csv","a") as f:
            f.write(str(user))
            f.write(",")
            f.write(str(datetime.datetime.now()))
            f.write(",")
            f.write("Mobile Load Complete")
            f.write("\n")
        UserCheck2()
    def UserCheck2():
        print("\n1 : Another Load\n0 : Main Menu(Go Back)")
        ci = int(input("\t"))
        if(ci == 0):
            Main()
        elif(ci == 1):
            Process()
        else:
            Main()
    def UserCheck():
        print("\n1 : Load\n0 : Main Menu(Go Back)")
        ci = int(input("\t"))
        if(ci == 0):
            Main()
        elif(ci == 1):
            Process()
        else:
            Main()
    UserCheck()