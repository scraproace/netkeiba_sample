from bs4 import BeautifulSoup
import requests


URL = 'https://db.netkeiba.com/race/202405040811/'


def get_pay_table(url: str) -> list[list[str]]:
    headers = {
        'User-Agent': 'Your User-Agent'  # 置換必要
    }

    r = requests.get(url, headers=headers)
    r.raise_for_status()

    soup = BeautifulSoup(r.content, 'lxml')

    pay_table = []

    for table_tag in soup.select('.pay_table_01'):
        for tr_tag in table_tag.select('tr'):
            # get_text('\n')とすることで<br>タグを\nに変換
            pay_table.append([data_tag.get_text('\n').strip() for data_tag in tr_tag.select('th, td')])

    return pay_table


if __name__ == '__main__':
    pay_table = get_pay_table(URL)
    print(pay_table)

'''
[
    ['単勝', '7', '380', '2'],
    ['複勝', '7\n4\n9', '200\n1,020\n1,000', '2\n9\n8'],
    ...
    ['三連単', '7 → 4 → 9', '397,100', '612']
]
'''
