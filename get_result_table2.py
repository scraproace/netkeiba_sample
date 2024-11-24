from bs4 import BeautifulSoup
import requests


URL = 'https://db.netkeiba.com/race/202405040811/'


def get_result_table(url: str) -> list[list[str]]:
    headers = {
        'User-Agent': 'Your User-Agent'  # 置換必要
    }

    r = requests.get(url, headers=headers)
    r.raise_for_status()

    soup = BeautifulSoup(r.content, 'lxml')

    result_table = []

    for tr_tag in soup.select('.race_table_01 tr'):
        row = []
        for i, data_tag in enumerate(tr_tag.select('th, td')):
            # プレミアム限定列は除外
            if i in [9, 15, 16, 17]:
                continue

            row.append(data_tag.text.strip())

        result_table.append(row)

    return result_table


if __name__ == '__main__':
    result_table = get_result_table(URL)
    print(result_table)

'''
[
    ['着順', '枠番', '馬番', '馬名', '性齢', '斤量', '騎手', 'タイム', '着差', '通過', '上り', '単勝', '人気', '馬体重', '調教師', '馬主', '賞金(万円)'],
    ['1', '4', '7', 'ドウデュース', '牡5', '58', '武豊', '1:57.3', '', '14-14-13', '32.5', '3.8', '2', '504(-4)', '[西]\n友道康夫', 'キーファーズ', '22,323.4'],
    ...
    ['15', '7', '13', 'シルトホルン', '牡4', '58', '大野拓弥', '1:58.4', '1/2', '2-2-2', '34.6', '412.0', '14', '468(+4)', '[東]\n新開幸一', 'デ ィアレストクラブ', '']
]
'''
