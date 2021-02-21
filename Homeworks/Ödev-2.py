ogrenciAdiSoyadi=["Ali Akyol","Veli Gün","Selim Can","Ali Can","Ahmet Çalış"]
midterm = [30,50,40,40,70]
final = [70,90,100,50,75]
hw = [100,90,100,100,50]

puanlar={}

i=0
while i<5:
  anahtar=ogrenciAdiSoyadi[i]
  puanlar[anahtar]=[int(sum([midterm[i],final[i],hw[i]])/3)]
  i+=1

#print(puanlar)

#{k: v for k, v in sorted(puanlar.items(), key=lambda item:item[1])}

sorted_puanlar=sorted(puanlar.items(),key=lambda kv:kv[1],reverse=True)

#dict(sorted(puanlar.items(), key=lambda item:item[1]))

#print(sorted_puanlar)

print(f"{sorted_puanlar[0][0]} adlı arkadaşımızı tebrik ediyoruz. {sorted_puanlar[0][1]} puan ile sınıfı birincilikle bitirdi. Helal olsun.")

