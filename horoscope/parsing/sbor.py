import sqlite3 as sq
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import os

def get_data_with_selenium():
    zodiac_hrefs = []

    with open('index.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    zodiac_signs = soup.find('div', class_='daily__zodiacs')

    for zodiac_sign_from_url in zodiac_signs.find_all('a'):
        zodiac_sign_from_url = 'https://www.thevoicemag.ru' + zodiac_sign_from_url.get('href')
        zodiac_hrefs.append(zodiac_sign_from_url)

    return zodiac_hrefs

def get_data_on_the_zodiac_sign(arraychik: list):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    try:
        for zodiac_url in arraychik:
            html_for_zodiac_signs = zodiac_url[43:-1:] + '.html'
            driver.get(url=zodiac_url)
            time.sleep(2)
            with open('C:\python\PycharmProjects\T_Z\Zad_from_Ilya\horoscope\parsing\zodiac_signs\\' + html_for_zodiac_signs, 'w', encoding="utf-8") as file:
                file.write(driver.page_source)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def get_content():
    directory = os.fsencode(r'C:\python\PycharmProjects\T_Z\Zad_from_Ilya\horoscope\parsing\zodiac_signs')
    dates = ''
    prognozes = []

    for f in os.listdir(directory):
        filename = os.fsdecode(f)
        with open('zodiac_signs\\' + filename, 'r', encoding='utf-8') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')

        dates = soup.find('div', class_='sign__description-date').find_all('span')
        dates = f'{dates[0].text} {dates[1].text}'
        prognozes.append(soup.find('div', class_='sign__description-text').text)

    return [dates, prognozes]

def zapolnenie_bd(peremena: str, array: list):
    bd = sq.connect('C:\python\PycharmProjects\T_Z\Zad_from_Ilya\horoscope\zodiac_signs_prognoz.sqlite3')
    cur = bd.cursor()
    for i in range(1, len(array)+1):
        cur.execute("UPDATE horoscope_app_zodiac_signs_prognoz SET date = ?, content = ? WHERE id = ?", (peremena, array[i-1], i))
        bd.commit()
    bd.close()


def main():
    vsp = get_data_with_selenium()
    get_data_on_the_zodiac_sign(vsp)
    nado = get_content()
    zapolnenie_bd(nado[0], nado[1])

if __name__ == '__main__':
    main()
