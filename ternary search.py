def ternarysearch(l,r,key,a):
    mid1 = l + (r-l)//3
    mid2 = r - (r-l)//3
    if(a[mid1]==key):
        print({mid1})
    if(a[mid2]==key):
        print({mid2})
    elif(a[mid2] < key):
        ternarysearch(mid2 + 1,r,key,a)
    elif(a[mid1] > key ):
        ternarysearch(l,mid1 - 1,key,a)
    else:
        ternarysearch(mid1 - 1,mid2 + 1,key,a)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
key = int(input("Enter a key value you wanna search "))
l = 0
r = len(a) - 1
ternarysearch(l,r,key,a)