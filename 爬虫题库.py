import json
import requests

import requests


userActivityId = ''
cookie = ''
authorization = ''


# 初始化一个空列表来存储所有问题
all_questions = []
# 请求URL
url = 'https://mars.mycourse.cn/marsapi/api/study/activity/practice/v1/getNear'

# 请求头
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'authorization': authorization,
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'cookie': cookie,
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
        'userActivityId': userActivityId,
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


