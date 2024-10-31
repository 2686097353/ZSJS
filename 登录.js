// 查找包含"南京信息工程大学"的列表项
const item = Array.from(document.querySelectorAll('.el-select-dropdown__item'))
                  .find(li => li.textContent.includes('南京信息工程大学'));

// 如果找到了该元素，模拟点击
if (item) {
    item.click();
}



// 等待一定时间后执行
setTimeout(() => {
    // 选择账号输入框
    const usernameInput = document.querySelector('.phone-email .el-input__inner');
    // 填写账号
    if (usernameInput) {
        usernameInput.value = '202412492138'; // 替换为你的账号
        // 触发 input 事件以确保其他逻辑能够响应这个变化
        usernameInput.dispatchEvent(new Event('input', { bubbles: true }));
    } else {
        console.error('账号输入框未找到');
    }

    // 选择密码输入框
    const passwordInput = document.querySelector('.pw .el-input__inner');
    // 填写密码
    if (passwordInput) {
        passwordInput.value = 'jzy000925.'; // 替换为你的密码
        // 触发 input 事件以确保其他逻辑能够响应这个变化
        passwordInput.dispatchEvent(new Event('input', { bubbles: true }));
    } else {
        console.error('密码输入框未找到');
    }
}, 2000); // 等待2000毫秒（2秒），可以根据需要调整时间
