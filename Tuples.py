if __name__ == '__main__':
    n = int(input())
    integer_list =list (map(int, input().split()))
    for i in range (n):
            x=tuple(integer_list)
            
    print(hash(x))
  
