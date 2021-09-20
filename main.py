import re
import requests

from bs4 import BeautifulSoup
import fake_useragent


sumClaim = 0
sumPercentage = 0

# читаем файл с адресами в список

with open("eth.txt") as f:
    addresses = f.readlines()

addresses = [x.strip() for x in addresses]

# по каждому адресу делаем запрос

for address in addresses:

    # генерируем сессию

    session = requests.Session()
    headers = {
        'user-agent': fake_useragent.UserAgent().random
    }

    url = f"https://testnet1.streamr.network:3013/stats/{address}"

    # отправляем запрос

    request = session.get(url=url, headers=headers)

    # разбираем ответ

    soup = BeautifulSoup(request.text, 'lxml')
    claimPercentage = soup.string

    claimCount = re.findall(r'\d+', claimPercentage)

    # выводим результат

    if (len(claimCount) == 3):
        percentage = f"{claimCount[2][:2]}"
        sumPercentage = sumPercentage + int(percentage)
        sumClaim = sumClaim + int(claimCount[0])

        print(f'{address}: {claimCount[0]} rewards, claimed: {percentage}%')
    else:

        print(f"{address}: no rewards.")

print(f"\ntotal rewards: {str(sumClaim)} | average rewards: {str(int(round(sumClaim/len(addresses))))} | average percentage: {str(int(round(sumPercentage/len(addresses))))}")
print("\nwith love by @cyberomanov.")