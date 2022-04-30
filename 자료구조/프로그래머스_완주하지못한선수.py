my_dict = dict()
def solution(participant, completion):
    for name in participant:
        if my_dict.get(name):
            my_dict[name] += 1
        else:
            my_dict[name] = 1

    for name in completion:
        my_dict[name] -= 1
        if my_dict[name] == 0:
            my_dict.pop(name)

    return my_dict.popitem()[0]



def solution(participant, completion):

