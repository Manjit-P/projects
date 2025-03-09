a = [1, 2, 3, 4, 5, 6,7, 8, 9, 10]
key = int(input("Enter a key value you wanna search "))
mid = int(len(a)//2)
exit = True
while exit:
    if(a[mid] == key):
        print(f"found at index  {mid}")
        exit = False
    elif(a[mid] > key):
        mid -= 1
    else:
        mid += 1