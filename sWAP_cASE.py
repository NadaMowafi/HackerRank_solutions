def swap_case(s):
    result =""
    for character in s:
        if ord(character) in range(65,91,1):
           result=result+(character.lower())
        elif ord(character) in range(97,123,1):
            result=result+(character.upper())
        else:
            result=result+character
            
    return result

