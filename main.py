def get_todos(filepath):
    # read file
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    """writing file to the todolist"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


user_prompt = "Enter a todo: "

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        # Opens, Reads and Closes 'todos.txt' file
        todos = get_todos('todos.txt')

        todos.append(todo + '\n')

        # Opens, Writes and Closes 'todos.txt' file
        write_todos('todos.txt', todos)

    elif user_action.startswith('show'):

        todos = get_todos('todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos('todos.txt')

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos('todos.txt', todos)
        except ValueError:
            print("Command is not Valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos('todos.txt')

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos('todos.txt', todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            # Action: if User enters value beyond the capacity of the todo list
            print('There is no item with that error')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")

print('bye')
