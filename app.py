from user import User
from arg_parser import args

def rejester():
    db = open("user.txt", "r")
    username = args.Rejester[0]
    password = args.Rejester[1]
    d = []
    f = []
    for i in db:
        user , pas = i.split(",")
        pas = pas.strip()
        d.append(user)
        f.append(pas)
    data = dict(zip(d, f))

    if len(password)<6:
        print("Password too short, restart!")
        pass

    elif username in d:
        print("username exists")

    else:
        user = User(username, password)
        db = open("user.txt", "a")
        db.write(username + "," + password +"\n")
        print("Success!")

def login():
    username = args.Login[0]
    password = args.Login[1]

    if not len(username or password)<1:
        db = open("user.txt", "r")
        d = []
        f = []
        for i in db:
            user , pas = i.split(",")
            pas = pas.strip()
            d.append(user)
            f.append(pas)
        data = dict(zip(d, f))
        
        try:
            if data[username]:
                try:
                    if password == data[username]:
                        print("Login Success!")
                        print("Hi,", username)
                    else:
                        print("Password or username inccorect!")
                except:
                    print("Password or username inccorect!")
            else:
                print("username dos`t exists")
        except:
            print("Login error!")
    else:
        print("please enter username and password!")

        


if __name__ == "__main__":
    login()
