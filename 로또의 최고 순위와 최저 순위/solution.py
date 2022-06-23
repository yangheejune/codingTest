def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

"""
내가 짠거와 비교....
def solution(lottos, win_nums):
    answer = []
    max_result = 0
    min_result = 0
    
    for lotto in lottos:
        if lotto in win_nums:
            max_result += 1
        
        if lotto == 0:
            min_result += 1
            
    if max_result + min_result == 6:
        answer.append(1)
    elif max_result + min_result == 5:
        answer.append(2)
    elif max_result + min_result == 4:
        answer.append(3)
    elif max_result + min_result == 3:
        answer.append(4)
    elif max_result + min_result == 2:
        answer.append(5)
    elif max_result + min_result < 2:
        answer.append(6)
    
    if max_result == 6:
        answer.append(1)
    elif max_result == 5:
        answer.append(2)
    elif max_result == 4:
        answer.append(3)
    elif max_result == 3:
        answer.append(4)
    elif max_result == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    return answer
"""
if __name__ == "__main__":
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]

    print(solution(lottos, win_nums))