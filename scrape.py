import requests
import os

if not os.path.exists('pdfs'):
    os.makedirs('pdfs')

base_url = 'https://www.ysk.gov.tr/doc/dosyalar/docs/24Haziran2018/KesinSecimSonuclari/'

# Make a GET request to the base URL
response = requests.get(base_url)

# Find all the links to the PDF files on the page
pdf_links = ['Adana','Adiyaman','Afyonkarahisar','Agri','Amasya','Ankara1','Ankara2','Ankara3','Antalya','Artvin','Aydin','Balikesir','Bilecik','Bingol','Bitlis','Bolu','Burdur','Bursa1','Bursa2','Canakkale','Cankiri','Corum','Denizli','Diyarbakir','Edirne','Elazig','Erzincan','Erzurum','Eskisehir','Gaziantep','Giresun','Gumushane','Hakkari','Hatay','isparta','Mersin','istanbul1','istanbul2','istanbul3','izmir1','izmir2','Kars','Kastamonu','Kayseri','Kirklareli','Kirsehir','Kocaeli','Konya','Kutahya','Malatya','Manisa','Kahramanmaras','Mardin','Mugla','Mus','Nevsehir','Nigde','Ordu','Rize','Sakarya','Samsun','Siirt','Sinop','Sivas','Tekirdag','Tokat','Trabzon','Tunceli','Sanliurfa','Usak','Van','Yozgat','Zonguldak','Aksaray','Bayburt','Karaman','Kirikkale','Batman','Sirnak','Bartin','Ardahan','igdir','Yalova','Karabuk','Kilis','Osmaniye','Duzce']

# Loop through the PDF links and download each file
for link in pdf_links:
    pdf_url = base_url + link + '.pdf'
    print('Downloading:', pdf_url)
    file_name = link.split('/')[-1]
    response = requests.get(pdf_url)
    with open('pdfs//'+file_name+'.pdf', 'wb') as f:
        f.write(response.content)
