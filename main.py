user_prompt = "Enter a todo: "

todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            # Opens, Reads and Closes 'todos.txt' file
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            # Opens, Writes and Closes 'todos.txt' file
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show' | 'display':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            new_todos = []

            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)

            for index, item in enumerate(new_todos):
                item = item.strip('\n')
                row = f"{index + 1} - {item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit "))
            number = number - 1
            new_todo = input("Enter new todo:  ")
            todos[number] = new_todo

        case 'complete':
            number = int(input("Number of the todo to complete:: "))
            todos.pop(number)

        case 'exit':
            break
        case whatever:
            print("Hey, you've entered an unknown command")

print('bye')
