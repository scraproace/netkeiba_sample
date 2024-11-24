import re

from bs4 import BeautifulSoup
import requests


URL = 'https://race.netkeiba.com/top/calendar.html?year=2024&month=10'


def get_kaisai_dates(url: str) -> list[str]:
    headers = {
        'User-Agent': 'Your User-Agent'  # 置換必要
    }

    r = requests.get(url, headers=headers)
    r.raise_for_status()

    soup = BeautifulSoup(r.content, 'lxml')

    kaisai_dates = []

    for a_tag in soup.select('.Calendar_Table .Week > td > a'):
        kaisai_date = re.search(r'kaisai_date=(.+)', a_tag.get('href')).group(1)
        kaisai_dates.append(kaisai_date)

    return kaisai_dates


if __name__ == '__main__':
    kaisai_dates = get_kaisai_dates(URL)
    print(kaisai_dates)

'''
['20241005', '20241006', '20241012', '20241013', '20241014', '20241019', '20241020', '20241026', '20241027']
'''
