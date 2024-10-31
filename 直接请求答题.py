import requests
import json

userActivityId = ''
cookie = ''
authorization = ''


with open(f'./题库/sum.json', 'r', encoding='utf-8') as f:
    # 加载文件内容到data变量中
    sum_anoswer = json.load(f)



#1.获取题库
url = 'https://mars.mycourse.cn/marsapi/api/study/activity/exam/v1/startPaper'


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
# POST请求的负载数据

payload1 = {
        'userActivityId': userActivityId,
}
# 发起POST请求
response = requests.post(url, headers=headers, data=payload1)
print(response.text)

data = response.json()
print(len(data['data']['result']['questionList']))
for option in data['data']['result']['questionList']:
    id = option['id']
    if sum_anoswer[id]:
        answerIds = sum_anoswer[id]
    payload = {
        'userActivityId': userActivityId,
        'questionId': id,
        'useTime': '1',
        'answerIds': answerIds,
    }
    url = 'https://mars.mycourse.cn/marsapi/api/study/activity/exam/v1/recordQuestion'
    response = requests.post(url, headers=headers, data=payload)
    print(response.text)

url = 'https://mars.mycourse.cn/marsapi/api/study/activity/exam/v1/submitPaper'
response = requests.post(url, headers=headers, data=payload1)
print(response.text)




