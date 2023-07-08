from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("it is now")

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
        write_todos(todos)

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

            write_todos(todos)
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

            write_todos(todos)

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
