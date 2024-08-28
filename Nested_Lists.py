

if __name__ == '__main__':
    records = []
    for i in range(int(input())):
        name = input( )
        score = float(input())
        records.append([name, score])
    
    min_score = min(record[1] for record in records)
    
    filtered_records = [record for record in records if record[1] != min_score]
    second_min_score = min(record[1] for record in filtered_records)
    
    # Collect names with the second minimum score
    lst = [record[0] for record in filtered_records if record[1] == second_min_score]
    
    # Sort and print the names
    lst.sort()
    print(*lst, sep='\n')
        
    
