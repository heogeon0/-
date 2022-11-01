from itertools import combinations


def solution(relation):
    answer = 0
    # 완전탐색?
    cnt = 0
    columns_cnt = len(relation[0])
    columns = range(0, columns_cnt)
    min_list = []
    answer = 0
    for i in range(1, columns_cnt + 1):
        test = list(combinations(columns, i))
        # 유일성 검사
        for item in test:
            one_test = set()
            for row in range(len(relation)):
                temp_list = []
                for col in item:
                    temp_list.append(relation[row][col])

                one_test.add(tuple(temp_list))

            if len(one_test) == len(relation):
                min_list.append(set(item))

    # 유일성 통과한 경우 최소성 검사
    min_list.sort(key=lambda x: len(x), reverse=True)
    while min_list:
        now = min_list.pop()
        answer += 1
        print(now)

        for i in range(len(min_list) - 1, -1, -1):
            print('here1', min_list[i] & now)
            if (min_list[i] & now) == now:
                print('here', min_list.pop(i))
    print(answer)
    return answer