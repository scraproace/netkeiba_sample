from bs4 import BeautifulSoup
import requests


URL = 'https://race.netkeiba.com/race/result.html?race_id=202405040811&rf=race_submenu'


def get_result_table(url: str) -> list[list[str]]:
    headers = {
        'User-Agent': 'Your User-Agent'  # 置換必要
    }

    r = requests.get(url, headers=headers)
    r.raise_for_status()

    soup = BeautifulSoup(r.content, 'lxml')

    result_table = []

    for tr_tag in soup.select('#All_Result_Table tr'):
        result_table.append([data_tag.text.strip() for data_tag in tr_tag.select('th, td')])

    return result_table


if __name__ == '__main__':
    result_table = get_result_table(URL)
    print(result_table)

'''
[
    ['着順', '枠', '馬番', '馬名', '性齢', ..., '厩舎', '馬体重(増減)'],
    ['1', '4', '7', 'ドウデュース', '牡5', ..., '栗東友 道', '504(-4)'],
    ...
    ['15', '7', '13', 'シルトホルン', '牡4', ..., '美浦新開', '468(+4)']
]
'''
