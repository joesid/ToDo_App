user_prompt = "Enter a todo: "

todos = []

while True:
    user_action = input("Type add or show or edit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show' | 'display':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
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
