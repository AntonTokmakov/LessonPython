mas = ["Орел", "Орел", "Орел", "Решка", "Решка"]
orel = 0

for coin in mas:
    if coin == "Орел":
        orel += 1

print(orel)
if orel > orel - len(mas):
    print(f"Перевернуть решку {len(mas) - orel}")
else:
    print(f"Перевернуть орлов {orel}")




# if c % a == 0 and c // a <= b or c % b == 0 and c // b <= a:
#     print("yes")
# else:
#     print("no")


# n = 385917
# n = str(n)
# part1 = 0
# part2 = 0
#
# for i in range(len(n)):
#     if i < len(n) / 2:
#         part1 += int(n[i])
#     if i >= len(n) / 2:
#         part2 += int(n[i])
#
# if part1 == part2:
#     print("yes")
# else:
#     print("no")

# n = 120
# p = 0
#
# for i in range(n):
#     if i * 2 * 2 == (i * 2 - n) * -1:
#         print(i)
#         p = i
#         break
#
# s = p
# k = (p + s) * 2
#
# print(f"{p} {k} {s}")
