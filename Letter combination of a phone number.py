def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []
    
    phone = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    def backtrack(index, path):
        if index == len(digits):
            combinations.append(''.join(path))
            return
        
        for char in phone[digits[index]]:
            path.append(char)
            backtrack(index + 1, path)
            path.pop()
    
    combinations = []
    backtrack(0, [])
    return combinations

print(letterCombinations("23"))  
print(letterCombinations(""))    
print(letterCombinations("2"))   
