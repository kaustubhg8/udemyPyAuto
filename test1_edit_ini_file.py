from pathlib import Path

ini1 = Path('E:/TrainingKG/udemyPyAuto/files/DIGIMAT_Settings2.ini')
n = None
if ini1.exists():
    with open(ini1,'r') as file:
        str1 = file.read()
        lst = str1.split("\n")
        # print(lst.index("Nexus_environment=qa"))
        # str2 = str1.replace('Nexus_environment=dev','Nexus_environment=dev Kaudtubh Garud')
        for ele in lst:
            if ele.find('Nexus_environment')==0:
                n = lst.index(ele)
        lst.pop(n)
        lst.append('Nexus_environment=qa')
        str2 = ''
        for ele in lst:
            str2 = str2 + '\n' + ele


with open(ini1,'w') as file:
    file.write(str2)

