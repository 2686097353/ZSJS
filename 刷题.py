from selenium.webdriver.edge.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from PIL import Image
import pytesseract
import io
import time
questions = []

# 设置Edge浏览器的选项
options = Options()
options.add_experimental_option('detach', True)

# 创建Edge浏览器实例
driver = webdriver.Edge(options=options)

# 访问考试页面
try:
    driver.get('https://mars.mycourse.cn/deimos/#/')

    with open('登录.js', 'r', encoding='utf-8') as file:
        script_content = file.read()
    results_text = driver.execute_script(script_content)

    # 获取验证码图片的 URL
    captcha_img_element = driver.find_element(By.CSS_SELECTOR, ".verification-code img")
    captcha_img_url = captcha_img_element.get_attribute("src")
    print("验证码图片 URL:", captcha_img_url)

    # 下载验证码图片
    response = requests.get(captcha_img_url)
    captcha_image = response.content

    # 将验证码图片加载到 PIL 中
    image = Image.open(io.BytesIO(captcha_image))

    # 进行验证码预处理（可选）
    # 这里可以进行灰度处理、二值化等
    image = image.convert('L')  # 转换为灰度图
    image = image.point(lambda x: 0 if x < 128 else 255, '1')  # 二值化

    # 使用 pytesseract 进行识别
    result = pytesseract.image_to_string(image, config='--psm 8')  # 8: 只识别单行
    print("识别的验证码是:", result.strip())

    # 将识别到的验证码输入到输入框
    input_element = driver.find_element(By.CSS_SELECTOR, ".el-input__inner")
    input_element.send_keys(result.strip())




    # 等待直到当前网址等于指定值
    target_url = 'https://mars.mycourse.cn/deimos/#/home'  # 替换为你的目标网址
    try:
        WebDriverWait(driver, 30).until(
            lambda driver: driver.current_url == 'https://mars.mycourse.cn/deimos/#/home'
        )
        print(f"登录成功\n")
    except Exception as e:
        print(f"原因: {e}")

    try:
        # 等待按钮可点击
        start_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[span[text()='开 始']]"))
        )
        # 点击按钮
        start_button.click()
    except Exception as e:
        print(f"出现错误: {e}")





    while(2):
        # 获取题型和题目
        # 获取题型和题目
        question_type = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.type'))
        ).text

        question_content = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.content'))
        ).text

        # 点击查看答案按钮
        driver.find_element(By.CSS_SELECTOR, '.btn[style*="background-color: rgb(245, 108, 108)"]').click()

        # 等待查看答案加载
        time.sleep(0.5)  # 等待0.5秒确保已加载

        # 获取正确选项的最后一个字符
        correct_option_message = driver.find_element(By.CSS_SELECTOR, '.el-message-box__message p').text
        correct_option = correct_option_message[-1]  # 获取倒数第一个字符

        # 点击确定按钮
        driver.find_element(By.CSS_SELECTOR,
                            '.el-button.el-button--default.el-button--small.el-button--primary').click()

        # 等待选项加载
        time.sleep(0.5)  # 等待0.5秒确保已加载

        # 获取选项
        options = []
        for option in driver.find_elements(By.CSS_SELECTOR, '.option'):
            label = option.find_element(By.CSS_SELECTOR, '.el-radio__label').text.strip()
            value = label[0]  # 将 value 设置为 label 的第一个字符

            radio_input = option.find_element(By.CSS_SELECTOR, '.el-radio__original')

            # 如果当前选项是正确答案，则标记为选中
            if correct_option == value:
                radio_input.click()  # 选择正确的选项
                print(f'选择的正确选项: {label}')  # 输出选择的正确选项

            options.append({'label': label, 'value': value})  # 添加选项到列表

        # 输出结果
        result = {
            'questionType': question_type,
            'questionContent': question_content,
            'correctOptionMessage': correct_option_message,
            'options': options
        }
        print(result)
        questions.append(result)

        # 点击下一步按钮
        time.sleep(1)  # 等待1秒确保已加载
        driver.find_element(By.CSS_SELECTOR, '.next.btn').click()
















except Exception as e:
    print(f"原因: {e}")