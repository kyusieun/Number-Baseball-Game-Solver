## 숫자야구 게임이란
  숫자야구 게임의 원제는 Bulls and Cows 이다.  
  한국에서는 Bulls 대신 Strike Cows 대신 Ball을 사용한다.  
  정답은 0에서 9까지 서로 다른 4자리 숫자이다.  
  숫자는 맞지만 위치가 틀렸을 때는 Ball.  
  숫자와 위치가 전부 맞으면 Strike.  
  무엇이 볼이고 스트라이크인지는 알려주지 않는다.
  Strike와 Ball의 단서를 토대로 정답을 추리하는 게임이다.
  
## 개요
  1. 숫자야구게임을 Brute-Force 방식으로 풀어주는 **Number_Baseball_Solver.py**  
  2. Brute-Force 방식으로 1000번 수행하여 Performance를 측정하는 **Number_Baseball_multipletry.py**  
  3. Backtracking 방식으로 개선한 **Number_Baseball_backtracking_multipletry.py**  
  4. Tabulation 방식으로 개선한 **Number_Baseball_tabulation_multipletry.py**  
  


## 알고리즘
먼저 숫자야구게임을 Brute-Force 방식으로 풀어주는 **Number_Baseball_Solver.py**를 작성함.  
1. 0~9의 숫자로 중복없는 4자리 순열 리스트 allCaseNums를 생성
2. allCaseNums의 첫번째 원소로 추측하여 유저에게 strike와 ball을 입력받음
3. 입력받은 strike와 ball을 토대로 allCaseNums를 순회하며 strike와 ball이 일치하지 않는 경우의수 전부 제거
4. allCaseNums에 원소가 1개 남을 때 까지 2~3 반복
5. 1개 남으면 종료후 정답 출력

Brute-Force 방식으로 1000번 수행하여 Performance를 측정하는 **Number_Baseball_multipletry.py**  
Number_Baseball_Solver.py의 알고리즘을 그대로 사용함.  
난수를 생성하여 임의의 정답을 만들고 이를 추측하는 방식으로 1000번 반복 수행하여 Performance를 측정함.  

Backtracking 방식으로 개선한 **Number_Baseball_backtracking_multipletry.py**  
기존의 Brute-Force 방식에서 가지치기를 하여 쓸모 없는 시행을 줄임.  
GetStrikeAndBall 함수는 인자로 추측한 값과 비교할 값을 넣고 tempStrike와 tempBall을 반환받는다.  
GetStrikeAndBall함수에 인자로 strike와 ball을 추가로 받아서 (tempStrike > strike or tempBall > ball)인 순간에 바로 탈출하는 루트를 추가했다.  

Tabulation 방식으로 개선한 **Number_Baseball_tabulation_multipletry.py**  
SBlist.pkl 파일에 0123으로 예측한 strike와 ball에 따른 경우의 수를 미리 계산하여 저장해서 수행 시간을 단축함.  
첫 추측은 어떤 수로 하던 평균적으로 무의미하기 때문에 0123으로 고정하여 제일 실행시간이 긴 첫 시도 부분을 스킵 가능.  


## Performance

### Brute-Force  
Average Try Count: 5.0043  
Total Execution Time: 31.356735  
Average Execution Time: 0.031355  
Maximun Execution Time: 0.087991  
Minimun Execution Time: 0.019327  

### Backtracking
Average Try Count: 5.0172  
Total Execution Time: 26.212737  
Average Execution Time: 0.026214  
Maximun Execution Time: 0.080989  
Minimun Execution Time: 0.013913  

### Tabulation
Average Try Count: 5.0003  
Total Execution Time: 17.645144  
Average Execution Time: 0.017618  
Maximun Execution Time: 0.039708  
Minimun Execution Time: 0.011887 

도쿄대 Tetsuro Tanaka 에 의해 minimum expected game length 가 5.213 이라는 것이 수학적으로 증명됨.  
따라서 Execution Time을 줄이는 방향으로 개선함.

## Requirment
 사용한 모듈: itertools, random, time, pickle  
 Number_Baseball_tabulation_multipletry.py을 실행하기 위해서는 SBlist.pkl이 동일한 경로에 위치해야 함.  

## 참조
https://hoil2.tistory.com/37 : **Number_Baseball_Solver.py** 구현시 참조
