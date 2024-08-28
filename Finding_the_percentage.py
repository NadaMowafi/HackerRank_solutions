if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    max = 0
    for i in range (3):
         max= max+ student_marks [query_name][i] 
    average = max/3
    print (format(average , ".2f"))
