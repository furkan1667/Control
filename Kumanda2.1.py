import random
import time

class Kumanda():
    def __init__(self,tv_durumu="Kapalı",tv_ses=0,kanal_listesi=["Kanal D"],kanal="kanal D"):
        self.tv_durumu=tv_durumu
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
        
    def tv_aç(self):
        if(self.tv_durumu=="Açık"):
            print("Televizyon zaten açık amk....")
        else:
            print("Televizyon açılıyor....")
            self.tv_durumu="Açık"
            
    def tv_kapat(self):
        if(self.tv_durumu=="Kapalı"):
            print("Televizyon zaten kapalı amk...")
        else:
            print("Televizyon kapanıyor...")
            self.tv_durumu="Kapalı"
            
    def ses_ayarları(self):
        while 1==1:
            cevap=input("Sesi Azaltmak için(<): \nSesi Yükseltmek için(>): \nÇıkış Yapmak için(ç):")
            if(cevap=="<"):
                self.tv_ses-=1
                print("Ses Seviyesi:",self.tv_ses)
            elif(cevap==">"):
                self.tv_ses+=1
                print("Ses Seviyesi:",self.tv_ses)
            else:
                print("Ses Ayarından çıkış yapılıyor....")
                break
            
    def kanal_ekle(self,kanal_ismi):
        print("Yeni Kanal Ekleniyor....")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Yeni Kanal Eklendi...")
    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        print("Şuan ki kanal:",self.kanal)
        
    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "TV Durumu: {}\nTV Ses: {}\nKanal Listesi: {}\nŞuan ki Kanal: {}\n".format(self.tv_durumu,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda=Kumanda()

print("""
      KARDEŞİM ALDIN ELİNE KUMANDAYI NE YAPMAK İSTERSİN
      
      1.TV yi aç
      
      2.TV ti kapat
      
      3.Ses ayarları
      
      4.Kanal ekle
      
      5.Kanal sayısı
      
      6.Rastgele kanal seçme
      
      7.Televizyon bilgileri
      
      Çıkmak için 'q' tuşuna basınız....    """)
      
      
while 1==1:
    işlem=input("Lütfen Hangi İşlemi Yapmak İstediğinizi Belirtiniz:")
    
    if(işlem=="q"):
        print("Kumandayı baba eline aldı...")
        break
    elif(işlem=="1"):
        kumanda.tv_aç()
        
    elif(işlem=="2"):
        kumanda.tv_kapat()
    if(kumanda.tv_durumu=="Açık"):
        
        if(işlem=="3"):
            kumanda.ses_ayarları()
            
        elif(işlem=="4"):
            kanal_isimleri=input("Lütfen Eklemek İstediğiniz Kanalları Yazınız(kanallar arasında '-' işaretini koyunuz):")
            kanal_listesi=kanal_isimleri.split("-")
            for eklenecekler in kanal_listesi:
                kumanda.kanal_ekle(eklenecekler)
                
        elif(işlem=="5"):
            print("Kanal Sayısı:",len(kumanda))
    
        elif(işlem=="6"):
            kumanda.rastgele_kanal()        

        elif(işlem=="7"):
            print(kumanda)
    elif(işlem=="7"):
            print(kumanda)
    else:
        print("Geçersiz Bir İşlem Yaptınız....")
        
        

    
        
        
        
             
                