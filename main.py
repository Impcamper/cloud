import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('C:\\Users\\impca\\Documents\\fall projects\\key.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()


#get user or new user
print("Welcome to the tracker!")
userdata=input("Are you an existing user or new user?\nNew for new user, Username for existing user.")

if(userdata.lower()=="new"):
    #user setup
    username=input("Enter your username")
    ref=db.collection("users").document(username.lower())
    task=input("Enter the daily task")
    ref.set({"task":task})
    ref.collection("checklist")#I don't think this is needed
else:
    ref=db.collection("users").document(userdata.lower())#simple get existing user

#menue
menue=-1
while(menue!=0):
    print("1 to register day\n2 for info\n0 to quit.")
    menue=int(input())
    if(menue==0):#quiting
        break
    elif(menue==1):#entering a day into the list
        date=input("enter the day mm/dd/yyyy\n")
        ref.collection("checklist").document("Daily").set({date:"done"}, merge=True)
        print("-----")
    elif(menue==2):#print the list
        for doc in ref.collection("checklist").stream():
            print(doc.to_dict())
            print("-----")
