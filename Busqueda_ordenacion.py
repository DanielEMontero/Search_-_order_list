import random

def order_a_list(number):
    pass


def srch_a_number(number):
    pass


def run():
    print(f'What do you want to do?: \n 1.Search a number in a list of numbers. \n 2.Order a list of numbers.')
    election = input(f'\n Your election:')
    try:
        election = int(election)
    except:
        print('Your election is not a number. Please insert a number.')
        quit

    if election == 1:
        srch_a_number(election)
    elif election == 2:
        order_a_list(election)
    else:
        print('Please select a valid option')
        quit
        

if __name__ == "__main__":
    run()







