
def solution(word, pages):
    word = word.upper()
    N = len(pages)
    title_lst = []
    answer = [0]*N
    # 1 title 구하기
    for i in range(N):
        # title 다른방법으로 추출하기!! TC 9번은 실패
        title = pages[i].split('<head>')[1].split('\n')[2].split('"https://')[1].rstrip('\"/>')
        print(title)
        title_lst.append(title)

    # 2. 사이트별 body를 통해 기본점수 / 외부점수 구하기
    for i in range(N):
        body = pages[i].split('<body>')[1].split('</body>')[0].split('<')
        a_total = 0
        giving_link_score = [0] * N
        basic_score = [0] * N
        for line in range(len(body)):
            if body[line]:
                if body[line][0] != 'a':
                    # 1 text인 경우
                    text = '.' + body[line].upper() + '.'
                    for j in range(len(text)-len(word)):
                        if not text[j].isalpha():
                            if ''.join(text[j+1:j+len(word) +1]) == word and not text[j+len(word)+1].isalpha():
                                basic_score[i] += 1

                else:
                    # a태그 구하기
                    a_total += 1
                    a_key = body[line].split('//')[1].split('"')[0]
                    if a_key in title_lst:
                        giving_link_score[title_lst.index(a_key)] += 1

        answer[i] += basic_score[i]

        # 참조받은 사이트에 점수주기
        for idx in range(len(giving_link_score)):
            if giving_link_score[idx]:
                answer[idx] += basic_score[i] / a_total

    max_value = max_idx = 0
    for i in range(N):
        if answer[i] > max_value:
            max_idx = i
            max_value = answer[i]

    return max_idx


print(solution('muzi',["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))