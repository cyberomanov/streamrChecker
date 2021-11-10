import requests

import fake_useragent


sumRew = 0
sumPercentage = 0
confirmed = 0

# читаем файл с адресами в список

with open("eth.txt") as f:
    addresses = f.readlines()

addresses = [x.strip() for x in addresses]

# по каждому адресу делаем запрос

for address in addresses:

    # генерируем сессию
    try:
        url = f"https://testnet1.streamr.network:3013/stats/{address}"
        session = requests.Session()

        # отправляем запрос

        try:
            headers = {
                'user-agent': fake_useragent.UserAgent().random
            }
            request = session.get(url=url, headers=headers)
        except:
            request = session.get(url=url)

        # разбираем ответ

        response = request.json()
        claimCount = response['claimCount']
        claimPercentage = round(float(response['claimPercentage']), 2)
        totalEarningsInData = round(float(response['totalEarningsInData']), 2)

        sumPercentage = sumPercentage + claimPercentage
        sumRew = sumRew + totalEarningsInData
        confirmed = confirmed + 1

        print(f'{address} > claimed: {claimCount}, percentage: {claimPercentage}, reward: {totalEarningsInData} DATA.')
    except:
        print(f"{address} > no rewards.")

print(f"\n/////////////////////////////////////////////////////////////////////")

print(f"total rewards: {str(sumRew)} | average rewards: {str(int(round(sumRew/confirmed)))}")

print("\nwith love by @cyberomanov.")
