import string
import random


def get_input():
    """
    Asks the user for input in how many characters 
    the random password should get.
    """

    while True:
        print('Please enter the length your password should be.')
        print('Your input should only consist of 1 number between 1 and 8.\n')
    
        enter_int = input('Enter your number here: ')
        
        if validate_input(enter_int):
            print(f'Your password will be {enter_int} digit(s) long.\n')
            break
    
    return int(enter_int)


def validate_input(number):
    """
    x
    """
    try:
        if len(number) != 1:
            raise ValueError(
                f'{number}.\n' 
                'Only 1 number is allowed!'
            )

        elif int(number) < 1 or int(number) > 8:
            raise ValueError(
                f'{number}.\n' 
                'Only a number between 1 and 8 is allowed!'
            )
        
    except ValueError as e:
        print(f'You entered: {e}. Please try again.\n')
        return False 
    
    return True


def generate_password(length):
    """
    x
    """
    print('Generating your password...')
    characters = string.ascii_letters + string.digits
    gen_pass = ''.join(random.choice(characters) for x in range(int(length)))
    print(gen_pass, '\n')
    
    
def question_continue():
    """
    x
    """
    enter_continue = input("Type 'yes' to conintue or 'no' to close: ")
    try:
        if enter_continue == 'yes':
            print(f'You typed {enter_continue}. Please try again.\n')
            return main_flow()

        elif enter_continue == 'no':
            print(f'You typed {enter_continue}. Goodbye!\n')
            quit()
        
        elif enter_continue != 'yes' or 'no':
            raise ValueError(f"{enter_continue}")
        
    except ValueError as e:
        print(f"You typed {e}. Please type 'yes' or 'no'!\n")
        return question_continue()
    
    return True
    

def main_flow():
    """
    Runs through all the functions.
    """
    input_number = get_input()
    generate_password(input_number)
    question_continue()
    

print("Welcome to the random password generator!\n")
main_flow()