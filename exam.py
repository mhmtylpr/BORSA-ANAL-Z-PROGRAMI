from selenium import webdriver
from time import sleep

print(15*"*" + "  " + "BORSA ANALİZ PROGRAMI" + "  " + 15*"*" + 3*"\n")

chrome = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.delete_all_cookies()

# Internet ya da sunucu kaynaklı hata mesajı derlendi

try:
    driver.implicitly_wait(15)
except:
    print("Lütfen internet bağlantınızı kontrol ediniz...")
    print("İnternet bağlantınızda bir problem yoksa site sunucusu cevap vermekte gecikiyor lütfen daha sonra tekrar deneyiniz")
    print("Teşekkürler...")

# Sabit değişkenler tanımlandı

NUM = 0
STNDRT_NAME = '//*[@id="ctl00_ctl58_g_81d0c4e3_49e1_40c1_84ae_878b4c967bbb"]/div/div[1]/div/div[1]/div[1]/div[1]/span'
STNDRT_PRİCE = '//*[@id="hisse_Son"]'
LIST = list()
IND = 0
driver.get("https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/default.aspx")

#Şirketlerin adı indexler kullanılarak belirtildi

for i in range(0,534):
    NUM+=1
    URL = f'//*[@id="DataTables_Table_0"]/tbody/tr[{NUM}]/td[1]/a'
    t = driver.find_element("xpath" , URL).text
    LIST.append(t)

#Şirketlerin AD,FİYAT,F/D,PD/DD durumları indexler kullanılarak çağırıldı

for i in range(0,534):

    # driver.get(f"https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=[{LIST[IND]}")

    # Sonucun çıktısını oluşturacak fonksiyon oluşturuldu

    def price(url,name,price):
        FD = '//*[@id="ctl00_ctl58_g_76ae4504_9743_4791_98df_dce2ca95cc0d"]/div[2]/div/table/tbody/tr[2]/td'
        PDDD = '//*[@id="ctl00_ctl58_g_76ae4504_9743_4791_98df_dce2ca95cc0d"]/div[2]/div/table/tbody/tr[3]/td'
        driver.get(url)
        NAME = driver.find_element("xpath",name).text
        PRİCE = driver.find_element("xpath" , price).text
        FD_NUM = driver.find_element("xpath" , FD).text
        PDDD_NUM = driver.find_element("xpath" , PDDD).text
        print(f"AD: {NAME} ,  FİYAT: {PRİCE} , F/D: {FD_NUM} , PD/DD: {PDDD_NUM}")

        #Siteden yeterli veri çekmesi için bekleme fonksiyonu çağırıldı

    sleep(1)
    IND += 1

# Fonksiyon çağırıldı

    price(f"https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={LIST[IND]}",STNDRT_NAME,STNDRT_PRİCE)




