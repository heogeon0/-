from collections import Counter
def solution(enroll, referral, seller, amount):
    parent_dict = dict(zip(enroll,referral))
    earning_dict = dict(zip(enroll,[0]*len(enroll)))


    for i in range(len(seller)):
        earing = amount[i] * 90
        giving = amount[i] * 10
        earning_dict[seller[i]] += earing

        parent = parent_dict[seller[i]]
        while parent != '-' and giving > 0:
            earing = giving - (giving // 10)
            giving //= 10
            earning_dict[parent] += earing
            parent = parent_dict[parent]

    answer = []
    for name in enroll:
        answer.append(earning_dict[name])

    return answer


solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
         ,["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10])