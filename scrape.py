import requests
import os

if not os.path.exists('pdfs'):
    os.makedirs('pdfs')

base_url = 'https://www.ysk.gov.tr/doc/dosyalar/docs/14Mayis2023/KesinSecimSonuclari/'

# Make a GET request to the base URL
response = requests.get(base_url)

# Find all the links to the PDF files on the page
pdf_links = ['ADANA','ADIYAMAN','AFYONKARAHISAR','AGRI','AMASYA','ANKARA-1','ANKARA-2','ANKARA-3','ANTALYA','ARTVIN','AYDIN','BALIKESIR','BILECIK','BINGOL','BITLIS','BOLU','BURDUR','BURSA-1','BURSA-2','CANAKKALE','CANKIRI','CORUM','DENIZLI','DIYARBAKIR','EDIRNE','ELAZIG','ERZINCAN','ERZURUM','ESKISEHIR','GAZIANTEP','GIRESUN','GUMUSHANE','HAKKARI','HATAY','ISPARTA','MERSIN','ISTANBUL-1','ISTANBUL-2','ISTANBUL-3','IZMIR-1','IZMIR-2','KARS','KASTAMONU','KAYSERI','KIRKLARELI','KIRSEHIR','KOCAELI','KONYA','KUTAHYA','MALATYA','MANISA','KAHRAMANMARAS','MARDIN','MUGLA','MUS','NEVSEHIR','NIGDE','ORDU','RIZE','SAKARYA','SAMSUN','SIIRT','SINOP','SIVAS','TEKIRDAG','TOKAT','TRABZON','TUNCELI','SANLIURFA','USAK','VAN','YOZGAT','ZONGULDAK','AKSARAY','BAYBURT','KARAMAN','KIRIKKALE','BATMAN','SIRNAK','BARTIN','ARDAHAN','IGDIR','YALOVA','KARABUK','KILIS','OSMANIYE','DUZCE']

# Loop through the PDF links and download each file
for link in pdf_links:
    pdf_url = base_url + link + '.pdf'
    print('Downloading:', pdf_url)
    file_name = link.split('/')[-1]
    response = requests.get(pdf_url)
    with open('pdfs//'+file_name+'.pdf', 'wb') as f:
        f.write(response.content)
