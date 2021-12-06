# advent of code 2021, day 1: Sonar Sweep,   ** first attempt **

#boilerplate
fileobject = open("Day1.txt", "r")
lines_list = fileobject.readlines()             # gives list where each element is a line in the text file   
depth_measures = list( map(int, lines_list) )   # convert the elements in lines_list to numbers and load them into a new array
fileobject.close()
acc = 0                                         # accumulator variable for number of increases in depth

for i in range(0, len(depth_measures)):
    if i == 1:
        print("%d\t No previous measurement" %depth_measures[i])
    elif depth_measures[i-1] < depth_measures[i]:                   # if the previous depth is lower than the current depth => depth value has increased
        print("%d\t Increased" %depth_measures[i])
        acc += 1
    else:                                                           # if the previous depth is higher than the current depth => depth value has decreased
        print("%d\t Decreased" %depth_measures[i])

print("\nThere are %d measurements larger than the previous measurement." %acc)
