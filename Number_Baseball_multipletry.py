#2022-2 알고리즘(공통) 최종프로젝트
#cows and bulls 자동 풀이
#참여인원 : 컴퓨터학부 20180500 오승준, 컴퓨터학부 20193437 공병현
#1. brute-force 알고리즘

#기능
#1. 컴퓨터가 랜덤수를 생성(완료)
#2. 랜덤수를 찾기 위해 아래 코드가 수행됨(완료)
#3. 수행시간, 완료되기까지의 횟수 확인(완료)
#4. 지정횟수만큼 반복해서 평균횟수 뽑기(완료)

import itertools
import random
import time

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

#랜덤난수 생성해서 allCaseNums중 하나 선택
def randomNum(allCaseNums):
    number = random.randrange(1, len(allCaseNums))
    return allCaseNums[number]

#AI가 제시해준 숫자열과 난수를 비교해 strike와 ball을 구하고 반환
def checkStrikeBall(numberStringByAI, randomNumberString):
    strike, ball = 0, 0
    for i in range(4):
        for j in range(4):
            if(i == j and numberStringByAI[i] == randomNumberString[j]):
                strike = strike + 1
                continue
            if(i != j and numberStringByAI[i] == randomNumberString[j]):
                ball = ball + 1
                continue

    return strike, ball

#========================================main수행==========================================
arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
totalCount = 0
totalCycleTime = 0
cycleTimeList = []

#==========================================================================================
for total in range(1000): #사용자 지정 횟수 반복
    allCaseNums = list(itertools.permutations(arr,4)) # 0~9를 가지고 4자리 순열 리스트 생성
    randomNumberString = randomNum(allCaseNums)
    print("=====================================")
    print("난수생성 : ", end='')
    for i in range(4):
        print(randomNumberString[i], end='')
    print("\n")

    count = 0 #완료될때까지의 횟수
    singleCycleTime = 0

    start = time.time()
    #==========================================================================================
    while (len(allCaseNums) != 1): # 리스트에 원소가 1개만 남을 때 까지
        print("AI : ", end='')
        for i in range(4):
            print(allCaseNums[0][i], end='')
        print()

        numberStringByAI = allCaseNums[0]
        strike, ball = checkStrikeBall(numberStringByAI, randomNumberString)
        print("strike :", strike, "/ ball :", ball)
        allCaseNums = RemoveElements(allCaseNums, allCaseNums[0], strike, ball)
        count = count + 1
    #==========================================================================================
    end = time.time()

    print()
    print("AI : 정답은 ", end='')
    for i in range(4):
        print(allCaseNums[0][i], end='')
    print()
    print(f"정답까지 {count}번 반복")
    print(f"정답까지 걸린 시간 : {end - start:.5f} sec\n=====================================\n")
    singleCycleTime = end - start
    totalCount += count
    totalCycleTime += singleCycleTime
    cycleTimeList.append(singleCycleTime)
    
#==========================================================================================
total += 1
print("brute-force 결과확인")
print(f"숫자야구게임을 진행한 횟수 : {total}회")
print(f"정답까지 반복횟수 평균 : {totalCount/total:.5f}회")
print(f"숫자야구게임 전체 진행시간 : {totalCycleTime:.5f}초")
print(f"정답까지 걸린시간 평균 : {totalCycleTime/total:.5f}초")
print(f"최대시간 : {max(cycleTimeList):.5f}초")
print(f"최소시간 : {min(cycleTimeList):.5f}초")