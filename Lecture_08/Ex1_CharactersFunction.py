def l1(a):
    i = 0
    count = 0

    while True:
        try:
            char = a[i]
            count += 1
            i += 1
        except IndexError:
            break
    if count == 1:
        print(f"{count} character is present in the given string")
    else:
        print(f"{count} characters are present in the given string")

a = input("Enter a string : ")
l1(a)