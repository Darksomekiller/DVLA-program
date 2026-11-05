#DVLA programme to check and generate licence plate
#IMPORTS
import random
from datetime import datetime
import time
#define my CONSTANTS
#SEPFEB_ADD_ON = 50
REQ_CHARS = 7
INVALID_LETTERS = 'QIZ'
VALID_FIRST_LETTERS = 'ABCDEFGHKLNMOPRSVWY'
INVALID_FIRST_LETTERS = 'JUTXQIZ'
REGIONS = ["Anglia", "Birmingham", "Cymru(Wales)", "Deeside", "Essex", "Forest & Fens", "Garden of England", "Hampshire /& Dorset",
          "(No Official Mnemonic Found)", "London", "Manchester", "North", "Oxford", "Preston", "Reading", "Scotland", "Severn Valley", 
          "West of England", "Yorkshire"]
FIRST_LETTER = ["A", "B", "C", "D", "E", "F", "G", "H", "K", "L", "M", "N", "O", "P", "R", "S", "V", "W", "Y"]
LIST_Of_DLVA_OFFICES =[['Anglia', 'Peterborough', 'ABCDEFGHJKLMN'], 
 ['Anglia', 'Norwich', 'OPRSTU'], 
 ['Anglia', 'Ipswich', 'VWXY'], 
 ['Birmingham', 'Birmingham', 'ABCDEFGHJKLMNOPRSTUVWXY'], 
 ['Cymru(Wales)', 'Cardiff', 'ABCDEFGHJKLMNO'], 
 ['Cymru(Wales)', 'Swansea', 'PRSTUV'], 
 ['Cymru(Wales)', 'Bangor', 'WXY'], 
 ['Deeside', 'Chester', 'ABCDEFGHJK'], 
 ['Deeside', 'Shrewsbury', 'LMNOPRSTUVWXY'], 
 ['Essex', 'Chelmsford', 'ABCDEFGHJKLMNOPRSTUVWXY'], 
 ['Forest & Fens', 'Nottingham', 'ABCDEFGHJKLMNOP'], 
 ['Forest & Fens', 'Lincoln', 'RSTUVWXY'], 
 ['Garden of England', 'Maidstone', 'ABCDEFGHJKLMNO'], 
 ['Garden of England', 'Brighton', 'PRSTUVWXY'], 
 ['Hampshire /& Dorset', 'Bournemouth', 'ABCDEFGHJ'], 
 ['Hampshire /& Dorset', 'Portsmouth', 'KLMNOPRSTUVXY'], 
 ['Hampshire /& Dorset', 'Portsmouth (Isle of Wight)', 'W'], 
 ['(No Official Mnemonic Found)', 'Luton', 'ABCDEFGHJKL'], 
 ['(No Official Mnemonic Found)', 'Northampton', 'MNOPRSTUVWXY'], 
 ['London', 'Wimbledon', 'ABCDEFGHJ'], 
 ['London', 'Stanmore', 'KLMNOPRST'], 
 ['London', 'Sidcup', 'UVWXY'], 
 ['Manchester', 'Manchester', 'ABCDEFGHJKLMNOPRSTUVWXY'], 
 ['North', 'Newcastle', 'ABCDEFGHJKLMNO'], 
 ['North', 'Stockton', 'PRSTUVWXY'], 
 ['Oxford', 'Oxford', 'ABCDEFGHJKLMNOPRSTUVWXY'], 
 ['Preston', 'Preston', 'ABCDEFGHJKLMNOPRST'], 
 ['Preston', 'Carlisle', 'UVWXY'], 
 ['Reading', 'Reading', 'ABCDEFGHJKLMNOPRSTUVWXY'], 
 ['Scotland', 'Glasgow', 'ABCDEFGHJ'], 
 ['Scotland', 'Edinburgh', 'KLMNO'], 
 ['Scotland', 'Dundee', 'PRST'], 
 ['Scotland', 'Aberdeen', 'UVW'], 
 ['Scotland', 'Inverness', 'XY'], 
 ['Severn Valley', 'Worcester', 'ABCDEFGHJKLMNOPRSTUVWXY'], 
 ['West of England', 'Exeter', 'ABCDEFGHJ'], 
 ['West of England', 'Truro', 'KL'], 
 ['West of England', 'Bristol', 'MNOPRSTUVWXY'], 
 ['Yorkshire', 'Leeds', 'ABCDEFGHJK'], 
 ['Yorkshire', 'Sheffield', 'LMNOPRSTU'], 
 ['Yorkshire', 'Beverley', 'VWXY']]
