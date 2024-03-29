"""
개인정보 수집 유효기간

💛 문제
고객의 약관 동의를 얻어서 수집된 1~n번으로 분류되는 개인정보 n개가 있습니다. 
약관 종류는 여러 가지 있으며 각 약관마다 개인정보 보관 유효기간이 정해져 있습니다. 
당신은 각 개인정보가 어떤 약관으로 수집됐는지 알고 있습니다.

수집된 개인정보는 유효기간 전까지만 보관 가능하며, 유효기간이 지났다면 반드시 파기해야 합니다.

예를 들어, A라는 약관의 유효기간이 12 달이고, 2021년 1월 5일에 수집된 개인정보가 A약관으로 수집되었다면 
해당 개인정보는 2022년 1월 4일까지 보관 가능하며 2022년 1월 5일부터 파기해야 할 개인정보입니다.
당신은 오늘 날짜로 파기해야 할 개인정보 번호들을 구하려 합니다.

모든 달은 28일까지 있다고 가정합니다.

오늘 날짜를 의미하는 문자열 today, 약관의 유효기간을 담은 1차원 문자열 배열 terms와 
수집된 개인정보의 정보를 담은 1차원 문자열 배열 privacies가 매개변수로 주어집니다.

이때 파기해야 할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

🧡 제한 사항
today는 "YYYY.MM.DD" 형태로 오늘 날짜를 나타냅니다.
1 ≤ terms의 길이 ≤ 20
    terms의 원소는 "약관 종류 유효기간" 형태의 약관 종류와 유효기간을 공백 하나로 구분한 문자열입니다.
    약관 종류는 A~Z중 알파벳 대문자 하나이며, terms 배열에서 약관 종류는 중복되지 않습니다.
    유효기간은 개인정보를 보관할 수 있는 달 수를 나타내는 정수이며, 1 이상 100 이하입니다.
1 ≤ privacies의 길이 ≤ 100
    privacies[i]는 i+1번 개인정보의 수집 일자와 약관 종류를 나타냅니다.
    privacies의 원소는 "날짜 약관 종류" 형태의 날짜와 약관 종류를 공백 하나로 구분한 문자열입니다.
    날짜는 "YYYY.MM.DD" 형태의 개인정보가 수집된 날짜를 나타내며, today 이전의 날짜만 주어집니다.
    privacies의 약관 종류는 항상 terms에 나타난 약관 종류만 주어집니다.
today와 privacies에 등장하는 날짜의 YYYY는 연도, MM은 월, DD는 일을 나타내며 점(.) 하나로 구분되어 있습니다.
    2000 ≤ YYYY ≤ 2022
    1 ≤ MM ≤ 12
    MM이 한 자릿수인 경우 앞에 0이 붙습니다.
    1 ≤ DD ≤ 28
    DD가 한 자릿수인 경우 앞에 0이 붙습니다.
파기해야 할 개인정보가 하나 이상 존재하는 입력만 주어집니다.

💚 입출력
today	        terms	                privacies	                                                                        result
"2022.05.19"	["A 6", "B 12", "C 3"]	["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]	                [1, 3]
"2020.01.01"	["Z 3", "D 5"]	        ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]    [1, 4, 5]
"""


def solution(today, terms, privacies):
    answer = []

    y, m, d = today.split(".")
    y, m = int(y), int(m)

    # 오늘 날짜를 의미하는 문자열 today, 약관의 유효기간을 담은 1차원 문자열 배열 terms
    # 수집된 개인정보의 정보를 담은 1차원 문자열 배열 privacies

    # input 값들을 전처리 해준다 예쁘게 다시 split 해서 새 배열 안으로 넣어준다
    terms_temp = []

    for i in range(len(terms)):
        a, b = terms[i].split(" ")
        # [['A', 6], ['B', 12], ['C', 3]]
        terms_temp.append([a, int(b)])

    privacies_temp = []
    for i in range(len(privacies)):
        a, b = privacies[i].split(" ")
        y, m, d = a.split(".")
        # [[2021, 5, 2, 'A'], [2021, 7, 1, 'B'], [2022, 2, 19, 'C'], [2022, 2, 20, 'C']]
        privacies_temp.append([int(y), int(m), d, b])

    new_privacies_temp = [[] for _ in range(len(privacies))]
    # 유효 기간 입력하기
    for i in range(len(terms_temp)):
        for j in range(len(privacies_temp)):
            temp = []
            # 약관 종류 비교하기
            if terms_temp[i][0] == privacies_temp[j][3]:
                # 약관 유효 기관 (달) 더하기
                yy = privacies_temp[j][1] + terms_temp[i][1]
                # 12개월 (1년) 을 지난다면 년도 +1
                if yy > 12:
                    if (yy % 12 == 0):
                        yyy = yy // 12 - 1
                        privacies_temp[j][0] += yyy
                        yy = 12
                    else:
                        yyy = yy // 12
                        privacies_temp[j][0] += yyy
                        yy -= 12 * yyy

                temp = [privacies_temp[j][0], str(
                    yy).zfill(2), privacies_temp[j][2]]
                # ['2021.11.02', '2022.7.01', '2022.5.19', '2022.5.20']
                print(temp)
                new_privacies_temp[j] = ".".join(map(str, temp))

    # 오늘 날짜와 비교하기
    for i in range(len(new_privacies_temp)):
        if today >= new_privacies_temp[i]:
            answer.append(i+1)

    return answer
