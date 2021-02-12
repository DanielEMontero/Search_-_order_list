import random

2
def order_a_list(my_list):
    print('\n\nThank you. \nNow, please select the method to order your list. 1,2 or 3?: \n 1. Bubble Sort. \n 2. Insertion Sort. \n 3. Merge Sort.')
    method_1 = input(f'\n Your method:')

    try:
        method_1 = int(method_1)
    except:
        print('Your method is not a number. Please insert a number.')
        order_a_list(my_list)
    
    if method_1 == 1:
        n = len(my_list)

        for i in range(n):
            for j in range(0, n - i - 1):
                
                if my_list[j] > my_list[j + 1]:
                    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
        return my_list

    elif method_1 == 2: 
        pass
    elif method_1 == 3:
        pass
    else:
        print('Please select a valid option: 1, 2 or 3')
        order_a_list(my_list)


def srch_a_number(my_list):
    print('\n\nThank you. \nNow, please select the method to search a number in the list. 1 or 2?: \n 1.Line Search. \n 2.Binary Search.')
    method_2 = input(f'\n Your method:')

    try:
        method_2 = int(method_2)
    except:
        print('Your method is not a number. Please insert a number.')
        srch_a_number(my_list)
    
    if method_2 == 1:
        pass
    elif method_2 == 2:
        pass
    else:
        print('Please select a valid option: 1 or 2')
        srch_a_number(my_list)


def run():
    print(f'What do you want to do. 1 or 2?: \n 1.Search a number in a list of numbers. \n 2.Order a list of numbers.')
    election = input(f'\n Your election:')
    list_size = input(f'Now, select the list size:')

    try:
        election = int(election)
        list_size = int(list_size)
    except:
        print('Your election or size is not a number. Please insert a number.')
        exit()
    
    my_list = [random.randint(0,100) for i in range(list_size)]
    print(f'Your list: \n {my_list}')

    if election == 1:
        new_list = order_a_list(my_list)
        return new_list
    elif election == 2:
        order_a_list(my_list)
    else:
        print('Please select a valid option: 1 or 2')
        exit()
       

if __name__ == "__main__":
    run()
    







