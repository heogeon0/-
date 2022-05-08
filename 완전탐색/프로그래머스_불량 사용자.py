import re
def solution(user_id, banned_id):
    def my_count(now):
        nonlocal cnt
        if now == N:
            tmp = sorted(check[:])
            if tmp not in my_answer:
                my_answer.append(tmp)
            return

        for str in candiates[now]:
            if str not in check:
                check.append(str)
                my_count(now+1)
                check.pop()
        else:
            return

    N = len(banned_id)
    candiates = [[] for _ in range(N)]
    for i in range(N):
        ban_id = banned_id[i]
        key = ''
        for char in ban_id:
            key += '.' if char == '*' else char
        exp = re.compile(key)

        for id in user_id:
            if len(ban_id) == len(id) and exp.match(id):
                candiates[i].append(id)

    cnt = 0
    check = []
    my_answer = []
    my_count(0)

    return len(my_answer)


solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"])