from random import choice;X='X';O='0'
b = [['·'for z in range(3)]for j in
range(3)];p=choice(['0','X']);H='·'
while True:
    print('\n'.join([''.join([l for l
in r])for r in b]));B=[''.join([''.join
([l for l in u]) for u in b])][0];c=[B
[c::3]for c in range(3)]+[B[r:r+3]for
r in range(0,9,3)]+[B[0]+B[4]+B[8]]+[B[
2]+B[4]+B[6]]
    if 3 in [z.count(O)for z
in c]:print("0 player won");break
    elif 3 in [z.count(X)for z in c]:
        print("X player won");break
    elif sum([z.count(H)for z in c])\
==0:print("draw");break
    i=input(f"{p}'s turn, enter coord("
"x,y):");i=i.split(',')
    if len(i)!=2:
        print("Invalid");continue
    try:i=[int(z)for z in i];
    except:
        print("Invalid");continue
    i=[int(z)for z in i]
    if b[i[1]-1][i[0]-1]!=H:print(
"Invalid move");continue
    if p==O:b[i[1]-1][i[0]-1]=O;p=O
    else:
        b[i[1]-1][i[0]-1]=X;p=X