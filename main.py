import mysql.connector as a
con=a.connect(host='localhost',user='root',passwd='Gpass@600271',database='LMS_APP')

def addbook():
    bcode=input("Enter Book Code:")
    bname=input("Enter Book Name:")
    bauthor=input("Enter Author of the Book:")
    bsubject=input("Enter subject of the Book:")
    Btotal=int(input("Enter Number of Books:"))
    Bcavail=int(input("Enter Number of Avail books:"))
    data=(bcode,bname,bauthor,bsubject,Btotal,Bcavail)
    sql='insert into book_mstr values(%s,%s,%s,%s,%s,%s);'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("\n\nBook Details Added Successfully.....\n\n")
    wait=input('\n\nPress Enter To Continue.....\n\n')
    main_menu()


def lendbook():
    bcod=input("Enter Book Code: ")
    a="select Bcurr_avail from book_mstr where bcode=%s;"
    data=(bcod,)
    c=con.cursor() 
    c.execute(a,data) 
    myresult=c.fetchone()
    t=myresult[0]+0
    print('Available # of Requested Books :',t)
    if( t > 0):   
        print('Requested Book Can Be Lended')
        bco=input("Enter Book Code: ")
        sregn=int(input("Enter Student Reg No.: "))
        sname=input("Enter Student Name: ") 
        ld=input("Enter Lending Date: ")
        a="insert into lend_details(bcode,sreg_no,sname,lend_date) values(%s,%s,%s,%s);" 
        data=(bco,sregn,sname,ld)
        c=con.cursor() 
        c.execute(a,data)
        con.commit()
        print("\n\n\n\nBook Lended successfully to: ",sname)
        wait = input("\n\n\nPress enter to continue.....\n\n\n\n\n\n") 
        bookupd(bco,-1)
        main_menu()
    else:
        print('All Books Already Lended')

def rtnbook():
    bco=input("Enter Book Code: ") 
    r=int(input("Enter Student Reg No.: "))
    d=input("Enter Return Date: ")
    a="select count(*) from lend_details where bcode=%s and sreg_no=%s;" 
    data=(bco,r)
    c=con.cursor() 
    c.execute(a,data)
    myresult=c.fetchone()    
    t=myresult[0]+0
    print('Books Available in Lending Table')
    if( t > 0):
        sql="update lend_details set return_date=%s where bcode=%s and sreg_no=%s;"
        ud=(d,bco,r)
        c.execute(sql,ud)
        con.commit()
        print('Return Book Updated Successfully......')
        wait = input("\n\n\nPress enter to continue.....\n\n\n\n\n\n")
        bookupd(bco,1)
    else:
        print('Books Not Available in Lending Table')
     

def bookupd(bco,u):
    a="select Bcurr_avail from book_mstr where bcode=%s;" 
    data=(bco,) 
    c=con.cursor() 
    c.execute(a,data)
    myresult=c.fetchone()
    t=myresult[0]+u
    sql="update book_mstr set Bcurr_avail=%s where bcode=%s;" 
    d=(t,bco)
    c.execute(sql,d) 
    con.commit()
    wait = input('\n\n\nPress enter to continue.....\n\n\n\n\n\n')
    main_menu()  

def avilsts():
    a="select * from book_mstr;" 
    c=con.cursor() 
    c.execute(a) 
    myresult=c.fetchall() 
    for i in myresult:
        print("Book Code: ",i[0]) 
        print("Book Name: ",i[1])
        print("Author: ",i[2]) 
        print("Subject:",i[3])
        print("Total No. Of Books:",i[4]) 
        print("Current No. Of Avail Books:",i[5])
        print("\n\n")
    bookstts()  

def lendsts(): 
    a="select * from lend_details;" 
    c=con.cursor() 
    c.execute(a) 
    myresult=c.fetchall() 
    for i in myresult: 
        print(myresult)
    bookstts()
        
def bookstts():
        print("""\n--------------------------------------------------------------------\n                B O O K  S T A T U S
--------------------------------------------------------------------
                    1. AVAILABLE BOOKS
                    2. LENDED BOOKS
                    3. BACK TO MAIN MENU
            \n\n\n""")
        opt=input("Enter The Selection...")
        print('\n\n\n\n\n\n\n')
        if(opt =='1'):
            avilsts()
        elif(opt =='2'):
            lendsts()
        elif(opt =='3'):
            main_menu()
        else:
            print('Kindly Enter the Selection Properly...\n\n\n\n')
           

def main_menu():
    from datetime import datetime
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("\n               Current Date & Time :", dt_string)
    print("""--------------------------------------------------------------------\n           L I B R A R Y  M A N A G E M E N T  S Y S T E M
                        V E L A M M A L -- RT - WING
                                
--------------------------------------------------------------------
		
                        1. ADD NEW BOOK
                        2. LENDING BOOK
                        3. RETURN OF BOOK
                        4. BOOKS STATUS
                        5. EXIT MENU
                    """)
    option=input('Enter the Menu Selection....')
    print("\n\n\n\n\n\n\n")
    if(option =='1'):
        addbook()
    elif(option =='2'):
        lendbook()
    elif(option =='3'):
        rtnbook()
    elif(option =='4'):
        bookstts()
    elif(option =='5'):
        print('\n\n\n\n\n\n THANKS FOR USING THE SYSTEM.....\n\n\n')
    else:
        print('Retry the Option..............\n\n\n\n')
        main_menu()
    
main_menu()
