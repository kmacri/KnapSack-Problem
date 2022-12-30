#read a file separated by commas

def knapsack(file, limit):
    #f = open("size.txt", "r")
    f = open(file, "r")
    array = []                          #will contain the value ratio of each item in the file
    for x in f:                         #for each line in the file
        y = x.split(", ")               #split each word by comma, y is a list with name + value + dimensions
        volume = int(y[2])*int(y[3])*int(y[4])         #volume of item
        array.append([int(y[1])/volume, y[0], volume])       #gives value ration (value/volume)

    #sort max-min
    array.sort(reverse=True)
    

    #repeatidly pick item with the largest ratio if its lower than capacity
    ans = []
    total = 0          #this is the total
    found = True
    index = 0
    print(array[index][2])
    while (total<=limit):
        if (array[index][2] + total) <= limit:
            ans.append(array[index][1])
            total=total+array[index][2]
        else:
            if (index == len(array)-1):
                break
            else:
                index= index+1
            

            
    print ("The total weight is: ", total)
    print (ans)

    

def main():
    limit = int(input("What is the cubic limit: "))
    knapsack("size2.txt", limit)

main()

