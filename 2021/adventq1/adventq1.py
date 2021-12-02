def adventq1(s):
    L = [] #convert this whole thing to a list, lists are easy, lists are simple, lists are beatiful
    with open(s, 'r') as f:
        for line in f:
            line = line.replace("\n", "")
            L.append(int(line))
            
    increased = 0 #initiate count
    for i in range(len(L)): #loop through list
        if L[i]>L[i-1]:
            increased = increased + 1 #add 1 to count everytime it notices an increase
             
    print(increased)
adventq1("input.txt")