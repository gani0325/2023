# 하루 동안 근무한 시간은 출근 시각과 퇴근 시각 사이의 시간
# 식사 시간 등 근무 외 시간을 근무 시간에서 제외하지 않음

# 월요일부터 금요일까지 휴가를 쓰지 않은 직원이
# 매 요일 언제 출근하고 언제 퇴근했는지가 주어질 때,
# 5일 동안 총 몇 분을 근무했는지를 구하는 프로그램을 작성하라.

import sys

input = sys.stdin.readline

# ":"를 기준으로 h, m 나누기
table = []
for _ in range(5):
    start, end = input().split()
    table.append((start, end))

total_answer = 0
for h, m in table:
    s_h, s_m = h.split(":")
    e_h, e_m = m.split(":")

    s_h = int(s_h)
    s_m = int(s_m)
    e_h = int(e_h)
    e_m = int(e_m)

    if e_m >= s_m:
        answer_h = e_h - s_h
        answer_m = e_m - s_m
    else:
        answer_h = e_h - 1 - s_h
        answer_m = e_m + 60 - s_m

    total_answer += answer_h * 60 + answer_m
print(total_answer)
