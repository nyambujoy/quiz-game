print("Welcome to my computer game")
score=0

playing=input("do you want to play ")

if playing.lower() != "yes":
    quit()

print("okay lets play ! :)")  

answer=input("what does cpu stand for ? ")
if answer.lower() == "central processing unit":
    print("correct")
    score+=1
else:print("you got it wrong ")
answer=input("what is your first name ? ")
if answer.lower() == "joyliz":
    print("correct")
    score+=1
else:print("you got it wrong ")
answer=int(input("how old are you ? "))
if answer == 23:
    print("correct")
    score+=1
else:print("you got it wrong ")
answer=input("where are you from? ")
if answer.lower() == "nyandarua":
    print("correct")
    score+=1
else:print("you got it wrong ")

print(f"you scored {(score/4)*100}% ")