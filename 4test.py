def sort(data):
    for i in range(0, len(data)):
        for j in range(i-1, -1, -1):
            print("j : ", data[j])
            print("i : ", data[i])
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
            else:
                break

data = [4,6,7,2,8,7,9,1]
print("Befor :", data)
sort(data)
print("Aftor :", data)
