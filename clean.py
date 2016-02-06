f = open('realDonaldTrump.txt')
f1 = open('realDonaldTrump1.txt','w')
for i in f :

	j = i.strip().replace('"','').replace("'","")
	j = str(filter(lambda x:ord(x)>31 and ord(x)<128,j)).strip().lower()
	f1.write(j+'\n')