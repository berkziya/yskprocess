from pdfminer.high_level import extract_text
import os
import csv
import math

partiler =  ['MİLLET PARTİSİ',
            'HAK VE ÖZGÜRLÜKLER PARTİSİ',
            'TÜRKİYE KOMÜNİST PARTİSİ',
            'TÜRKİYE KOMÜNİST HAREKETİ',
            'SOL PARTİ',
            'GENÇ PARTİ',
            'MEMLEKET PARTİSİ',
            'BÜYÜK BİRLİK PARTİSİ',
            'ADALET VE KALKINMA PARTİSİ',
            'YENİDEN REFAH PARTİSİ',
            'MİLLİYETÇİ HAREKET PARTİSİ',
            'YEŞİLLER VE SOL GELECEK PARTİSİ',
            'TÜRKİYE İŞÇİ PARTİSİ',
            'ADALET BİRLİK PARTİSİ',
            'ANAVATAN PARTİSİ',
            'YENİLİK PARTİSİ',
            'HALKIN KURTULUŞ PARTİSİ',
            'MİLLİ YOL PARTİSİ',
            'VATAN PARTİSİ',
            'GÜÇ BİRLİĞİ PARTİSİ',
            'CUMHURİYET HALK PARTİSİ',
            'İYİ PARTİ',
            'ADALET PARTİSİ',
            'ZAFER PARTİSİ',
            'BAĞIMSIZLAR']

folder_path = ".//pdfs//"
output_file = "results.csv"
header = ["Province", "Political Party", "Votes", "Deputy", "Vote Strength"]
results = {}

for filename in os.listdir(folder_path):
    with open(os.path.join(folder_path, filename), 'rb') as f:
        data = extract_text(f)
        
        start = 0
        for i in range(2):
            start = data.find('SİYASİ PARTİ ADI', start + 1) + 49
        end = data.find('MİLLETVEKİLİ SEÇİLENLERİN AD-SOYADLARI İLE BAĞLI OLDUKLARI SİYASİ PARTİ / BAĞIMSIZ') - 2
        vekilcikaranlar = data[start:end].split('\n')[:math.floor(len(data[start:end].split('\n'))/2)]
        vekilsayisi = data[start:end].split('\n')[math.ceil(len(data[start:end].split('\n'))/2):]

        start = 0
        start = data.find('BAĞIMSIZLAR', start + 1)
        for i in range(54):
            start = data.find('\n', start + 1)
        end = data.find('SİYASİ PARTİ / BAĞIMSIZ ADAYLARIN KAZANDIKLARI MİLLETVEKİLİ SAYILARI')
        oylar = data[start+1:end-2].replace('.', '').split('\n')

        print(vekilcikaranlar, vekilsayisi)

        i = 0
        iother = 0
        parti_data = {}
        for parti in partiler:
            deputy = 0
            vote = int(oylar[i])
            if parti in vekilcikaranlar:
                deputy = int(vekilsayisi[iother])
                iother += 1
            i += 1
            str = (deputy / vote) / (600 / 54442588) if vote != 0 else 0
            parti_data[parti] = {"vote": vote, "deputy": deputy, "str": str}
        results[filename[:-4]] = parti_data

with open(output_file, "w", newline="", encoding="UTF-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for province, party_data in results.items():
        for party_name, party_stats in party_data.items():
            row = [province, party_name, party_stats["vote"], party_stats["deputy"], party_stats["str"]]
            writer.writerow(row)
