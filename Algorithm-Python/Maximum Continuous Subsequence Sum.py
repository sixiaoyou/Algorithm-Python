def maxSum(list):
    maxNum=0
    for i in range(len(list)):
        for j in range(i,len(list)):
            thisNum = 0
            for k in range(i,j):
                thisNum+= list[k]
            if thisNum > maxNum:
                maxNum = thisNum
    return maxNum

def maxSum2(list):
    maxNum = 0
    thisNum = 0
    for i in range(len(list)):
        thisNum+=list[i]
        if thisNum > maxNum:
            maxNum = thisNum
        elif thisNum < 0:
            thisNum=0
    return maxNum

if __name__ == "__main__":
    list=[1,2,3,-1,4,5,6,7,-2]
    # list=[-1,-2,-3,-4]
    print maxSum2(list)
