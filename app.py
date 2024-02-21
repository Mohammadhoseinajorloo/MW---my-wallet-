from user import User
from arg_parser import args

def rejester():
    db = open("user.txt", "r")
    username = args.Rejester[0]
    password = args.Rejester[1]
    mail = args.Rejester[2]
    user = User(username, password, mail)
    db = open("user.txt", "a")
    db.write(username + "," + password + "," +  mail + "\n")
    print("Success!")

def login():
    pass

if __name__ == "__main__":
    rejester()
