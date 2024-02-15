import math
room_num = input()
plastic = [0]*10

for i in range(10):
  plastic[i] = room_num.count(str(i))

plastic[6] = math.ceil((plastic[9] + plastic[6])/2)
plastic[9] = 0

print(max(plastic))