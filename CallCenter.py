import datetime

ID = 0

class CallCenter(object):
    calls = []
    def __init__(self ):
        self.queue = len(self.calls)
    
    def add(self, call):
        self.calls.append(call)
        return self

    def remove(self):
        self.calls.pop(0)
    
    def removePhone(self, phone):
        for i in self.calls:
            if i.getPhoneNumber() == phone:
                self.calls.remove(i)

    
    def info(self):
        print("================================================")
        print("Length of list: ", len(self.calls))
        for i in self.calls:
            print("--------------------------------------------------")
            i.display()
        print("================================================")
        return self

class Call(object):
    def __init__(self, callerName, callerPhoneNumber, reasonForCall):
        global ID 
        ID += 1
        self.id = ID
        self.callerName = callerName
        self.callerPhoneNumber = callerPhoneNumber
        self.timeOfCall = datetime.datetime.now().strftime("%H:%M")
        self.reasonForCall = reasonForCall


    def display(self):
        print("ID: ",self.id)
        print("Caller Name: ", self.callerName)
        print("Caller Phone Number: ", self.callerPhoneNumber)
        print("Time of Call: ", self.timeOfCall)
        print("Reason for Calling: ", self.reasonForCall)
        return self
    
    def getPhoneNumber(self):
        return self.callerPhoneNumber


callCenter = CallCenter()

def addCaller():
    name = input('What`s your name: ')
    phone = input('What`s your number: ')
    reason = input("Reason of calling: ")
    call = Call(name, phone, reason)
    callCenter.add(call) 

while True:
    print()
    print("1 add new call")
    print("2 show callers")
    print("3 delete first caller")
    print("4 delete by phone number")
    print("Q for exit ")
    menu = input("Menue number: ")
    if menu == '1':
        addCaller()
    elif menu == '2':
        callCenter.info()
    elif menu == '3':
        callCenter.remove()
    elif menu == '4':
        phone = input("What phone you want ot remove: ")
        callCenter.removePhone(phone)
    elif menu == 'Q':
        break
# call.display()
# callCenter = CallCenter(call)
# callCenter.info()