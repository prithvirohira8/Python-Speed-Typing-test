import time
import random

print("Python Speed Typing Test")
print("\n\n")
lst_of_paragraphs = ["Python is a fantastic programming language", "Java is an object oriented programming language",
                     "C++ has the fastest execution time for any program", "Python is the most popular language"]
s = input("Press type yes when u are ready: ")
test_string = ""
input_string = ""
time_taken = 0
if s == "yes":
    print("\n(Please enter the words with the correct punctuation marks too)\n\n")
    test_string = random.choice(lst_of_paragraphs)
    print(test_string)
    print("\n\n\n")
    t1 = time.time()
    input_string = input("Type the lines here: ")
    t2 = time.time()
    time_taken = (t2 - t1)

    
    
count2 = 0
for i in range(min(len(test_string), len(input_string))):
    if input_string[i] != test_string[i]:
        count2 += 1
count2 += abs(len(test_string) - len(input_string))

res1 = test_string.split()
res2 = input_string.split()

test_lst_set = set()
input_lst_set = set()

for i in res1:
    test_lst_set.add(i)
    
for i in res2:
    input_lst_set.add(i)

count = 0
for i in input_lst_set:
    if(i in test_lst_set):
        count += 1
        test_lst_set.discard(i)
        
time_taken_in_mins = time_taken / 60
typing_speed = int(count // time_taken_in_mins)

typing_accuracy1 = (count/len(res1))*100

typing_accuracy2 = (1 - count2 / max(len(test_string), len(input_string))) * 100

typing_accuracy = (0.8*typing_accuracy1)+(0.2*typing_accuracy2)

print("The no of words typed correctly are: {}".format(count))

if(len(test_lst_set) != 0):
    print("\nThe incorrectly typed/missing words are: ",)
    for i in test_lst_set:
        print("{} ".format(i),end='')

print("\n\nYour typing speed is {} words per minute".format(typing_speed))
print("\nYour typing accuracy is {:.2f}% ".format(typing_accuracy))
if typing_speed < 35:
    print("\nThe average person types at a speed of 30 words per minute, your typing speed is below average")
elif typing_speed < 75:
    print("\nThe average person types at a speed of 30 words per minute, your typing speed is above average")
elif typing_speed >= 75:
    print("\nProfessional typists type at a speed of 75 words or more, you are a proffessional ")
