
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
                    add_contact(phone_book, *args)

                # Change contact
                elif command == 'change':
                    change_contact(phone_book, *args)

                # Show contact
                elif command == 'phone':
                    show_contact(phone_book, *args)

                # Show all contact
                elif command == 'all':
                    show_all(phone_book)

                elif command == 'info':
                    show_info()

                # Invalid command
                else:
                    bot_answer('I don\'t know how to handle this command.')
    except KeyboardInterrupt:
        bot_answer('Oops.. Something went wrong..')


if __name__ == '__main__':
    main()
