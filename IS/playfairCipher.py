ALPHABETS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def checkIJYZ(key):
    global ALPHABETS
    if 'I' in key or 'J' in key:
        ALPHABETS.remove('Z')
    if 'I' in key and 'Y' in key:
        ALPHABETS.remove('Z')
    else:
        ALPHABETS.remove('J')

def generateTable(key):
    global ALPHABETS
    table = [[None] * 5 for _ in range(5)]
    print(table)
    # append keys into the table
    i, j = 0, 0
    for char in key:
        table[i][j] = char
        if j == 4:
            i += 1
        j = (j + 1) % 5
    
    for char in ALPHABETS:
        if i == 4 and j == 4:
            break
        if char not in key:
            table[i][j] = char
            if j == 4:
                i += 1
            j = (j + 1) % 5
            
    keyAlpha = key + ALPHABETS
    
    for char in keyAlpha:
        

def main():
    key = list(input("Enter key: ").upper())
    text = input("Enter plain text: ")
    generateTable(key)
    # checkIJYZ(key)

if __name__ == '__main__':
    main()
