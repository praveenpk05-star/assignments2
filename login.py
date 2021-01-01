#Develop a Login app with Username and Password.
username = "praveenkumar";
password = "1234"

trials = 3

while(trials):
    uname = input("Enter user name : ")
    Pass = input("Enter password : ")
    if uname == username and Pass == password :
        print("Welcome "+ username)
        trials = 0
    else:
        trials = trials - 1


