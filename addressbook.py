# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 02:52:59 2021

@author: usetr2
"""
#address book, covid data, 0X, calculator
import pickle
import os
class addressbook(object):
    def __init__(s):
        s.sno=1
        s.name="abcd"
        s.ph=9999999999
        s.add="Ashok Vihar"
    def create(s):  #function to get data from user
        name=input("Enter the name of the person: ")
        s.name=name.capitalize()
        type=input("Enter address of the person: ")
        s.add=type.upper()
        s.ph=input("Enter phone number: ")
    def show(s):    #function to show data on screen
        print("\nSerial No. :", s.sno)
        print("\nName: ", s.name)
        print("\nAddress", s.add)
        print("\nPhone Number: ", s.ph)
    def modify(s):          #function to get new data from user
        print("\nSerial No. : ", s.sno)
        s.name=input("Enter the name of: ")
        address=input("Enter address of the person: ")
        s.add=address.upper()
        s.ph=input("Enter phone number: ")
    def report(s):          #function to show data in tabular format
        print("%-10s"%s.sno,"%-20s"%s.name,"%-10s"%s.add,"%-6s"%s.ph)
    def retsno(s):         #function to return account number
        return int(s.sno)
    def retph(s):      #function to return balance amount 
        return s.ph
    def retn(s):
        return s.name
    def retadd(s):         #function to return type of account
        return s.add
def gen_sno():
    s=addressbook()
    sno=s.sno
    inFile=open("address.dat","rb")
    try:
        while True:
            s=pickle.load(inFile)
            if (sno<s.retsno()):
                sno=s.retsno
    except EOFError:
        inFile.close()
    return int(sno)+1
def write():
   ac=addressbook()
   inFile=open("address.dat","ab")
   ac.sno=gen_sno()
   ac.create()
   pickle.dump(ac,inFile)
   print("\n\nYour data has been added")
   print("the serial number is:", ac.retsno())
   inFile.close()
def display_sp(n):
    flag=0
    try:
        inFile=open("address.dat","rb")
        print("\nADDRESS DETAILS\n")
        while True:
            ac=pickle.load(inFile)
            if ac.retsno==n:
                ac.show()
                flag=1        
    except EOFError:
        inFile.close
        if flag==0:
            print("\n\nEntry does not exist")
    except IOError:
        print("File could not be open !! Press any Key...")
def display_name(name):
    flag=0
    try:
        inFile=open("address.dat","rb")
        print("\nADDRESS DETAILS\n")
        while True:
            ac=pickle.load(inFile)
            if ac.retn==name:
                ac.show()
                flag=1        
    except EOFError:
        inFile.close
        if flag==0:
            print("\n\nEntry does not exist")
    except IOError:
        print("File could not be open !! Press any Key...")
def display_add(add):
    flag=0
    try:
        inFile=open("address.dat","rb")
        print("\nADDRESS DETAILS\n")
        while True:
            ac=pickle.load(inFile)
            if ac.retadd==add:
                ac.show()
                flag=1        
    except EOFError:
        inFile.close
        if flag==0:
            print("\n\nEntry does not exist")
    except IOError:
        print("File could not be open !! Press any Key...")
def display_ph(ph):
    flag=0
    try:
        inFile=open("address.dat","rb")
        print("\nADDRESS DETAILS\n")
        while True:
            ac=pickle.load(inFile)
            if ac.retph==ph:
                ac.show()
                flag=1        
    except EOFError:
        inFile.close
        if flag==0:
            print("\n\nEntry does not exist")
    except IOError:
        print("File could not be open !! Press any Key...")
def modify(n):
    found=0
    try:
        inFile=open("address.dat","rb")
        outFile=open("temp.dat","wb")
        while True:
            ac=pickle.load(inFile)
            if ac.retsno()==n:
                print(30*"-")
                ac.show()
                print(30*"-")
                print("\n\nEnter The New Details of Address")
                ac.modify()
                pickle.dump(ac,outFile)
                print("\n\n\tRecord Updated")
                found=1
            else:
                pickle.dump(ac,outFile)
             
    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print("\n\nRecord Not Found")

    except IOError:
        print("File could not be open !! Press any Key...")

    os.remove("address.dat")
    os.rename("temp.dat","address.dat")
def delete(n):
    found=0
    try:
        inFile=open("address.dat","rb")
        outFile=open("temp.dat","wb")
        while True:
            ac=pickle.load(inFile)
            if ac.retsno()==n:
                found=1
                print("\n\n\tRecord Deleted ..")
            else:
                pickle.dump(ac,outFile)
    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print("\n\nRecord Not Found")
    except IOError:
        print("File could not be open !! Press any Key...")
    os.remove("address.dat")
    os.rename("temp.dat","address.dat")
def display_all():
    print("\n\n\tADDRESS LIST\n\n")
    print(60*"=")
    print("%-10s"%"S.No.","%-10s"%"Name","%-20s"%"Address","%-6s"%"Phone Number")
    print(60*"=","\n")
    try:
        inFile=open("address.dat","rb")
        while True:
            ac=pickle.load(inFile)
            ac.report()
    except EOFError:
        inFile.close()
    except IOError:
        print("File could not be open !! Press any Key...")
def intro():
    print("\n\n\tADDRESS MANAGEMENT")
    print("\n\n\nMADE BY : Dev Bhardwaj")
intro()
while True:
    print(3*"\n",60*"=")
    print( """MAIN MENU
    1. New Entry
    2. Address Enquiry
    3. All Address List
    4. Delete An Entry
    5. Modify An Entry
    6. Get by name
    7. Get by address
    8. Get by phone number
    9. Exit
    """)
    ch=int(input("Enter Your Choice(1~9): "))
    if ch==1:
        write()
    elif ch==2:
        num=input("\n\nEnter Serial Number: ")
        display_sp(num)
    elif ch==3:
        display_all()
    elif ch==4:
        num=input("\n\nEnter Serial Number: ")
        delete_account(num)
    elif ch==5:
        num=input("\n\nEnter Serial Number: ")
        modify_account(num)
    elif ch==6:
        name=input("\n\nEnter Name: ")
        display_name(name)
    elif ch==7:
        add=input("\n\nEnter address: ")
        display_add(add)
    elif ch==8:
        ph=input("\n\nEnter Phone Number: ")
        display_ph(ph)
    elif ch==9:
        break
    else:
        print("Input correct choice...(1-9)")
print("\n\n\n\n\nTHANK YOU\n\n")