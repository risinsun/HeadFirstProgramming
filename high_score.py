__author__ = 'risinsun'

highest_score = 0
result_file = open("result.txt")

for line in result_file:
    (name, score) = line.split(" ")
    if float(score) > highest_score:
        highest_score = float(score)

result_file.close()

print("The highest score is: ")
print(highest_score)