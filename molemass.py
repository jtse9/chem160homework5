names=["H", "C", "N", "O","P","S"]
masses=[1.008,12.0107,14.00674,15.9994,30.973761,32.066]
Dict={}
for i in range(len(names)):
    Dict[names[i]]=masses[i]
Molec=input("Enter molecule string without spaces: ")
def molemass(x):
    mm = 0
    string=x
    alist=list(x)
    mm= sum([Dict[k] for k in alist])
    print (mm)