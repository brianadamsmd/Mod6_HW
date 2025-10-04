#!/usr/bin/env python
# coding: utf-8

# In[16]:


def wrong_add_function(arg1,arg2):
    '''
    The function takes in two lists of integers, then it adds
    all of arg2 to each item of arg1.
    
    Example:
    > wrong_add_function([1,2,3],[1,1,1])
    > [6,9,12]
    
    whereas the expected correct answer is, [2,3,4]
    
    Parameters
    ----------
    arg1 : list
    list of integers.
    arg2 : list
    list of integers.
    
    Returns
    -------
    arg1 : list
    Elements of arg1, with each element having had the contents of 
    arg2 added to it.
    
    '''
    arg1_index=0

    # NOTE: The expected output [2,3,4] for the input ([1,2,3],[1,1,1])
    # implies elementwise addition (arg1[i] + arg2[i]), not adding
    # the every element in arg2 to each element of arg1.
    expected_output = [arg1[i] + arg2[i] for i in range(len(arg1))]
    print(f"The correct answer is supposed to be: {expected_output}. This was generated using a list comprehension and is a lot less code than a while loop.\n\n\n")

    while arg1_index < len(arg1):
        arg_2_sum = 0
        # ------------------------------------------------------------------
        # We are making an error in the loop!
        # This line calculates the sum of (arg1[arg1_index] + all of arg2),
        # which is why the output is [6, 9, 12] instead of [2, 3, 4].
        # ------------------------------------------------------------------
        for arg2_elements in arg2:
            print("1.a: Here is the error. The sum(arg1[arg1_index]+i for i in arg2]) is adding each value of arg2 to the value at arg1[arg1_index] then summing the iterable together.")
            # ie arg1[0] (1) + arg2[0] (1) = 2, arg1[0] (1) + arg2[1] (1) = 2, arg1[0] (1) + arg2[2] (1) = 2; 2+2+2 = 6
            # ie arg1[1] (2) + arg2[0] (1) = 3, arg1[1] (2) + arg2[1] (1) = 3, arg1[1] (2) + arg2[2] (1) = 3; 3+3+3 = 9
            # ie arg1[2] (3) + arg2[0] (1) = 4, arg1[2] (3) + arg2[1] (1) = 4, arg1[1] (3) + arg2[3] (1) = 4; 4+4+4 = 12
            arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
            print(f"arg_2_sum = {arg_2_sum}")
        arg1[arg1_index]=arg_2_sum  
        arg1_index+=1 
    return arg1


def correct_add_function(arg1,arg2):
    '''
    The function takes in two lists of integers, then it adds
    all of arg2 to each item of arg1.
    
    Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [6,9,12]
    
    whereas the expected correct answer is, [2,3,4]
    
    Parameters
    ----------
    arg1 : list
      list of integers.
    arg2 : list
      list of integers.
    
    Returns
    -------
    arg1 : list
      Elements of arg1, with each element having had the contents of 
      arg2 added to it.
    
    '''
    arg1_index=0

    while arg1_index < len(arg1):
        # ---We only need to add the element at the same index----
        # ---This one line replaces the incorrect inner for loop logic---
        arg1[arg1_index] = arg1[arg1_index] + arg2[arg1_index]
        arg1_index+=1

    # ******************************
    # or even more concise would be to remove the outer while loop altogether and just use this:
        # expected_output = [arg1[i] + arg2[i] for i in range(len(arg1))]
        # print(f"The correct answer is supposed to be: {expected_output}. This was generated using a list comprehension and is a lot less code than a while loop.\n\n\n")
    # ******************************
    
    return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]

wrong_add_function(arg1, arg2)

arg1 = [1,2,3]
arg2 = [1,1,1]
correct_add_function(arg1, arg2)


# In[62]:


