import time;
print("\n\nWELCOME TO BANK OF MONEY")
time.sleep(3)
print("INSERT YOUR CARD")
time.sleep(2)
print("CHECKING INSERTED CARD...")
time.sleep(1)
print("DATA ENQUIRING...")
time.sleep(3)
pin=int(input("ENTER YOUR PIN NUMBER \n"))

cash=75000

if(pin==4243):
    print("1 - DEPOSIT")
    print("2 - ENQUIRE BALANCE")
    print("3 - WITHDRAW")
    print("4 - CHANGE PIN")
    opt=int(input("\nPLEASE CHOOSE TRANSACTION : \n\t"))
    if(opt==1):
        print("PUT YOUR CASH ON CASHBOARD")
        print("\n(Only cash allow as ruppees 2000, 500, 100)\n")
        time.sleep(2)
        dpt=int(input("1 - CONFIRM \n2 - CANCEL\n \n"))
        if(dpt==1):
            print("\nTRANSACTION PROCEEDING...\nPLEASE WAIT")
            time.sleep(3)
            print("DEPOSITED CASH DEBITED TO YOUR BANK")
            time.sleep(2)
        else:
            print("\nCANCELED\n")
    elif(opt==2):
        print("YOUR ACCOUNT HAS RS.75000 ")
    elif(opt==3):
        amount=int(input("ENTER YOUR AMOUNT : "))
        print("\nPLEASE WAIT TRANSCATION PROCEEDING...")
        time.sleep(3)
        print("\nTAKE OUT CASH FROM CASHBOARD")
        time.sleep(2)
        cash=int(cash-amount)
        print("YOUR CASH BALANCE IS "+str(cash))
    elif(opt==4):
        changepin=int(input("ENTER YOUR NEW 4 DIGIT PIN NUMBER : "))
        pinopt=int(input("1 - CONFIRM\t 2 - CANCEL \n"))
        if(pinopt==1):
            print("\nPIN CHANGED SUCCESSFULLY")
            time.sleep(2)
        else:
            print("CANCELED")
            time.sleep(1)
    else:
        print("PLEASE TAKE YOUR CARD ")
        time.sleep(2)
        
else:
    print("WRONG PIN")
    
print("REMOVE YOUR CARD ")
print("THANKS FOR USE ME")
time.sleep(1)
print("\nBANK OF MONEY \n\n")
