def counting_vowles(sentence):
    vowles = 0
    for i in sentence:
        if i in "aeiou":
            vowles += 1
    print("Number of Vowles is: ", vowles)
    return vowles

def finding_i_index(sentence):
    for i in range(len(sentence)):
        if sentence[i] == 'i':
            print ("Found i at Index:", i)
    return i

def mult_table (t_size):
    for i in range(1, t_size+1):
        for j in range(1, i+1):
            print(i , " x ", j, " = ", i*j)
        print("===================================")

def mario_pyramid(height):
    for i in range(1,height+1):
        print(' '*(height-i), '*'*i)

def sort_array(Num_list):
    print(f"Ascending Order: {sorted(Num_list)}")
    print(f"Descending Order: {sorted(Num_list, reverse=True)}")

def mult__table_list(number):
    mult_table = []

    for i in range(1, number+1):
        row = []
        for j in range(1, i+1):
            row.append(i*j)
        mult_table.append(row)

    print(f"Multiplication Table: {mult_table}")

def user_info(name, email):

    if(name.strip() == ""):
        print("Invalid Input, You entered an empty entry.")
    elif(not name.isalpha()):
        print("Invalid Input, Please enter alphapetic character only.")

    if('@' not in email or "." not in email):
        print("Invalid Input, Please enter a valid email containing @ and .")
    else:
        parts = email.split('@')
        if len(parts) == 2:
            user = parts[0]
            domain = parts[1].split('.')
            if len(domain) == 2:
                service = domain[0]
                org = domain[1]
                if user and service and org:
                    print(f"Hello {name}, this is your email address {email}")
            else:
                print("The '.' should be after the '@'")
        else:
            print("The Email format should be (name@service.organization)")


def mario_pyramid_lsit(height):
    pyramid = []

    for i in range(1,height+1):
        row = []
        row.append(' ' * (height-i) + '*' * i)
        pyramid.append(row)

    for rows in pyramid:
        print(rows)

def user_login(in_user, in_pass):
    users = [{"michael": "pass123"}, {"omar": "qwerty"},{"maria": "abc123"}]

    user_found = None
    for user in users:
        if in_user in user:
            user_found = user
            break

    if user_found:
        if user_found[in_user] == in_pass:
            print(f"Welcome, {in_user}!")
        else:
            print("Incorrect password.")
    else:
        print("Username not found.")