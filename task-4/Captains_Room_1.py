K = int(input())
room_num = list(map(int, input().strip().split()))

room_count = {}
for i in room_num:
    if i in room_count:
        room_count[i] += 1
    else:
        room_count[i] = 1

for i, count in room_count.items():
    if count == 1:
        print(i)
        break
