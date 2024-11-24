from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


URL = 'https://race.netkeiba.com/race/shutuba.html?race_id=202405040811&rf=race_submenu'


def get_shutuba_table(url: str) -> list[list[str]]:
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 30)

    try:
        driver.get(url)

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ShutubaTable')))

        soup = BeautifulSoup(driver.page_source, 'lxml')

        shutuba_table = []

        header_tr_tag = soup.select_one('.ShutubaTable > thead > tr:first-of-type')

        # .split('\n')[0]を入れないとオッズがオッズ\n\n更新となる
        shutuba_table.append([th_tag.text.strip().split('\n')[0] for th_tag in header_tr_tag.select('th')[:11]])

        for tbody_tr_tag in soup.select('.ShutubaTable > tbody > tr'):
            row = []
            for i, td_tag in enumerate(tbody_tr_tag.select('td')[:11]):
                # 印列のみ別処理
                if i == 2:
                    row.append(td_tag.select_one('.selectBox').text.strip())
                else:
                    row.append(td_tag.text.strip())

            shutuba_table.append(row)
    finally:
        driver.quit()

    return shutuba_table


if __name__ == '__main__':
    shutuba_table = get_shutuba_table(URL)
    print(shutuba_table)

'''
[
    ['枠', '馬番', '印', '馬名', '性齢', '斤量', '騎手', '厩舎', '馬体重(増減)', 'オッズ', '人気'],
    ['1', '1', '--', 'ベラジオオペラ', '牡4', '58.0', '横山和', '栗東上村', '514(-4)', '13.3', '4'],
    ...
    ['8', '15', '--', 'ニシノレヴナン ト', 'セ4', '58.0', '田辺', '美浦上原博', '490(0)', '415.8', '15']
]
'''
