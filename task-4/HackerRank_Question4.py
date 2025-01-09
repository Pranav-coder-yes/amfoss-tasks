def count(S):
    frequency = [0] * 10
    
    for char in S:
        if char.isdigit():
            frequency[int(char)] += 1

    for i in frequency:
        print(i,end=" ")

S = input()
count(S)
