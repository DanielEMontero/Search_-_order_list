###########################################################
###########################################################

############## SEARCH A NUMBER & ORDER A LIST #############

###########################################################

####################### DESCRIPTION #######################
# This program let you do two proccess: 
# 1. Search a number in a list (even if the list is not ordered).
# with two diferents methods: Lineal and binary search.
# 2. Order a list with tree diferents methods: buble, insertion and
# merge sort. 

######################### AUTHOR ##########################
# Ing. DANIEL EDUARDO MONTERO RAMÍREZ


import random


def merge_sort(my_list):
    if len(my_list) > 1:
        middle = len(my_list) // 2
        left = my_list[:middle]
        right = my_list[middle:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                my_list[k] = left[i]
                i += 1
            else:
                my_list[k] = right[j]
                j += 1
            
            k += 1

        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1

    return my_list


def binary_search(my_list, target, start, finish):
    if start > finish:
        return False
        
    middle = (start + finish) // 2

    if my_list[middle] == target:
        return True
    elif my_list[middle] < target:
        return binary_search(my_list, target, middle + 1, finish)
    else:
        return binary_search(my_list, target, start, middle - 1)


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
        n = len(my_list)  

        for i in range(1,n):
            current_value = my_list[i]
            current_position = i

            while current_position > 0 and my_list[current_position - 1] > current_value:
                my_list[current_position] = my_list[current_position - 1]
                current_position -= 1
            
            my_list[current_position] = current_value
        
        return my_list

    elif method_1 == 3:
        new_list = merge_sort(my_list)
        return new_list

    else:
        print('Please select a valid option: 1, 2 or 3')
        order_a_list(my_list)


def srch_a_number(my_list,target):
    print('\n\nThank you. \nNow, please select the method to search a number in the list. 1 or 2?: \n 1.Linear Search. \n 2.Binary Search.')
    method_2 = input(f'\n Your method:')

    try:
        method_2 = int(method_2)
    except:
        print('Your method is not a number. Please insert a number.')
        srch_a_number(my_list)
    
    if method_2 == 1:    
        match = False
        
        for i in my_list:
            if i == target:
                match = True
                break
        
        return match

    elif method_2 == 2:
        start = 0
        finish = len(my_list)
        my_list = merge_sort(my_list)
        return binary_search(my_list,target,start,finish)

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
        target = input(f'Please select the target number: ')
        try:
            target = int(target)
        except:
            print(f'Your target number {target} is not a valid option. Please try again')

        new_list = srch_a_number(my_list,target)
        print(f'The target: {target} {"is" if new_list else "is not"} in the list.')

    elif election == 2:
        new_list = order_a_list(my_list)
        print(my_list)

    else:
        print('Please select a valid option: 1 or 2')
        exit()
       

if __name__ == "__main__":
    run()