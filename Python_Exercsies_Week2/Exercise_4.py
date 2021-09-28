nmbr = int(input("Number : "))
if nmbr<1:
    print(nmbr,"Not Prime")
else: 
    for i in range(2, nmbr):
        if(nmbr%1) == 0: print(nmbr,"Not Prime")
        break
    else: 
        print(nmbr, "Prime")