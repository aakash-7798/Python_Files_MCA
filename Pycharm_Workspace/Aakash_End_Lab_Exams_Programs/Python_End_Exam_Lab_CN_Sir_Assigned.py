# ## Bit Stuffing
#
print("Bit Stuffing")
arry = list(input("Enter Data for Bit Stuffing -> "))

def BitStuffing(arry):
    i,j=0,5
    while i<len(arry) and j<len(arry):
        if arry[i:j].count("1") == 5:
            arry.insert(j,'0')
            i = j
            j += 5
        else:
            i += 1
            j += 1
    return "01111110-"+''.join(arry)+"-01111110"

def Bit_Destuffing(arry):
    i,j=0,5
    while i<len(arry) and j<len(arry):
        if arry[i:j].count("1") == 5:
            arry.pop(j)
            i = j
            j += 5
        else:
            i += 1
            j += 1
    return "01111110-"+''.join(arry)+"-01111110"


# data-> 11000111111011111100

print("Data After Stuffing -> ",BitStuffing(arry))
print("Data After Destuffing -> ",Bit_Destuffing(arry))


print()
print("Byte Stuffing")

characters = list(input("Enter Character Set -> ").upper())
escp = input("Enter Escape Character : ")
flag = input("Enter Flag Character : ")

def Byte_Stuffing(characters,esp_char,flag_char):
    stuffed = []
    for i in characters:
        if esp_char in i or flag_char in i:
            stuffed.append(esp_char)
        stuffed.append(i)
    return ''.join(stuffed)

def Byte_Destuffing(lt,esc_char):
    try:
        ioe = lt.index(esc_char)
        return lt[:ioe] + [lt[ioe + 1]] + Byte_Destuffing(lt[ioe + 2:], esc_char)
    except:
        return lt

byte_stuffed = Byte_Stuffing(characters,escp,flag)
print("Characters After Stuffing -> ",byte_stuffed)
print("Characters After Destuffing -> ",''.join(Byte_Destuffing(list(byte_stuffed),escp)))


# characters = 'abcdefghijklmnopqrstuvwxyz'


