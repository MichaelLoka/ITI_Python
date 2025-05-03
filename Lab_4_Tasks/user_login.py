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