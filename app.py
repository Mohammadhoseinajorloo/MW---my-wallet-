from user import User
from arg_parser import args


if __name__ == "__main__":
    mohammad = User(args.login[0], args.login[1], args.login[2])
    print(mohammad.info())
