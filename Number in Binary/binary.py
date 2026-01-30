def convert_to_binary(number:int):
    binary=""
    if number<0:
        sign = "1"
        number = abs(number)-1
    else:
        sign = "0"
    if number ==0:
        return sign+"0000000"
    while number !=0:
        rem=number%2
        number=number//2
        binary = f"{rem}"+binary
    bits = len(binary)
    
    if bits <=7:
        binary= (7-bits)*"0"+binary
    elif bits <=15:
        binary= (15-bits)*"0"+binary
    elif bits <=31:
        binary= (31-bits)*"0"+binary

    if sign =="1": # -13 -> "1" 13-1 = 12-> binary ->  1111 -> "1" + binary
        flip = ""
        for i in range(len(binary)):
            if binary[i]=="0":
                flip+="1"
            elif binary[i]=="1":
                flip+="0"
        binary = flip
    return sign+binary



print(convert_to_binary(192)) # 16-bits
print(convert_to_binary(-5)) # 8 bits negative
print(convert_to_binary(0)) # 0 
