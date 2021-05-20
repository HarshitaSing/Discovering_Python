if __name__ == '__main__':
    students = [] # empty list to store name & score together
    scores = set() # to store unique scores
    names = [] # to store names at the end
    
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score]) # adding the name & score inside list
    scores.add(score) # adding scores in the set

second_lowest_marks = sorted(scores)[1] # getting the second lowest mark

for name,score in students: # looping over name & score in students list
    if score == second_lowest_marks: # getting the name of students having 2nd lowest mark
        names.append(name) # adding the names to the list

for name in sorted(names):
    print (name) # printing the names in sorted order
