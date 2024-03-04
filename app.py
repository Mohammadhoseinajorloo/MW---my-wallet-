from src.user import User
import pytermgui as ptg


def rejester(db_path):
    """
    """
    db = open(db_path, "r")

    username = input("Create Username : ")
    password = input("Create Password : ")
    password_confirm = input("Confirm Password : ")

    username_list = []
    password_list = []
    for i in db:
        usernme, password = i.split(",")
        password = password.strip()
        username_list.append(username)
        password_list.append(password)


    if password != password_confirm:
        print("The password do not mach")
        rejester(db_path)


    elif len(password)<8:
        print("The password is short")
        rejester(db_path)


    elif username in username_list:
        print("There is username")
        rejester(db_path)


    else:
        user = User(username, password) 
        db = open(db_path, "a")
        db.write(username+","+password+"\n")
        print("Hi, ", username)


if __name__ == "__main__":

    db_path = "database/user.txt"

    CONFIG = """
    config:
        InputField:
            styles:
                prompt: dim italic
                cursor: '@72'
        Label:
            styles:
                value: dim bold

        Window:
            styles:
                border: '60'
                corner: '60'

        Container:
            styles:
                border: '96'
                corner: '96'
    """

    with ptg.YamlLoader() as loader:
        loader.load(CONFIG)


    with ptg.WindowManager() as manager:

        # TODO: find icon and gretting and about for app
        icon = ptg.Container("💰", box="EMPTY")
        gretting = "gretting massage"
        about = ptg.Label("about(title & massage)", position=1)

        buttons  = (["SingUp", lambda *_: rejester(db_path)], ["Login", lambda *_: rejester(db_path)], ["Exit", lambda *_: manager.stop()])

        container = ptg.Container(about)

        window = ptg.Window(icon, gretting, container, buttons)
        window.set_title("[210 bold]my wallet")
        window.center()

        window.select(0)

        manager.add(window)
