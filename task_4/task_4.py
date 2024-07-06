from utils import *


def main():
    phone_book = {}
    try:
        while True:
            user_input = input('Enter command: ').strip().lower()
            if user_input:
                command, *args = parse_input(user_input)

                # Finish
                if command in ['exit', 'close']:
                    bot_answer('Goodbye!')
                    break

                # Greeting
                elif command in ['hi', 'hello']:
                    bot_answer('Hello! How can I help you?')

                # Add contact
                elif command == 'add':
                    if len(args) != 2:
                        bot_answer('If you want to add a contact you should ask for "add <name> <number>"')
                    else:
                        add_contact(phone_book, *args)

                # Change contact
                elif command == 'change':
                    if len(args) != 2:
                        bot_answer('If you want to change a contact you should ask for "change <name> <number>"')
                    else:
                        change_contact(phone_book, *args)

                # Show contact
                elif command == 'phone':
                    if len(args) != 1:
                        bot_answer('If you want to see the number of a contact you must ask for "phone <name>"')
                    else:
                        show_contact(phone_book, *args)

                # Show all contact
                elif command == 'all':
                    if len(phone_book) == 0:
                        bot_answer('Your phone book is empty')
                    else:
                        show_all(phone_book)

                # Show info
                elif command == 'info':
                    show_info()

                # Invalid command
                else:
                    bot_answer('I don\'t know how to handle this command.')

    except KeyboardInterrupt:
        bot_answer('Oops.. Something went wrong..')


if __name__ == '__main__':
    main()
