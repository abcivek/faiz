def faiz(miktar, oran, ekle, sure):
	tmp = miktar
	oran=oran/12.  
	print "Aylık faiz: ", oran*10, "TL"
	for i in range(sure):
		miktar=miktar+miktar*oran/100
		print  i+1, ". ay toplam: ", int(miktar), "TL"
		miktar = miktar + ekle
	if ekle==0:
		faiz = int(miktar-tmp)
	else:
		faiz = int(miktar-ekle*(sure+1))
	print "kazanılan faiz: ", faiz, "TL"


# örneğin, her ay bankaya 1000 tl atsam, yıllık %6 faizden 12 ay sonunda kazanacağım faiz ne olur? (faiz(1000, 6, 1000, 12))
