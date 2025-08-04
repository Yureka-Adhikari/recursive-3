keypad = ["","", "ABC", "DEF", "GHI","JKL","MNO", "PQRS", "TUV", "WXYZ"]

def print_combinations(combinations, curr, output, n):
    if curr == n:
        print(*output, sep=",")
        return
    
    for i in range(len(keypad[combinations[curr]])):
        output.append(keypad[combinations[curr]][i])
        
        print_combinations(combinations, curr+1,output, n)
        output.pop()
        
        if combinations[curr] == 0 or combinations[curr] == 1:
            return 
        
combination = [4,3,1]
n = len(combination)
print_combinations(combination,0, [], n)