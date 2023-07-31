data = [4, 2, 3, 5, 1]

for i in range(len(data)):
    for y in range(len(data) - 1, i, -1):
        if data[y] < data[y - 1]:
            data[y], data[y - 1] = data[y - 1], data[y]
        print(data)

print(data)