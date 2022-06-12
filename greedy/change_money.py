'''
거슴름돈 거슬러주는 알고리즘 짜기
KEY_POINT
    1. "가장 큰 화폐 단위부터" 돈을 거슬러주는 것
'''
n = 1260
count = 0

#큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin #  해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin
    
print(count)