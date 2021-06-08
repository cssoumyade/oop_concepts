class X():
    n_objects = 0

    def __init__(self, name):
        X.n_objects += 1 
        self.name = name
        print("Class name : {}".format(self.__class__.__name__))
        print("Object name : {}".format(self.name))
        self.exe_count = 0
        self.config_ = {}

    def execute(self, dict_):
        self.config_ = dict_
        self.exe_count += 1
        print("Class name : {}".format(self.__class__.__name__))
        print("Object name : {}".format(self.name)) 
        print("Arguments : ")
        for k,v in self.config_.items():
            print("\t* {} = {}".format(k,v))

    def __del__(self):
        X.n_objects -=1

    def shutdown(self):
        print("Class name : {}".format(self.__class__.__name__))
        print("Object name : {}".format(self.name))

class A(X):
    pass
class B(X):
    pass
class C(X):
    pass


def display_menu():
    print("------------------------------")
    print("|          M E N U           |")
    print("|----------------------------|")
    print("|                            |")
    print("|    1. Create an object     |")
    print("|    2. Delete an object     |")
    print("|    3. Execute an object    |")
    print("|    4. Quit                 |")
    print("------------------------------")

def find(objects, class_name, name):
    for i, obj in enumerate(objects):
        if (obj.__class__.__name__ == class_name) and (obj.name == name):
            return i
    return None

def create_object(objects):
    print("There are three classes A, B, C of which instances can be created")
    menu = str(input("Please enter a class choice : ")).upper()
    name = str(input("Enter instance name : "))
    present = find(objects, menu, name)
    if present is not None:
        print("Can't create, object with name \"{}\" from class \"{}\" is already present".format(name, menu.upper()))
    else:
        flag = len(menu)==1
        if menu == 'A' and flag:
            temp = A(name)
        elif menu == 'B' and flag:
            temp = B(name)
        elif menu == 'C' and flag:
            temp = C(name)
            raise ValueError("Invalid Choice. Choice must be from [A/B/C]")
        objects.append(temp)
    return objects

def del_object(objects):
    print("From which class you want to delete an object (A/B/C)")
    menu = str(input("Please enter a choice : ")).upper()
    flag = len(menu)==1
    found = 0
    if flag:
        name = str(input("Enter instance name : "))
        i = find(objects, menu, name)
        if i is not None:
            temp = objects[i]
            objects.remove(temp)
            del temp
            print("Object deleted")
        else:
            print("No object found")
    return objects

def input_params():
    n_params = int(input("Enter number of parameters to be specified : "))
    dict_ = {}
    for i in range(n_params):
        p_name, value = input("Enter parmater {} [name value]".format(i+1)).split()
        dict_[p_name] = value
    
    return dict_

def exe_object(objects):
    print("From which class you want to execute an object (A/B/C)")
    menu = str(input("Please enter a choice : ")).upper()
    flag = len(menu)==1
    if flag:
        name = str(input("Enter instance name : "))
        i = find(objects, menu, name)
        if i is not None:
            temp = objects[i]
            c = 1
            if temp.exe_count > 0:
                temp_dict = temp.config_
                print("Do you want update [0] or overwrite [1] parameters?")
                c = int(input("Enter a choice (0/1)... "))
            dict_ = input_params()
            if c == 0:
                dict_.update(temp_dict)       
            temp.execute(dict_)

        else:
            print("No object found")

objects = []

def main():
    while(True):
        display_menu()
        menu = int(input("Please enter a choice : "))
        if menu == 1:
            objects = create_object(objects)
        elif menu == 2:
            objects = del_object(objects)
        elif menu == 3:
            exe_object(objects)
        elif menu == 4:
            break
        else:
            raise ValueError("Invalid Choice. Please enter valid option from (1/2/3/4).")