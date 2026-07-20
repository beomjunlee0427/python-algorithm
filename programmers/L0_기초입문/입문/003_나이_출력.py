# 나이 출력
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120820
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 20. 09:31:25

def solution(age):
    answer = 2022-age+1
    if age < 0 or age > 120:
        print("올바른 값을 입력하세요")
    return answer