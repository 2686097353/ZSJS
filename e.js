let questions = []; // 存储题目信息

async function fetchQuestion() {
    // 获取题型和题目
    const questionType = document.querySelector('.type').innerText;
    const questionContent = document.querySelector('.content').innerText;

    // 点击查看答案按钮
    document.querySelector('.btn[style*="background-color: rgb(245, 108, 108)"]').click();

    // 等待查看答案加载
    await new Promise(resolve => setTimeout(resolve, 500)); // 等待0.5秒确保已加载

    // 获取正确选项的最后一个字符
    const correctOptionMessage = document.querySelector('.el-message-box__message p').innerText;
    const correctOption = correctOptionMessage.charAt(correctOptionMessage.length - 1); // 获取倒数第一个字符

    // 点击确定按钮
    document.querySelector('.el-button.el-button--default.el-button--small.el-button--primary').click();

    // 获取选项
    const options = Array.from(document.querySelectorAll('.option')).map(option => {
        const label = option.querySelector('.el-radio__label').innerText.trim();
        const value = label.charAt(0); // 将 value 设置为 label 的第一个字符

        const radioInput = option.querySelector('.el-radio__original');

        // 如果当前选项是正确答案，则标记为选中
        if (correctOption === value) {
            radioInput.checked = true; // 选择正确的选项
            // 手动触发 change 事件
            radioInput.dispatchEvent(new Event('change', {bubbles: true}));
            console.log(`选择的正确选项: ${label}`); // 输出选择的正确选项
        }

        return {label, value}; // 使用简化的对象返回方式
    });

    // 保存当前题目信息
    questions.push({
        questionType,
        questionContent,
        correctOption,
        options
    });

    // 输出结果
    console.log({
        questionType,
        questionContent,
        correctOptionMessage,
        options
    });

    // 等待加载下一题
    await new Promise(resolve => setTimeout(resolve, 1000));

    // 检查是否还有更多题目
    if (document.querySelector('.next.btn')) {
        document.querySelector('.next.btn').click();
        // 继续获取下一个问题
        fetchQuestion();
    } else {
        // 处理收集到的题目信息
        console.log(questions);
        // 可以在这里进行数据下载等操作
    }
}

// 启动获取题目的过程
fetchQuestion();