#Month
currentMonth = datetime.now().strftime("%B")
Months={"March":"Earlymonths",
        "April":"Earlymonths",
        "May":"Earlymonths",
        "June":"Earlymonths",
        "July":"Earlymonths",
        "August":"Earlymonths",
        "September":"Latermonths",
        "October":"Latermonths",
        "November":"Latermonths",
        "December":"Latermonths",
        "January":"Latermonths",
        "February":"Latermonths"
}
#Test cases
test_cases_List = ["AB 21 BHR","AB 23 AAA","AO 23 AAA","EA 23 AAA","BA 23 AAA",
"SB 23 AAA","YY 23 AAA","MC 23 AAA","RD 23 AAA","OO 23 AAA","AA 02 AAA","YY 76 SVW",
"AB 26 AOA","AB 76 AOA","AB 02 AOA","AB 51 AOA","AB 23 AAAA ","AB23AAAA","JA 23 AAA",
"UA 23 AAA","TA 23 AAA","XA 23 AAA","QA 23 AAA","IA 23 AAA","ZA 23 AAA","AQ 23 AAA",
"BI 23 AAA","CZ 23 AAA","AA 00 AAA","AA 52 AAA","AA 28 AAA","AA 78 AAA","AA 20 AAQ",
"AA 20 AIA","AA 20 ZAA","AA 300 AAA","AA 20 AB1","1B 20 AAA","A1 20 AAA","AA 20 AA£",
"%A 20 AAA","A( 20 AAA","12 57 827","AA CB AAA"," "
]
#this function takes a string and strips out the spaces

def strip_spaces(s):
    s = s.replace(' ', '')
    return s

#this function returns True if the final three letters are valid, False otherwise
def validEnd(s):
    for char in s:
      if char in INVALID_LETTERS:
        return False
     
    return True

#this function will find the office given a VALID region
def find_Office(region):

    for i in range(len(LIST_Of_DLVA_OFFICES)):
        if LIST_Of_DLVA_OFFICES[i][0] == region:
            if user_licence_plate[1] in LIST_Of_DLVA_OFFICES[i][2]: # if the second letter of the plate is in the valid codes
                return LIST_Of_DLVA_OFFICES[i][1] # we found the office!!
    return "invalid second letter that office does not exist !!! We should never get here"
#function to check userlicence plate fully
def finalCheck(licence,strip,Reqchar,V1L,IL,Region,Endsection,Firstletter):
    print(licence)
    licence = strip(licence.upper())
#print(strip_spaces(user_licence_plate)) #debug to help us see if it worked

#we will test the licence plate in this order: 1) Fisrt to letters 2) Second two numbers 3) Final three numbers
#each of these tests follows different rules, all three must PASS for a valid licence plate

    if len(licence) != Reqchar:
   #wrong length
        print(f"The licence plate you entered was {len(user_licence_plate)} characters. It should be 7. Note: Spaces don't count")

    elif licence[0] not in V1L or licence[1]  in IL or not licence[1].isalpha() : 
        print('fail - those first two letters include INVALID ONES like Q I Z J U T X or invvalid characters like numbers or special characters')
    else: # if we got here, we have a 7 length string and the first two letter are VALID :)
        print('correct length and first two letters')
    
    try:
        region= Region[Firstletter.index(licence[0])]#find the first letter(region)
        office = find_Office(region)#find the second letter(office)
        print(f'that licence plate was registered in {office}')
    except ValueError:
        print("The first section of your licence plate is invalid")
        
    
   
