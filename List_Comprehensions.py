if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    return_list=[]
    for i in range(x +1):
        for j in range(y + 1):
            for k in range(z + 1):
                if (i+j+k) != n:
                    return_list.append([i, j, k])
    print(return_list)
