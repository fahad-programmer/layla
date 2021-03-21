import os 

while True:
    query = input("Enter the folder name: ")
    if "download" in query:
        path = 'C:/Users/Anonymous/Downloads'
    elif "c" in query:
        path = 'C:/'
    elif "d" in query:
        path = 'D:/'
    elif "e" in query:
        path = 'E:/'
    else:
        print("No path")
        pass
    
    while True:
        my_list = os.listdir(path)
        print(my_list)

        path = os.path.realpath(path)
        os.startfile(path)
        path = "" + path
        