n=8
for i in range(n):
    user_search_value =input('enter the number ')

    count = 0    

    with open('keydistribution.txt', 'r') as f:
        for word in f.readlines():
            words = word.lower().split()
            if user_search_value in words:
                count += 1
    print (count)
