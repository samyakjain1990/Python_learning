# using a nested list comprehension and range(),create a variable called answer
# with the following value [[0,1,2],[0,1,2],[0,1,2]]. To break it down...start by using 
# range and a list of comp to generate the list[0,1,2].
# and repeat the whole thing  times in a nested list comp.

answer = [[num for num in range(3)] for listm in range(3)] 

print(answer)


answer = [[num for num in range(10)] for listm in range(10)] 

print(answer)