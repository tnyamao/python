def sort(data):
    #count = 1
    for i in range(0, len(data)-1):
        min_i = i
        for j in range(i+1, len(data)):
            # print("min_i :", data[min_i], "j : ", data[j], "i :", data[i])
            print("min:", data[min_i], "Target Value: ", data[j])
            if data[min_i] > data[j]:
                #print("min!:", data[j])
                min_i = j
            
                data[min_i], data[i] = data[i], data[min_i]
                #print("#.", count , "list: ", data)
                #count = count + 1


data = [4,6,7,2,8,7,9,1]
print("Befor :", data)
sort(data)
print("Aftor :", data)
