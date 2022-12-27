#дан списко a = [4, 3, -10, 1, 7, 12],
# изменить его а=[4, -10, 12, 3, 1, 7]

#a= [4, 3, -10, 1, 12]
#a=input().split()
b=list(map(int, input().split()))
b.sort(key=lambda x: x%2)

print(b)