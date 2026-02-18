# To do list
def todo_list():
    list = []

    while True:
        print("\n --Menu--")
        print("1. Add work")
        print("2. View list")
        print("3. Remove work")
        print("4. Reset list")
        print("5. Exit")

        option = input ("\n Choose: ")
        if option == "1":
            viec = input ("\n Nhập việc cần thêm: ")
            list.append (viec)
            print("\n Work added successfully")

        elif option == "2":
            if not list:
                print ("\n List unavailable")
            else:
                for i, viec in enumerate(list, start=1):
                    print(f"{i}. {viec}")

        elif option == "3":
            if not list:
                print("\n No work to remove")
                continue
            for i, viec in enumerate(list, start=1):
                    print(f"\n {i}. {viec}")
            try:
                number = int(input("\n The sequence number of the work to be removed: "))
                if 1 <= number <= len(list):
                    remove=list.pop(number -1)
                    print(f"\n Removed {remove} successfully")
                else:
                    print("\n Number not valid")
            except ValueError:
                print("\n Please enter valid number")

        elif option == "4":
            if not list:
                print("\n Empty list")
            else:
                Decision = input("Are you sure? Y/N: ")
                if Decision == "Y":
                    list.clear()
                    print ("\n List RESETED")
                elif Decision == "N":
                    continue
                else:
                    print("\n Unvalid answer")
                    
        elif option == "5":
            Choice=input("\n Are you sure? Y/N: ")
            if Choice == "Y":
                break
            elif Choice == "N":
                continue
            else:
                print ("\n Unvalid answer")
                continue
        

        else:
            print("\n Unvalid option")

todo_list()
