FILEPATH="todos.txt"
def get_todos(filepath=FILEPATH): #argument filepath
    with open(filepath, 'r') as file_local:  #argument filepath
        todos_local = file_local.readlines()
        return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Welcome to the TO-do list app:)")
    print(get_todos())