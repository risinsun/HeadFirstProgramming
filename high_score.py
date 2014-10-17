__author__ = 'risinsun'

result_file = open("result.txt")
scores = []

for line in result_file:
    (name, score) = line.split(" ")
    scores.append(float(score))

scores.sort(reverse=True)
result_file.close()

print("The highest score is: ")
print(scores[0])
print("The second score is: ")
print(scores[1])
print("The third score is: ")
print(scores[2])
