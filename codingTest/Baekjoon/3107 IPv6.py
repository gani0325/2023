"""
[3107] IPv6

💛 문제
IPv6은 길이가 128비트인 차세대 인터넷 프로토콜이다.
IPv6의 주소는 32자리의 16진수를 4자리씩 끊어 나타낸다. 
이때, 각 그룹은 콜론 (:)으로 구분해서 나타낸다.

예를 들면, 다음과 같다.
2001:0db8:85a3:0000:0000:8a2e:0370:7334
32자리의 16진수는 사람이 읽고 쓰기에 불편하고, 
대부분의 자리가 0이기 때문에 아래와 같이 축약할 수 있다.

각 그룹의 앞자리의 0의 전체 또는 일부를 생략 할 수 있다. 
위의 IPv6을 축약하면, 다음과 같다
2001:db8:85a3:0:00:8a2e:370:7334

만약 0으로만 이루어져 있는 그룹이 있을 경우 그 중 한 개 이상 연속된 그룹을 하나 골라 콜론 2개(::)로 바꿀 수 있다.
2001:db8:85a3::8a2e:370:7334

2번째 규칙은 모호함을 방지하기 위해서 오직 한 번만 사용할 수 있다.
올바른 축약형 IPv6주소가 주어졌을 때, 

이를 원래 IPv6 (32자리의 16진수)로 복원하는 프로그램을 작성하시오.

💚 입력
첫째 줄에 올바른 IPv6 주소가 주어진다. 이 주소는 최대 39글자이다. 
또한, 주소는 숫자 0-9, 알파벳 소문자 a-f, 콜론 :으로만 이루어져 있다.

💙 출력
첫째 줄에, 입력으로 주어진 IPv6의 축약되지 않은 형태를 출력한다.
"""

IPv6 = input()
IPv6 = IPv6.split(':')

# # ['25', '09', '1985', 'aa', '091', '4846', '374', 'bb']
# print(IPv6)

temp = []

for i in range(len(IPv6)):
    if len(IPv6[i]) == 0:
        temp.append(i)
        continue

    if len(IPv6[i]) < 4:
        # 0 없는 만큼 채워줌
        IPv6[i] = "0" * (4 - len(IPv6[i])) + IPv6[i]
# print(IPv6)
# print(temp)

# 0으로만 이루어짐
if temp:
    for _ in temp:
        del IPv6[temp[0]]

    # IPv6의 길이가 8이 될 때까지
    while len(IPv6) != 8:
        IPv6.insert(temp[0], "0000")

print(":".join(IPv6))
