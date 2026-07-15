def solution(numbers):
    str_numbers = list(map(str, numbers))
    
    str_numbers.sort(key=lambda x: x * 3, reverse=True)
    
    if str_numbers[0] == '0':
        return '0'
        
    return ''.join(str_numbers)