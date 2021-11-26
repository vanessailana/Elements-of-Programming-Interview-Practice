
'''

The parity of a binary word is 

1 if the word contains an odd num of 1s and 
0 if it contains an even number of ones.

1 if the word contains an odd number of 1s and,
0 if it contains an even number of ones.

10011

parity 1 because odd num of 1s
'''


n= input("enter word")

print("The word give is",n)

#partiy = 0

data=n.count('1')


#convert count to int 

count = int(data)
print(count)

if count==0:
    print("there are no 1's ")
elif count %2==0:
    print("Parity = 0 because of the even number of 1s.")
else:
    print("Parity = 1 because of the odd number of 1s.")



#test cases
'''
 word given by user is:  1011
Parity is  1

The word given by user is:  10001000
Parity is  0
'''
