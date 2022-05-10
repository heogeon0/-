import re

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    strA = []
    strB = []
    # 1. 집합만들기
    exp = re.compile('[A-Z][A-Z]')
    for i in range(len(str1)-1):
        temp = str1[i] + str1[i+1]
        if exp.match(temp):
            strA.append(temp)

    for i in range(len(str2)-1):
        temp = str2[i] + str2[i+1]
        if exp.match(temp):
            strB.append(temp)

    # 2. 합집합/교집합구하기
    union = []
    inter = []
    stand = list(set(strA+strB))
    for st in stand:
        if st in strA and st in strB:
            union.extend([st]*max(strA.count(st), strB.count(st)))
            inter.extend([st]*min(strA.count(st), strB.count(st)))

    for st in strA + strB:
        if st not in inter:
            union.append(st)

    # 3. 자카드계수 구하기
    if len(union) == 0:
        return 65536
    return int((len(inter)/len(union) * 65536) // 1)


solution('E=M*C^2', 'e=m*c^2')


