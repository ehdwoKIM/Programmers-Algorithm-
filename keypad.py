def solution(numbers, hand):
    answer=''
    left = '*'
    right = '#'
    
    for number in numbers:
        # 1, 4, 7 이면 왼손
        if number in [1,4,7]:
            answer += 'L'
            left = number
        # 3, 6, 9 이면 오른손  
        elif number in [3,6,9]:
            answer += 'R'
            right = number
        # 가운데 2, 5, 8, 0 이면 finger함수 사용하여 return    
        else:
            fin = finger(number, left, right, hand)
            answer += fin
            if fin == 'L':
                left = number
            elif fin == 'R':
                right = number

    return answer
    
def finger(number, left, right, hand):
    # 손가락의 현 위치 => 딕셔너리 키패드 생성
    keypad = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2),
    }
    
    # (x1,y1), (x2,y2) 좌표 간 거리 |x1-x2| + |y1-y2|
    left_d = abs(keypad[number][0]-keypad[left][0]) + abs(keypad[number][1]-keypad[left][1])
    right_d = abs(keypad[number][0]-keypad[right][0]) + abs(keypad[number][1]-keypad[right][1])
    
    # 입력한 수의 키와 가까운 손가락 return
    if left_d < right_d :
        return 'L'
    elif right_d < left_d :
        return 'R'
    else:
        if hand == 'right':
            return 'R'
        elif hand == 'left':
            return 'L'