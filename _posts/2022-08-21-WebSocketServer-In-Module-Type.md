---
title: 「大坑」关于 module 模式下如何正确引入 WebSocketServer
date: 2022-08-21 17:44:30
tags:
 - Node
 - 折腾
 - 抓狂
categories:
 - 电脑网络
id: 879
alias: 20220301064
---

> WebSocket.Server is not a constructor

遇到上边错误，直接照着 cjs 写法改成 mjs 形式，但是用不了；

<!--more-->

```js
import WebSocket from "ws"
console.log(typeof WebSocket)
console.log(typeof WebSocket.Server)
// function
// undefined
```

用报错的「`WebSocket.Server is not a constructor`」作为关键词并没能找到原因；

直到我换了个姿势，直接搜索「`import WebSocket from 'ws'`」，得到的代码是下边这样子的：

```js
import WebSocket, { WebSocketServer } from 'ws';
console.log(typeof WebSocket)
console.log(typeof WebSocketServer)
// function
// function
```

然后我去看了 ws 这个库的导出文件；

```js
// cjs
'use strict';

const WebSocket = require('./lib/websocket');

WebSocket.createWebSocketStream = require('./lib/stream');
WebSocket.Server = require('./lib/websocket-server');
WebSocket.Receiver = require('./lib/receiver');
WebSocket.Sender = require('./lib/sender');

WebSocket.WebSocket = WebSocket;
WebSocket.WebSocketServer = WebSocket.Server;

module.exports = WebSocket;
```

```js
// mjs
import createWebSocketStream from './lib/stream.js';
import Receiver from './lib/receiver.js';
import Sender from './lib/sender.js';
import WebSocket from './lib/websocket.js';
import WebSocketServer from './lib/websocket-server.js';

export { createWebSocketStream, Receiver, Sender, WebSocket, WebSocketServer };
export default WebSocket;
```

差别不只是有点儿大好么 Orz；
