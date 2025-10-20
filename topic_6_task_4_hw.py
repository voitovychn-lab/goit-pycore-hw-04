def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except ValueError:
        return "", []


def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Usage: add [name] [phone]"
    
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Usage: change [name] [new_phone]"
    
    name, phone = args
    if name not in contacts:
        return "Contact not found."
        
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command. Usage: phone [name]"
        
    name = args[0]
    if name not in contacts:
        return "Contact not found."
        
    return contacts[name]


def show_all(contacts):
    if not contacts:
        return "No contacts saved."
        
    output = "All contacts:\n"
    for name, phone in contacts.items():
        output += f"{name}: {phone}\n"
    return output.strip()


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
            
        elif command == "add":
            print(add_contact(args, contacts))
            
        elif command == "change":
            print(change_contact(args, contacts))
            
        elif command == "phone":
            print(show_phone(args, contacts))
            
        elif command == "all":
            print(show_all(contacts))
            
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()