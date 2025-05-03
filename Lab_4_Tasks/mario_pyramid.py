def mario_pyramid(height):
    for i in range(1,height+1):
        print(' '*(height-i), '*'*i)

def mario_pyramid_lsit(height):
    pyramid = []

    for i in range(1,height+1):
        row = []
        row.append(' ' * (height-i) + '*' * i)
        pyramid.append(row)

    for rows in pyramid:
        print(rows)