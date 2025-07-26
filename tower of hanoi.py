def hanoi(n,a,b,c):
    if n == 1:
        print(f"Move the first disk from rod {a} to rod {b}")
        return
    
    hanoi(n-1,a,c,b)
    print(f"Move the disk {n} from rod {a} to rod {b}")
    hanoi(n-1,c,b,a)
    print(f"Move the disk {n} from rod {a} to rod {b}")
    
n = 6
hanoi(n,'A', 'B', 'C')