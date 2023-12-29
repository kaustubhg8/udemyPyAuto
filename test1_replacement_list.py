lst1 = ['hi kg','hello kaustubh','Nexus_environment=dev','kg']
n = None
for a in lst1:
    if a.find('Nexus_environment')== 0:
        print(a)
        n = lst1.index(a)
        print(n)

lst1.pop(n)
lst1.append('Nexus_environment=qa')
print(lst1)
str2=''
for a in lst1:
    str2 = str2 + '\n' + a


print(str2)