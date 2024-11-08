import csv

def profile():
    file1 = open("music.csv",'a')
    w = csv.writer(file1)
    L = []
    profile = ['username','date joined' ,'usage','genre']
    c = input("Do you wish to create a profile:")
    if c in 'yY':
        username = input("enter your name:")
        p = [username,'','','']
        file2 = open("music.csv",'r')
        read = csv.reader(file2)
        for i in read:
            L.append(i[0])
        if username in L:
            print ("user already exists")
        else :
            w.writerow(p)































































 
































































































