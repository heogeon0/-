import sys

n = int(input())
s = input()
result = -1 * sys.maxsize

cal = {
    "+" : lambda a,b: a+b,
    "-" : lambda a,b: a-b,
    "*" : lambda a,b: a*b
}

def dfs(index, value):
    global result

    if index == n - 1:
        result = max(result, value);
        return

    if index + 2 < n:
        dfs(index + 2, cal[s[index+1]](value, int(s[index +2])))

    if index + 4 < n:
        dfs(index + 4, cal[s[index + 1]](value, cal[s[index + 3]](int(s[index +2]),int(s[index +4]))))

dfs(0, int(s[0]))
print(result)