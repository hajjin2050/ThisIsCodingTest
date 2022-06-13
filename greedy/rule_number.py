'''
첫쨰 줄에 N(2<=N<=1000), M(1<=M<=10000), K(1<=K<=10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분
둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각가의 자연수는 1 이상 10,000이하의 수로 주어진다
입력으로 주어지는 K 는 항상 M보다 작거나 같다

=> 가장 큰 수를 ㅏ번 더하고 두번째로 큰 수를 한번 더하는 연산
'''

# N,K,M 를 공백을 구분하여 입력
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list((map(int, input().split())))

data.sort()  # 입력받은 수들 정렬하기
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두 번째로 큰 수

result = 0

# 1번
while True:
    for i in range(k):  # 가장 큰수를 K 번 더하기
        if m == 0:  # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1  # 더할 때마다 1씩 빼기
    if m == 0:
        break
    result += second
    m -= 1

print(result)

# 2번
count = int(m / (k+1)) * k
count += m % (k+1)  # 가장 큰 수가 더해지는 횟수

result = 0
result += (count) * first
result += (m - count) * second
