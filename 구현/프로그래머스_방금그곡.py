
def hourtomin(time):
    hh, mm = time.split(':')
    time = int(hh) * 60 + int(mm)
    # 처음에 re를 이용해서 구했는데 계속 런타임 에러나서 맵핑으로 바꿔봤지만 그래도 에러가 나서 진짜 멘탈이
    # 나갔습니다. 질문하기에 모든 테케를 돌려보았지만 정답은 나와서 진짜 너무화났었는데
    # int(hh*60)이 에러를 만들었습니다. 왜 시간이 같은값일때는 오류안나다가 12:04 , 13:04를 비교하면 오류나는지
    # 모르겠습니다. 다른분들도 조심하기 바랍니다
    return time

def convert(content):
    ohno = {
        'C#' : 'c',
        'D#' : 'd',
        'F#' : 'f',
        'G#' : 'g',
        'A#' : 'a',
        'B#' : 'b',
    }
    for k in ohno.keys():
        content = content.replace(k,ohno[k])
    return content

def solution(m, musicinfos):
    answer = []
    m = convert(m)
    for music in musicinfos:
        idx = 0
        st, et, title, contents = music.split(',')
        # 시간 구하기
        run_time = hourtomin(et) - hourtomin(st)

        # 악보변환
        contents = convert(contents)
        run_song = len(contents)

        if run_time > run_song:
            na = run_time % run_song
            new_con = contents * int(run_time // run_song)
            new_con += contents[:na]

        else:
            new_con = contents[:run_time]

        if new_con.find(m) != -1:
            answer.append([idx,run_time,title])
        idx += 1

    if answer:
        answer.sort(key=lambda x:(-x[1],x[0]))
        return answer[0][2]
    return "(None)"


# print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC",["12:00,13:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("A#AB#", ["13:00,13:01,HAPPY,B#A#A"]))
# print(solution("C", ["13:00,13:01,WORLD,F"]))
# print(solution("CCB", ["03:00,03:04,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"]))