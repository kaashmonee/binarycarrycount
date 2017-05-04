#num = input("number: ")

def countCarries(number):
    number+=1
    number = str(number)
    number = list(number)
    carries = 0
    for x in range(len(number)-1, -1, -1):
        if int(number[x])==2:
            carries+=1
            if number[x-1]:
                number[x-1]=str(int(number[x-1])+1)
    print(carries),
    return carries

def run(runNum):
    myList=[]
    for i in range(0,runNum):
        temp = countCarries(int(format(i,"b")))
        myList.append(temp)
    print "\n"+str(sum(myList))
    
numberToRun = input("how many numbers: ")
run(numberToRun)
