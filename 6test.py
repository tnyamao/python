#shell-Sort
def sort(data):
    gaps = [7, 3, 1]
    for gap in gaps:
        for i in range(0, len(data), gap):
            for j in range(i-gap, 0, -gap):
                if data[j] > data[j+gap]:
                    data[j], data[j+gap] = data[j+gap], data[j]
                    print("gap:", gap, "data[j]", data[j], "data[j+gap]", data[j+gap])
                else:
                    break
data = [1, 3, 2, 5, 4, 2, 1]
print("Befor: ", data)
sort(data)
print("Aftor: ", data)