# def number_to_string(argument):
from Authentication import Authentication
from hash import hashing
def Registration():
    name = input("name here : ")
    email = input("email here : ")
    password = input("password here : ")
    password = hashing(password)
    Authentication.Register(username=name,email=email,password=password)


def Login():
    username = input("username please : ")
    passw = input("password : ")
    print(Authentication.Login(username=username,userpassword=passw))


if "__main__" == __name__:
    while(True):
        print("""
        1. Registration 
        2. Login 
        3. Add items (for managers) 
        4. Update stock (for cashier or manager) 
        5. Generate reports (sales/custom) 
        6. Display inventory 
        7. Remove items (for managers) 
        8. Manage cart (add/remove items, generate bill) 
        9. Logout 
        10. Exit 
        """)
        ele = int(input())

        match ele:
            case 1:
                Registration()
                continue
            case 2:
                Login()
                continue
            case 3:
                print("zero")
                continue
            case 4:
                print("one")
                continue
            case 5:
                print("two")
                continue
            case 6:
                print("zero")
                continue
            case 7:
                print("one")
                continue
            case 8:
                print("two")
                continue
            case 9:
                print("zero")
                continue
            case 10:
                break

            case default:
                print("Please select valid value from below : \n")