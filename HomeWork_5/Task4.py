# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

line = 'AAAAAAAABCCCCAAAAANNNN'
rle_list = []

for i in list(line):
    if len(rle_list) == 0 or rle_list[-1][0] != i:
        rle_list.append([i, 1])
    else:
        rle_list[-1][1] += 1

rle_str = list(map(lambda x: f'{x[1]}x{x[0]}', rle_list))

print(rle_str)
