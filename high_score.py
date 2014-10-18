__author__ = 'risinsun'

result_file = open("result.txt")
scores = {}

for line in result_file:
    (name, score) = line.split(" ")
    scores[score] = name

for score, name in sorted(scores.items(), reverse=True):
    print(name + ' has point of ' + str(score))

result_file.close()
