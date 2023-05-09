from pdfminer.high_level import extract_text
import os
import csv

partiler =  ['ADALET VE KALKINMA PARTİSİ',
            'MİLLİYETÇİ HAREKET PARTİSİ',
            'HÜR DAVA PARTİSİ',
            'VATAN PARTİSİ',
            'HALKLARIN DEMOKRATİK PARTİSİ',
            'CUMHURİYET HALK PARTİSİ',
            'SAADET PARTİSİ',
            'İYİ PARTİ',
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
            start = data.find('SİYASİ PARTİ ADI', start + 1)
        end = data.find('KAZANDIĞI MİLLETVEKİLİ SAYISI')
        vekilcikaranlar = data[start+17:end-2].split('\n')
        nend = end
        for i in range(len(vekilcikaranlar)+1):
            nend = data.find('\n', nend + 1)
        vekilsayisi = data[end+30:nend].split('\n')
        print(vekilcikaranlar, vekilsayisi)

        a = data.find('SİYASİ PARTİ ADI')
        b = data.find('ÇEVRE OYU')
        adaylar = data[a+17:b-2].split('\n\n')
        start = b
        while(data.find('TOPLAM', start) != -1):
            start = data.find('TOPLAM', start + 1)
            if data[start+7] in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                break
        
        nend = start
        for i in range(len(adaylar)*2):
            nend = data.find('\n', nend + 1)

        oylar = data[start+7:nend].replace('.', '').split('\n\n')
        print(adaylar, oylar)

        i = 0
        iother = 0
        parti_data = {}
        for parti in partiler:
            deputy = 0
            if parti in adaylar:
                vote = int(oylar[i])
                if parti in vekilcikaranlar:
                    deputy = int(vekilsayisi[iother])
                    iother += 1
                i += 1
                str = (deputy / vote) / (600 / 50137175) if vote != 0 else 0
                parti_data[parti] = {"vote": vote, "deputy": deputy, "str": str}
        results[filename[:-4]] = parti_data

with open(output_file, "w", newline="", encoding="UTF-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for province, party_data in results.items():
        for party_name, party_stats in party_data.items():
            row = [province, party_name, party_stats["vote"], party_stats["deputy"], party_stats["str"]]
            writer.writerow(row)
