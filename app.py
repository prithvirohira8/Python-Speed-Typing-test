from flask import Flask, render_template, request, Response, jsonify
import time
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET'])
def result():
    #a = request.args.post['original_text'];
    if request.method == 'GET':
        input_string=request.args.get('typed_text')
        test_string=request.args.get('original_text')
        start_time=request.args.get('start_time')
        end_time=request.args.get('end_time')
        #return jsonify({'typed': typed_text, 'original': original_text, 'starttime': start_time, 'endtime': end_time})
        
        t1=start_time.split(':')
        t2=end_time.split(':')

        if t1[0]==t2[0]:
            if t1[1]==t2[1]:
                time_taken=int(t2[2])-int(t1[2])
            elif t1[1]!=t2[1]:
                time_taken=60-int(t1[2])+int(t2[2])+((int(t2[1])-int(t1[1])-1)*60)

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

        typing_accuracy = (0.9*typing_accuracy1)+(0.1*typing_accuracy2)

        #print("The no of words typed correctly are: {}".format(count))
        incorrect_missing_words=[]
        if(len(test_lst_set) != 0):
            #print("\nThe incorrectly typed/missing words are: ",)
            for i in test_lst_set:
                #print("{} ".format(i),end='')
                incorrect_missing_words.append(i)


        #print("\n\nYour typing speed is {} words per minute".format(typing_speed))
        #rint("\nYour typing accuracy is {:.2f}% ".format(typing_accuracy))
        #if typing_speed < 35:
        #    print("\nThe average person types at a speed of 30 words per minute, your typing speed is below average")
        #elif typing_speed < 75:
        #    print("\nThe average person types at a speed of 30 words per minute, your typing speed is above average")
        #elif typing_speed >= 75:
        #    print("\nProfessional typists type at a speed of 75 words or more, you are a proffessional ")
        print(incorrect_missing_words)
        typing_accuracy=round(typing_accuracy, 2)
        return jsonify({'words_per_minute': typing_speed, 'typing_accuracy': typing_accuracy, 'correct_words': count, 'incorrect_missing': incorrect_missing_words})


if __name__=='__main__':
  app.run(debug=True)