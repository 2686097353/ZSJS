import json

List=[]
for current_index in range(10):  # 从0到100
    with open(f'./题库/顺序练习/{current_index}.json', 'r', encoding='utf-8') as f:
        # 加载文件内容到data变量中
        startPaper = json.load(f)

    data = startPaper['data']
    result = data['result']
    questionList = result['questionList']
    print(len(questionList))
    for question in questionList:
        # print(question)
        List.append(question)


# print(len(List))
answer = {}
for option in List:
    id = option['id']
    # print(id)
    typeLabel = option['typeLabel']
    if typeLabel == "多选题":
        current = ""
        for ansower_option in option['optionList']:
            if ansower_option['isCorrect'] == 1:
                current += ansower_option['id']+','
        # print(current)
    else:
        for ansower_option in option['optionList']:
            if ansower_option['isCorrect'] == 1:
                current = ansower_option['id']
        # print(current)
    answer[id] = current
print(answer)
# 将所有问题写入JSON文件
with open(f'./题库/顺序练习/sum.json', 'w', encoding='utf-8') as f:
    json.dump(answer, f, ensure_ascii=False, indent=4)