#slice out the last 3 chars in the licence plate
    final_letters = user_licence_plate[-3:]

    if (Endsection(final_letters)):
        print('that is a valid final 3 letters for a licence plate')
    else:
        print('that is  NOT valid final 3 letters for a licence plate')

#function to reopen menu
def reopenMenu(Reopen,menu):
    while Reopen not in ["Y","N"]:
        Reopen=input("Do you want to reopen the menu?(Y/N)").upper()
    else:
        if Reopen == "N":
            print("Thank you for using me")
            return False
        if Reopen == "Y":
            print("Ok!")
            return True

#Random number selection  and check for second section 26-49,76-99 AKA Section2
def licenceSection2Check(Months,currentMonth,licenceSection2,userchoice):
    LaterMonthAddition=50
    licenceSection2VALID=True
    if userchoice == "1":#for generated licence plates which need a random month and not current month
        if Months[currentMonth] == "Latermonths":
            licenceSection2 +=LaterMonthAddition
    if currentMonth in ["January","February"] and licenceSection2 == "2" or licenceSection2=="02":#if year is 2002 and months are january or february
        licenceSection2 -=1
    #if randomly generated or user input number is single digit 
    if licenceSection2>=0 and licenceSection2<=9:#if number is single digit it will be turned double
        if licenceSection2 >=0 and licenceSection2 <=2:#if number is invalid
            print("<<<Invalid year of registration>>>")
        Car_age=licenceSection2
        licenceSection2=str(licenceSection2)
        licenceSection2="0"+licenceSection2
    else:
        while licenceSection2VALID:
            if licenceSection2>26 and licenceSection2<=51:#invalid time frame
                print("<<<Invalid year of registration>>>")
                if licenceSection2>=0 and licenceSection2<=9:
                    licenceSection2=str(licenceSection2)
                    licenceSection2="0"+licenceSection2
                    licenceSection2VALID=False
                break
            elif licenceSection2>76 and licenceSection2<=99:#invalid time frame
                print("<<<Invalid year of registration>>>")
                break
            else:
                licenceSection2VALID=False#to stop while loop
            
    if type(licenceSection2) is str:#if number was single digit and needs to have first print
        print(f"Your car's age is {Car_age}, {currentMonth}")
    if type(licenceSection2) is int:#second print for normal double digit numbers
        if licenceSection2 >=LaterMonthAddition:#if number above 50
            print(f"Your car's age is {licenceSection2-LaterMonthAddition}, {currentMonth}")
        else:#if number not above 50
            print(f"Your car's age is {licenceSection2}, {currentMonth}")

    licenceSection2=str(licenceSection2)
    return licenceSection2

#Generate a random licence plate for if userchoice is 1----------------------------------------------------------------
#random letter selection for 1st section

licenceSection1FIRST=["A","B","C","D","E","F","G","H","K","L","M","N","O","P","R","S","V","W","Y"]
licenceSection1SECOND=["A","B","C","D","E","F","G","H","J","K","L","M","N","O","P","R","S","T","U","V","W","X","Y"]
FIRSTLength=len(licenceSection1FIRST)
SECONDLength=len(licenceSection1SECOND)
while FIRSTLength !=1:
    FIRSTLength=len(licenceSection1FIRST)-1
    
    RandomRemove= random.randint(0,FIRSTLength)
    licenceSection1FIRST.pop(RandomRemove)
while SECONDLength !=1:
    SECONDLength=len(licenceSection1SECOND)-1
    
    RandomRemove= random.randint(0,SECONDLength)
    licenceSection1SECOND.pop(RandomRemove)
licenceSectionLETTER1="".join(licenceSection1FIRST)
licenceSectionLETTER2="".join(licenceSection1SECOND)
licenceSection1=licenceSectionLETTER1+licenceSectionLETTER2

#Random letter selection for third section if user choice is "1"------------------------------------------------
licenceSection3=["A","B","C","D","E","F","G","H","J","K","L","M","N","O","P","R","S","V","W"]
Section3Length=len(licenceSection3)
while Section3Length !=3:#for 3 letters remaining
    Section3Length=len(licenceSection3)-1
    RandomRemove= random.randint(0,Section3Length)
    licenceSection3.pop(RandomRemove)
