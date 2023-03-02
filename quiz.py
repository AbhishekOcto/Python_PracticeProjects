print("Welcome to my computer quiz!")

playing = input("Do you want to play? type Y/N ")
#print(playing)

if playing != "Y":
    quit()

print("Okay! Let's play :) ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does CG stand for? ")
if answer.lower() == "computer graphics":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the  brain of computer? ")
if answer.lower() == "cpu":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Final Score = " +str(score)+ "/5")
print("You Scored " +str((score/5) * 100 )+ "%")


if score == 5:
    print("Excellent")
elif score == 4:
    print("Very good!")
elif score == 3:
    print("Average")
else:
    print("Go again in class 3 and study well!!!")
