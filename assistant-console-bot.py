def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: 'add' command needs correct argument count."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: 'change' command needs correct argument count."
    name, phone = args
    if name not in contacts:
        return f"Error: Contact '{name}' not found."
    contacts[name] = phone
    return f"Contact '{name}' updated."

def get_phone(args, contacts):
    if len(args) != 1:
        return "Error: 'phone' command needs correct argument count."
    name = args[0]
    return contacts.get(name, f"Error: Contact '{name}' not found.")

def list_all_contacts(contacts):
    if not contacts:
        return "No contacts saved."
    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command:")
        command, args =parse_input(user_input)

        if command in ["close","exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can i help you?")
        elif command == "add":
             print(add_contact(args, contacts))
        elif command == "change":
             print(change_contact(args, contacts))    
        elif command == "phone":
             print(get_phone(args, contacts))
        elif command == "all":
             print(list_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
    