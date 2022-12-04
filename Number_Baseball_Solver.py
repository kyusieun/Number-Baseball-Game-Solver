import itertools

def RemoveElements(list, nums, strike, ball):
    i = 0
    for _ in range(len(list)):
        tempStrike, tempBall = GetStrikeAndBall(list[i], nums)

        if (strike != tempStrike or ball != tempBall): # strike ball이 둘다 같지 않으면 제거
            del list[i]
        else:
            i = i+1
    return list

def GetStrikeAndBall(curList, setList):
    tempStrike = 0
    tempBall = 0
    for i in range(4):
        for j in range(4):
            if ( i == j and curList[i] == setList[j]):
                tempStrike = tempStrike + 1
                break
            elif ( curList[i] == setList[j] ):
                tempBall = tempBall + 1
                break
    return tempStrike, tempBall

arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
allCaseNums = list(itertools.permutations(arr,4)) # 0~9를 가지고 4자리 순열 리스트 생성

while (len(allCaseNums) != 1): # 리스트에 원소가 1개만 남을 때 까지
    print("AI : ", end='')
    for i in range(4):
        print(allCaseNums[0][i], end='')
    print()

    strike = int(input("strike : "))
    ball = int(input("ball  : "))

    allCaseNums = RemoveElements(allCaseNums, allCaseNums[0], strike, ball)

print("AI : 정답은 ", end='')
for i in range(4):
    print(allCaseNums[0][i], end='')
print()

