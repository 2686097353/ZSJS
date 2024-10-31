___江苏省安全知识竞赛全自动答题___


开始本来写js自动答题，后来发现用python发送请求好像能直接发送请求，实现0秒答题






![c419c796b1b707fde583e34b1c478ff1](https://github.com/user-attachments/assets/0febebd7-f787-4af4-a671-a3d6fedab4bd)
![35f74b49b78feb25308f3514bc335303](https://github.com/user-attachments/assets/520b4309-0cf1-49b9-b573-7c5ba0ef583a)




**1.js自动答题**

点击开始后，进入答题页面，浏览器F12，打开开发者工具，在控制台粘贴代码，回车自动运行
![0816a1ca9d6e412a0bee92da644e86a3](https://github.com/user-attachments/assets/83053169-bbd1-4ea1-9ced-daee63575d10)














**2.发送请求**

这里只抓取了模拟考试和正式考试，练习不适用

浏览器F12，打开开发者工具，点击网络，网页点击开始答题，然后会出现一个请求，抓取请求头的cookie，authorization和负载里面的userActivityId值，填入py文件即可

![1730347724881](https://github.com/user-attachments/assets/4b6d7046-2af5-4b4a-ba40-377516da7fcb)

