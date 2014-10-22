__author__ = 'risinsun'

import ready

number_asked = 0
number_correct = 0
number_wrong = 0
s1 = ready.sounds.Sound("correct.wav")
s2 = ready.sounds.Sound("wrong.wav")

choice = input("Enter your choice: ")
while choice != 0:
    if choice == 1:
        number_correct += 1
        ready.wait_finish(s1.play())
    else:
        number_wrong += 1
        ready.wait_finish(s2.play())
    number_asked += 1
    choice = input("Enter your choice: ")

print("number asked: %d, number_correct: %d, number_wrong: %d" % (number_asked, number_correct, number_wrong))

