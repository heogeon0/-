ok = ['-','_','.']


def solution(new_id):
    id = new_id.lower()
    stack = []

    for char in id:
        # 2단계 & 3단계
        if char.isalpha() or char.isdecimal() or char in ok:
            if char == '.' and stack:
                if stack[-1] == '.':
                    continue
            stack.append(char)

    # 4단계
    if stack and stack[0] == '.':
        stack.pop(0)
    elif stack and stack[-1] == '.':
        stack.pop()

    # 5단계
    if not stack:
        stack.append('a')

    # 6단계
    stack = stack[:15]
    if stack[-1] == '.':
        stack.pop()

    # 7단계
    while len(stack) < 3:
        stack.append(stack[-1])

    answer = ''.join(stack)

    return answer

print(solution("...A..-.,_BCD..E.."))