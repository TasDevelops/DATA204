print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list    # another way is  print(x[:5])
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
five = [i for i in x[0:5]]
print (five)




print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even) another way 
# x_even = [num for num in x if num % 2 == 0]  print (x_even)

x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
for i in x:
    if i % 2 ==0:
        print(i)





print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
for n in x[:5]:
    if n % 2 ==0:
        print(n, end=" ")






print("\nQ2a\n")

# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
for list in names:
    print(list[0], end=" ")






print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

first_spaces = []
for name in names:
    first_spaces.append(name.index(" "))
    print(first_spaces)




print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
for name in names:
    initials = name[0] + name[name.index(' ')+1]
    print(initials)


print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


new_list = []
for x in list_of_lists:
    if len(set(x)) == len(x):
        new_list.append(x)
print(new_list)
# A3a:


print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

a = int(input("Input a number greater than 100: "))
while a != 100:
    if a < 100:
        a = int(input("Input a number greater than 100: "))
    elif a > 100:
        print(a)
        break
else: a = int(input("Input a number greater than 100: "))

for i in range (2,a):
    if a % i ==0:
        print('not prime')
        break
    else:
        print('prime')
        break




print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:

for i in range (2,a):
    if a % i ==0:
        print('not prime')
        break
    else:
        print('prime')
        break



    
