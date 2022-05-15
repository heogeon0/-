import math
def solution(fees, records):
    base_time = fees[0]
    base_fee = fees[1]
    time = fees[2]
    fee = fees[3]

    fee_record = {}
    max_time = 23 * 60 + 59
    for record in records:
        record_lst = record.split()
        record_time, record_num = record_lst[0], record_lst[1]
        HH, MM = map(int,record_time.split(':'))
        num_time = HH*60 + MM
        if record_lst[2] == 'IN':
            try:
                fee_record[record_num] += max_time - num_time
            except:
                fee_record[record_num] = max_time-num_time
        else:
            fee_record[record_num] -= (max_time - num_time)
    answer = []
    for re in sorted(fee_record.items()):
        ans = math.ceil((re[1] - base_time)/time) * fee + base_fee if re[1] > base_time else base_fee
        answer.append(ans)

    return answer

solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])