#get the username from a prompt
username=raw_input("Login:>>")

#list of allowed users
user1 = 'Jack'
user2 = 'Navpreet'
user3 = 'Atlas'
user4 = 'Bowser'

#control that the user belongs to the list of allowed users
if username == user1:
    print "Access Granted"
elif username == user2:
    print "Welcome to the System"
elif username == user3:
    print "What is up Big Pup, Doing big things??"
elif username == user4:
    print "What is up my Sunshine Doggy!! Whose a good boy!"
else:
    print "Access Denied"
    