#%% try, except
'''
2.a
Update the numeric section of the function with your changes from 1 for both 
2.b and 2.c

2.b
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
returns an error message to the user, in case users give invalid inputs,
(for example an input of ["5","2", 5])
: "Your input argument [1 or 2] at element [n]
is not of the expected type. Please change this and rerun. Name this function 
exception_add_function()

2.c
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
gets it to process via the string section. IE, do not, outside the function,
change the values of arg_str_1 or arg_str_2. Name this function 
correction_add_function(), i.e you will not be updating the wrong_add_function,
you will simply handle the error of wrong inputs in a seperate function, you want
the wrong_add_function to output its current result you are only bolstering the 
function for edge cases .
'''
def q2_wrong_add_function(arg1,arg2):
   '''
   The function takes in two lists of integers, then it adds
   all of arg2 to each item of arg1.
   
   Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [4,5,6]
   
   If the lists are lists of strings, concatenate them
   Example:
      > wrong_add_function(['1','2','3'],['1','1','1'])
      > ['1111','2111','3111']
   Parameters
   ----------
   arg1 : list
      list of integers.
   arg2 : list
      list of integers.

   Returns
   -------
   arg1 : list
      Elements of arg1, with each element having had the contents of 
      arg2 added to it.

   '''
   #numeric section
   if sum([type(i)==int for i in arg1])==len(arg1) and \
      sum([type(i)==int for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            # if I were to change the code without the "little as possible" constraint it would look like this:
            # ---We only need to add the element at the same index----
            # ---This one line replaces the incorrect inner for loop logic---
            arg1[arg1_index] = arg1[arg1_index] + sum(arg2)
            arg1_index+=1

            # ******************************
            # or even more concise would be to remove the outer while loop altogether and just use this:
                # expected_output = [arg1[i] + arg2[i] for i in range(len(arg1))]
                # print(f"The correct answer is supposed to be: {expected_output}. This was generated using a list comprehension and is a lot less code than a while loop.\n\n\n")
            # ******************************
         return arg1
   #string section
   elif sum([type(i)==str for i in arg1])==len(arg1) and \
      sum([type(i)==str for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
               arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
         return arg1

def exception_add_function(arg1, arg2):
    try:
        #checks to see all values are integers and if not raises a type error otherwise if all are integers it goes straight to q2_wrong_add_function
        if not sum([type(i)==int for i in arg1])==len(arg1) or not sum([type(i)==int for i in arg2])==len(arg2):
            raise TypeError
        else:
            return q2_wrong_add_function(arg1,arg2)
    
    except TypeError:
        #specifies where theere are elements taht are not integers in the first argument
        for i, element in enumerate(arg1):
            if type(element) != int:
                print("*****************************************************")
                print(f"The first argument passed to this function at element {i} is not of the expected type. Please check this and rerun the code.")
                print("*****************************************************")
        #specifies where there are elements that are not integers in the second argument
        for i, element in enumerate(arg2):
            if type(element) != int:
                print("*****************************************************")
                print(f"The second argument passed to this function at element {i} is not of the expected type. Please check this and rerun the code.")   
                print("*****************************************************")
        return correction_add_function(arg1, arg2)

def correction_add_function(arg1, arg2):
    try:
        #Checks to see if all elements are integers and if so calls q2_wrong_add_function and aborts the rest of the this function
        if sum([type(i)==int for i in arg1])==len(arg1) and sum([type(i)==int for i in arg2])==len(arg2):
            return q2_wrong_add_function(arg1,arg2)
        
        #Checks to see if any of the elements are not strings, raises an error if there are and goes to the except statement 
        if not sum([type(i)==str for i in arg1])==len(arg1) or not sum([type(i)==str for i in arg2])==len(arg2):
            raise ValueError
            
    except ValueError:
        #converts any element in arg1 that is not a str to a string
        for i, element in enumerate(arg1):
            if type(element) != str:
                print(f"The first argument passed at [{i}] type was a {type(arg1[i])}.")
                arg1[i] = str(arg1[i])
                print(f"The first argument passed at [{i}] type is now a {type(arg1[i])}, value = {arg1[i]}")
        
        #converts any element in arg2 that is not a str to a string
        for i, element in enumerate(arg2):
            if type(element) != str:
                print(f"The second argument passed at [{i}] type was a  {type(arg2[i])}.")
                arg2[i] = str(arg2[i])
                print(f"The second argument passed at [{i}] type is now a {type(arg2[i])}, value = {arg2[i]}")
        #after all the integers have been converted q2_wrong_add_function is called so it will enter the "string section"
        return q2_wrong_add_function(arg_str_1,arg_str_2)

arg_str_1=[1,2,3]
arg_str_2=[1,1,"1"]

exception_add_function(arg_str_1,arg_str_2)

