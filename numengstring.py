def solution(s):
    answer = ''
    word = '' #word에 영단어들을 따로 넣는다 
    eng = { 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 
           'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0' }
     
    for w in s : 
        #isdigit으로 판별하여 숫자면 answer에 추가
        if w.isdigit() :
            answer += w
            
        #숫자가 아니면 word에 알파벳을 한개씩 넣고
        else :
            word += w
            #word에 eng와 일치하는 key가 있으면 해당 value값을 answer에 추가
            if word in eng.keys() : 
                answer += eng[word]
                word = ''
                
    return int(answer)