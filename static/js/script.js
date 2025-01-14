// 聊天功能初始化
function initializeChatbot() {
    const chatbotButton = document.getElementById('chatbotButton'); // 悬浮按钮
    const chatbotWindow = document.getElementById('chatbotWindow'); // 聊天窗口
    const closeChatbotWindow = document.getElementById('closeChatbotWindow'); // 关闭按钮
    const sendMessage = document.getElementById('sendMessage'); // 发送按钮
    const chatbotMessages = document.getElementById('chatbotMessages'); // 聊天内容区域
    const userMessageInput = document.getElementById('userMessage'); // 输入框

    // 点击悬浮按钮显示聊天窗口
    chatbotButton.addEventListener('click', function () {
        chatbotWindow.style.display = 'block'; // 显示聊天窗口
        chatbotButton.style.display = 'none'; // 隐藏悬浮按钮
    });

    // 点击关闭按钮隐藏聊天窗口
    closeChatbotWindow.addEventListener('click', function () {
        chatbotWindow.style.display = 'none'; // 隐藏聊天窗口
        chatbotButton.style.display = 'block'; // 显示悬浮按钮
    });

    // 发送用户消息并显示回复
    sendMessage.addEventListener('click', function () {
        const userMessage = userMessageInput.value;
        if (userMessage.trim() === '') return;

        // 显示用户消息
        const userMessageElement = document.createElement('div');
        userMessageElement.textContent = "You: " + userMessage;
        userMessageElement.style.margin = '5px 0';
        chatbotMessages.appendChild(userMessageElement);

        // 清空输入框
        userMessageInput.value = '';

        // 发送消息给后端并获取回复
        fetch('/Chatbot', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userMessage })
        })
            .then(response => response.text()) // 解析为纯文本
            .then(data => {
                // 显示机器人回复
                const botMessageElement = document.createElement('div');
                botMessageElement.textContent = "Bot: " + data;
                botMessageElement.style.margin = '5px 0';
                botMessageElement.style.color = 'blue';
                chatbotMessages.appendChild(botMessageElement);

                // 滚动到底部
                chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
            })
            .catch(error => {
                console.error("Error in fetch:", error); // 捕获错误
            });
    });
}

// Sea Level 页面加载
function showSeaLevelPage() {
    document.getElementById('welcome-text').style.display = 'none';
    document.getElementById('welcome-description').style.display = 'none';

    const mainContainer = document.querySelector('main');
    mainContainer.innerHTML = '';

    const iframe = document.createElement('iframe');
    iframe.src = '/sea_level?' + new Date().getTime(); // 防止缓存
    mainContainer.appendChild(iframe);
}

// Ice Mass 页面加载
function showIceMassPage() {
    document.getElementById('welcome-text').style.display = 'none';
    document.getElementById('welcome-description').style.display = 'none';

    const mainContainer = document.querySelector('main');
    mainContainer.innerHTML = '';

    const iframe = document.createElement('iframe');
    iframe.src = '/ice_mass?' + new Date().getTime(); // 防止缓存
    mainContainer.appendChild(iframe);
}

// 页面加载完成后初始化
window.onload = function () {
    initializeChatbot();
};
