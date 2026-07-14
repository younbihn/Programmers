def solution(array, commands):
    answer = []
    for nums in range(len(commands)):
        i = commands[nums][0]
        j = commands[nums][1]
        k = commands[nums][2]
        
        temp_array = array[i-1:j]
        
        temp_array.sort()
        
        answer.append(temp_array[k - 1])
    return answer