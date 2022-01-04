import csv, json
import os.path
import pandas as pd
from csv import writer
from tabulate import tabulate

class FileTool:
    def __init__(self, path, fields = []):
        self.path = path
        self.fields = fields

    def showfile(self):
        with open(self.path, "r", encoding="UTF-8") as f:            
            print(tabulate(f))
        return self.path       
    
    def create_file(self):        
        check = os.path.exists(self.path)
        if check:
            print("İşlem yapmak istediğiniz dosya sistemde mevcut.")
        else:
            print("İşlem yapmak istediğiniz dosya oluşturuldu.")
            with open(path, 'w', encoding='utf-8') as file:
                writer = csv.writer(file)
                fields = [i for i in input("Enter the list of fields: ").split()]
                writer.writerow(fields)                

    def csv_to_json(self):
        df = pd.read_csv(self.path,sep = ";")        
        df = df.reset_index().to_json(path.replace(".csv", ".json"), orient='records')        
        print("İstediğiniz dosya JSON formatına dönüştürüldü.")

    def search(self):         
        search_ = input("Aramak istediğiniz sözcüğü giriniz: ")
        with open(self.path, 'r') as f:
            for line in f.readlines():
                if search_ in line:
                    print(line)

    def add(self):
        txt = [i for i in input("Lütfen eklemek istediğiniz veriyi yazınız: ").split("\n")]
        with open(self.path, 'a', newline='') as f:  
            writer_object = writer(f)
            writer_object.writerow(txt)  
            f.close()

    def delete(self):        
        deleted_ = input("Silmek istediğiniz veriyi giriniz: ")
        with open(self.path, 'r+') as f:
            lines = f.readlines()
            for line in lines:
                if line.strip("\n") != deleted_:
                    f.write(line)

    ############## Buna bak olm çalıştıramadın bunu###############
    def update(self):
        df = pd.read_csv(self.path)
        print(df)
        df.replace('{}'.format(input("Eski veri: ")),'{}'.format(input("Yeni veri: ")), inplace=True)
        return df    
    
#    def merge_file(self):          
#        with open(self.path, 'r') as f1:
#            original = f1.read()
#
#        with open(self.path, 'a') as f2:
#            f2.write('\n')
#            f2.write(original)

    def Menu(self):
        print("Lütfen aşağıdaki menüden bir seçim yapınız.")        
        while True:
            select_ = input("""
1- Ara,
2- Ekle,
3- Sil,
4- Güncelle,
5- Yeni "csv" dosyası oluştur,
6- "csv" dosyasını "json" dosyasına dönüştür,
7- Dosyayı göster,
8- Çıkış yap

Gerçekleştirmek istediğiniz işlemin başındaki numarayı yazınız: """)
            if select_ == '1':
                self.search()
            elif select_ == '2':
                self.add()
            elif select_ == '3':
                self.delete()
            elif select_ == '4':
                self.update()
            elif select_ == '5':
                self.create_file()
            elif select_ == '6':
                self.csv_to_json()
            elif select_ == '7':
                self.showfile()
            elif select_ == '8':
                break
            else:
                print("Geçersiz veri girişi!!!")

path = input("İşlem yapmak istediğiniz dosyanın adını giriniz: ")
FileTool(path).Menu()