#a dictionary that stores question and answers.
# have a variable that track the score of the player
# loop through the dict using key,value pairs.
# display each question and allow user to answer
# tell them they are wrong or right..
# show the final result when quiz is complete..

quiz = {
     'question1':{
        "question":'what is the capitail of India ?',
        "answer":"delhi"
     },
         'question2':{
        "question":'what is the capitail of  France?',
        "answer":"paris"
     },
         'question3':{
        "question":'what is the capitail of Germany ?',
        "answer":"berlin"
     },
         'question4':{
        "question":'what is the capitail of Italy ?',
        "answer":"rome"
     },
         'question5':{
        "question":'what is the capitail of Spain?',
        "answer":"madrid"
     },
         'question6':{
        "question":'what is the capitail of Austria ?',
        "answer":"vienna"
     },
         'question7':{
        "question":'what is the capitail of England ?',
        "answer":"London"
     }    
}

score=0

for key,value in quiz.items():
    print(value['question'])
    answer = input("your answer :")
    if value['answer'].lower() == answer.lower():
        print("Correct")
        score+=1
        print("your score is :",score)
    else:
        print("Wrong,answer is :",value['answer'])
        print("your score is :",score)