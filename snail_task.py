h = 5
up = 3
down = 2

count = 1
snail_h = 0

# while h > 0:
#     h -= up
#     count += 1
#     if h == 0:
#         break
#     h += down

# while snail_h < h:
#     snail_h += up
#     count += 1
#     if snail_h >= h:
#         break
#     snail_h -= down

# for i in range(100):
#     if h - up - i * (up - down) <= 0 :
#         count = i + 1
#         break

while h - up - count * (up - down) > 0:
    count += 1

print(count + 1)
