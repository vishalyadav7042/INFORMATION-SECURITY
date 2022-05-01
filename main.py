# ceaser cipher encryption
print("CEASER CIPHER ENCRYPTION")
TEXT=input("enter the text : ")
KEY=int(input("enter the key value : "))
newtext=""
for i in TEXT:
    if i.isupper():
        newtext+=chr((ord(i)+KEY-65)%26+65)
    elif (ord(i)==32):
        newtext+=chr(ord(i))
    else:
        newtext+=chr((ord(i)+KEY-97)%26+97)
print("Cipher Text : ",newtext)
print("-----------------------------------------------------------------------------------------------------------")

# Rail Fence cipher encryption
print("RAIL FENCE ENCRYPTION")
plaintext=input("enter the plain text : ")
key=int(input("enter the key value : "))
text=plaintext.upper()
matrix=[[" " for x in range(len(plaintext))] for y in range(key)]
flag=0
row=0
for i in range(len(text)):
  matrix[row][i]=text[i]
  if row==0:
    flag=0
  elif row==key-1:
    flag=1
  if flag==0:
    row+=1
  else:
    row-=1
for i in range(key):
    "".join(matrix[i])
ciphertext=[]
for i in range(key):
    for j in range(len(text)):
        if matrix[i][j]!=' ':
            ciphertext.append(matrix[i][j])
cipher="".join(ciphertext)
print("Cipher Text: ",cipher)
print("-----------------------------------------------------------------------------------------------------------")

# Ceaser Cipher Decryption
print("CEASER CIPHER DECRYPTION")
Cipher_text=input("enter the encrypted text : ")
key =int(input("enter tyhe key value : "))
Plain_text=""
for i in Cipher_text:
    if i.isupper():
        Plain_text+=chr((ord(i)-key-65)%26+65)
    elif(ord(i)==32):
        Plain_text+=chr(ord(i))
    else:
        Plain_text+=chr((ord(i)-key-97)%26+97)
print("Plain Text : ",Plain_text)
print("-----------------------------------------------------------------------------------------------------------")

# Rail Fence Cipher Decryption
print("RAIL FENCE CIPHER DECRYPTION")


# rail fence cipher decryption
def decryptRailFence(cipher, key):
    # create the matrix to cipher
    # plain text key = rows ,
    # length(text) = columns
    # filling the rail matrix to
    # distinguish filled spaces
    # from blank ones
    rail = [ [ ' ' for i in range ( len ( cipher ) ) ]
             for j in range ( key ) ]

    # to find the direction
    dir_down = None
    row, col = 0, 0

    # mark the places with '*'
    for i in range ( len ( cipher ) ):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        # place the marker
        rail [ row ] [ col ] = '*'
        col += 1

        # find the next row
        # using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1

    # now we can construct the
    # fill the rail matrix
    index = 0
    for i in range ( key ):
        for j in range ( len ( cipher ) ):
            if ((rail [ i ] [ j ] == '*') and
                    (index < len ( cipher ))):
                rail [ i ] [ j ] = cipher [ index ]
                index += 1

    # now read the matrix in
    # zig-zag manner to construct
    # the resultant text
    result = [ ]
    row, col = 0, 0
    for i in range ( len ( cipher ) ):

        # check the direction of flow
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        # place the marker
        if (rail [ row ] [ col ] != '*'):
            result.append ( rail [ row ] [ col ] )
            col += 1

        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    return ("".join ( result ))


# Driver code

cipher = input ( "enter the cipher text : " )
key = int ( input ( "enther the key value : " ) )
print ( decryptRailFence ( cipher, key ) )


print("-----------------------------------------------------------------------------------------------------------")
