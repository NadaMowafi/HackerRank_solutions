n = int(input())
for i in range (n):
    try:
        a , b= input().split()
        c= int(a)//int(b)
        print(c)
    except Exception as e :
        print(f"Error Code: {e}")         
