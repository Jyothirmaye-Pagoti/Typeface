lst = input().split(',')
print(lst)
str1=lst[0]
str2=lst[1]
k=str2[len(str2)-1]
count=0
for i in range(len(str1)):
    if(str1[i]==k):
        count+=1
print(count)
    
