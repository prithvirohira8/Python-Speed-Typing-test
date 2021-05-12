import time
import random

print("Python Speed Typing Test")
print("\n\n")
lst_of_paragraphs = [
    "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma, which is living with the results of other people's thinking",
    "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.",
    "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.",
    "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart.",
    "Do not go where the path may lead, go instead where there is no path and leave a trail"]
s = 'yes'
if s == input("Press type yes when u are ready: "):
    print("\n(Please enter the words with the correct punctuation marks too)\n\n")
    test_string = random.choice(lst_of_paragraphs)
    print(test_string)
    print("\n")
    t1 = time.time()
    input_string = input("Type the lines here: ")
    t2 = time.time()
    time_taken = (t2 - t1)

res1 = test_string.split()
res2 = input_string.split()

test_lst_lst = []
input_lst_lst = []

for i in res1:
    test_lst_lst.append(i)

for i in res2:
    input_lst_lst.append(i)

sorted(test_lst_lst)
sorted(input_lst_lst)

count = 0
for i in input_lst_lst:
    for j in test_lst_lst:
        if i == j:
            count += 1
            test_lst_lst.remove(i)
            break;

time_taken_in_mins = time_taken / 60
typing_speed = int(count // time_taken_in_mins)
typing_accuracy = (count / len(res1)) * 100
print("The no of words typed correctly are: {}".format(count))

if (len(test_lst_set) != 0):
    print("\nThe incorrectly typed/missing words are: ", )
    for i in test_lst_set:
        print("{} ".format(i), end='')

print("\n\nYour typing speed is {} words per minute".format(typing_speed))
print("\nYour typing accuracy is {:.2f}% ".format(typing_accuracy))
if typing_speed<35:
    print("\nThe average person types at a speed of 30 words per minute, your typing speed is below average")
elif typing_speed<75:
    print("\nThe average person types at a speed of 30 words per minute, your typing speed is above average")
elif typing_speed>=75:
    print("\nProfessional typists type at a speed of 75 words or more, you are a proffessional ")
