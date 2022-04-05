"""
Python Assignment:

1. There is s a list which states the number of new users on the platform month on month for a
 6 month period, starting from 100 as the number of new users in the first month.

new = [100,170,150,140,120,110] 

Introduce/Create an empty list 

Calculate the month on month % change in new users using a for loop

Append the calculated values to the original list created (in 1) and print the list.

2. Create a function “turnout” that takes the value of the month for which the delta is calculated from the previous month 
and returns ‘Bad Turnout’ if the month on month delta is less than 0 and ‘Good Turnout’ otherwise. 

What is the value for the 4th month delta?
"""

def turnout(val):
    if val <0:
        print("bad turnout")
    else:
        print("good turnout")

if __name__ == "__main__":
    new = [100,170,150,140,120,110]

    newlist = []

    for x,y in zip(new[:-1],new[1:]):
        prt = (y-x)*100/x

        newlist.append(prt)
        new.append(prt)

        turnout(prt)

    print(newlist)
    #print(new)