# Chatapp

这个项目是一个最简单的基于Django和socket.io实现的聊天室。目前正在完善中。

## 运行
```

```

功能
1. 登入与登出
客户端浏览器内，登入时将用户名存入localStorage从而避免输入密码和保存会话。
登入时向服务器发送message
服务器收到message更新userlist并广播

浏览器可以通过点击按钮，或者是通过关闭tab/程序等事件触发，向服务器发送message
服务器收到message，更新userlist并广播。
