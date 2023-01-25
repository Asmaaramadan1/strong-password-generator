import string
import random

l1=list(string.ascii_lowercase)
l2=list(string.ascii_uppercase)
l3=list(string.digits)
l4=list(string.punctuation)

No_of_characters=input("How many characters do you want for the password? ")
while True:
    try:
        No_of_characters=int(No_of_characters)
        if No_of_characters <6 :
           print("The number must be greater than 6 and less than35 :)")
           No_of_characters=input("Choose a number greater than 6, please ^_^ :")
        elif No_of_characters >35 :
            print("The number must be greater than 6 and less than 35 :)")
            No_of_characters=input("Please choose a number less than 35: ")
        else:
            break
    except:
        print("Please enter numbers only :(")
        No_of_characters = input("Choose a number greater than 6 and less than 35, please ^_^ :")

random.shuffle(l1)
random.shuffle(l2)
random.shuffle(l3)
random.shuffle(l4)

p1=round(No_of_characters*(20/100))
p2=round(No_of_characters*(30/100))

password=[]
for i in range (p1):
    password.append(l1[i])
    password.append(l2[i])

for i in range (p2):
    password.append(l3[i])
    password.append(l4[i])

random.shuffle(password)
password="".join(password[0:])
print("your password :")
print(password)
