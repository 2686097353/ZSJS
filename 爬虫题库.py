import json
import requests

import requests
# 初始化一个空列表来存储所有问题
all_questions = []
# 请求URL
url = 'https://mars.mycourse.cn/marsapi/api/study/activity/practice/v1/getNear'

# 请求头
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJjbGllbnRUeXBlIjoyLCJ1c2VyaWQiOiI1NTM0MTQyNzgzMTYwODM3IiwicGxhdGZvcm0iOjIsImxvZ2luX3VzZXJfa2V5IjoiMGUzNGFlNDFlYzJmMjUzMzg4ZGMwOTkwYWE5NjA5OGIifQ.MN7K-R76Qs2y4Q5qU6F7QIz_yZwR9zGayeUeoof4i-aAaLdZhzbs-yQZ30I0KONOd28U0Uf-KLYtxqtARJrK9g',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'cookie': 'Hm_lvt_890425597da00ebdf2d7bf4fd671fa46=1730294821,1730301584,1730305313; Hm_lpvt_890425597da00ebdf2d7bf4fd671fa46=1730305313; HMACCOUNT=1B9B892625EDE6FF; mars_token=eyJhbGciOiJIUzUxMiJ9.eyJjbGllbnRUeXBlIjoyLCJ1c2VyaWQiOiI1NTM0MTQyNzgzMTYwODM3IiwicGxhdGZvcm0iOjIsImxvZ2luX3VzZXJfa2V5IjoiMGUzNGFlNDFlYzJmMjUzMzg4ZGMwOTkwYWE5NjA5OGIifQ.MN7K-R76Qs2y4Q5qU6F7QIz_yZwR9zGayeUeoof4i-aAaLdZhzbs-yQZ30I0KONOd28U0Uf-KLYtxqtARJrK9g',
    'origin': 'https://mars.mycourse.cn',
    'referer': 'https://mars.mycourse.cn/deimos/',
    'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
}

for current_index in range(10):  # 从0到100
    # POST请求的负载数据
    payload = {
        'userActivityId': '5534143192695336',
        'currentIndex': current_index,
        'nearType': 2
    }
    # 发起POST请求
    response = requests.post(url, headers=headers, data=payload)
    data = response.json()
    print(data)
    print(current_index)
    print(len(data['data']['result']['questionList']))


    # 将所有问题写入JSON文件
    with open(f'./题库/顺序练习/{current_index}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


