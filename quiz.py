# simple quiz game
print("Welcome to Online Computer Quiz!!!")
play=input("Do you wanna play? ")

while play.lower() != "yes" :
    quit()

print("ohohh!! Let's play:)\n ")
score = 0 

print("QUESTIONS")
print("---------")


question0 = input("Which language is known as simplest and easy language to learn ?\n>>")
if question0.lower() == "python":
    print("---Correct---\n")
    score = score  + 1
else:
    print("Ohh noo, it's wrong:( \n")


question1 = input("What is CSS stands for ?\n>> ")
if question1.lower() == "cascading coding language":
    print("---Correct---\n")
    score += 1
else:
    print("Ohh noo, it's wrong:( \n")


question2 = input("Is HTML a programming language ?\n>>")
if question2.lower() == "no":
    print("---Correct---\n")
    score += 1
else:
    print("Ohh noo, it's wrong:( \n")


question3 = input("Which is the most trending language in 2024 ?\n>> ")
if question3.lower() == "javascript" :
    print("---Correct---\n")
    score += 1
else:
    print("Ohh noo, it's wrong:( \n")


question4 = input("Who developed C language ?\n>> ")
if question4.lower() == "Dennis Ritchie":
    print("---Correct---\n")
    score += 1
else:
    print("Ohh noo, it's wrong:( \n")


question5 = input("Which is the first operating system ?\n>> ")
if question5.lower() == "general motors":
    print("---Correct---\n")
    score += 1
else:
    print("Ohh noo, it's wrong:( \n")

question6 = input("Which keyword is used to come out of recursion ?\n>> ")
if question6.lower() == "return":
    print("---Correct---\n")
    score += 1
else:
    print("Ohh noo, it's wrong:( \n")

question7 = input("What is the maximum length of the filename in DOS ?\n>> ")
if question7.lower() == "8" :
    print("---Correct---\n")
    score += 1
else:
    print("Ohh noo, it's wrong:( \n")

question8 = input("What is the extension of the notepad ?\n>> ")
if question8.lower() == ".txt":
    print("---Correct---\n")
    score += 1
else:
    print("Ohh noo, it's wrong:( \n")

question9 = input("Which type of value does compareTo() returns _____ ?\n>> ")
if question9.lower() == "int":
    print("---Correct---\n")
    score += 1
else:
    print("Ohh noo, it's wrong:( \n")

question10 = input("What does AWT stands for ?\n>> ")
if question10.lower() == "abstract window toolkit":
    print("---Correct---\n")
    score += 1
else:
    print("Ohh noo, it's wrong:( \n")

question11 = input("A variable declared in a method is called as ?\n>> ")
if question11.lower() == "local data":
    print("---Correct---\n")
    score += 1
else:
    print("Ohh noo, it's wrong:( \n")

question12 = input("In C++, the index of the final element in as array is ?\n>> ")
if question12.lower() == "0":
    print("---Correct---\n")
    score += 1
else:
    print("Ohh noo, it's wrong:( \n")

question13 = input("Queue data strcture works on ?\n>> ")
if question13.lower() == "FIFO":
    print("---Correct---\n")
    score += 1
else:
    print("Ohh noo, it's wrong:( \n")

question14 = input("When a pop() operation is called on an empty queue, what is the condition called ?\n>> ")
if question14.lower() == "underflow":
    print("---Correct---\n")
    score += 1
else:
    print("Ohh noo, it's wrong:( \n")

print("Total score >> ",score)