licenceSection3="".join(licenceSection3)


#menu
menu=True
while menu:
    userchoice=input("""(1)Do you want to generate a valid licence plate
(2)Check your licence's validity
(3)Check your car's age
(4)Automated Testing
(5)to quit the program
Enter your choice:""")
#-------------------------------------------------------------------------------------------------------------
    if userchoice == "1":#randomly generated licence plate
        time.sleep(1)
        licenceSection2=int(datetime.now().strftime("%y"))#current year
        licenceSection2Check(Months,currentMonth,licenceSection2,userchoice)
        user_licence_plate = licenceSection1+str(licenceSection2)+licenceSection3
        finalCheck(user_licence_plate,strip_spaces,REQ_CHARS,VALID_FIRST_LETTERS,INVALID_LETTERS,REGIONS,validEnd,FIRST_LETTER)
#-------------------------------------------------------------------------------------------------------------       
    elif userchoice == "2":#own licence validation, doesnt need licencesection1 and 3 because it isnt random.
        licenceSection3Valid=True
        licenceSection3List=["A","B","C","D","E","F","G","H","J","K","L","M","N","O","P","R","S","V","W"]

        licenceSection1=input("Enter the first two letters of your licence plate:").upper()
        if  not licenceSection1.isalpha():
            while  not licenceSection1.isalpha():
                licenceSection1=input("That is not valid as it contains a character which is not a letter please enter again:").upper()
                if licenceSection1.isalpha():
                    break
        licenceSection2= int(input("Enter your licence plate numbers:"))
        licenceSection3=input("Enter the last 3 letters of your licence plate:").upper()
        
    #while loop to make sure last section is 3 letters
        while len(licenceSection3) !=3:
            licenceSection3=input("Enter the last 3 letters of your licence plate").upper()
        for letter in licenceSection3:#checks if last letters are invalid
            if letter not in licenceSection3List:
                print(f"{letter} is invalid meaning {licenceSection3} is invalid")
    #prints out a user licence plate with information given so rest of program works
        time.sleep(1)
        user_licence_plate=licenceSection1+licenceSection2Check(Months,currentMonth,licenceSection2,userchoice)+licenceSection3
        finalCheck(user_licence_plate,strip_spaces,REQ_CHARS,VALID_FIRST_LETTERS,INVALID_LETTERS,REGIONS,validEnd,FIRST_LETTER)
#-------------------------------------------------------------------------------------------------------------          
    elif userchoice== "3":#check car age
        licenceSection2= input("Enter your licence plate numbers:")
        if not licenceSection2.isnumeric():
            while not licenceSection2.isnumeric():
                licenceSection2= input("Enter your licence plate numbers again:")
        licenceSection2=int(licenceSection2)
        licenceSection2Check(Months,currentMonth,licenceSection2,userchoice)
#-------------------------------------------------------------------------------------------------------------       
    elif userchoice== "4":#makes a file of all the invalid test
        invalidlist=[]
        for i in test_cases_List:
            user_licence_plate=i
            try:
                finalCheck(user_licence_plate,strip_spaces,REQ_CHARS,VALID_FIRST_LETTERS,INVALID_LETTERS,REGIONS,validEnd,FIRST_LETTER)
            except:
                invalidlist.append(user_licence_plate)
        invalidTests=open("invalidtests.txt", "w")
        invalidTests.write(f"{invalidlist} this is all of the licence plates that are either invalid or erroneous")
        invalidTests.close()
        invalidTests=open("invalidtests.txt","r")
        invalidTests.close()
#-------------------------------------------------------------------------------------------------------------
    elif userchoice== "5":#quit program
        print("Thank you for using me. Exiting program...")
        break
    else:#if input is not any of the choices
        print("Invalid input")
#-------------------------------------------------------------------------------------------------------------
    ReopenMenu=input("Do you want to select an option again?(Y/N)").upper()
    if  reopenMenu(ReopenMenu,menu) == False:
        break