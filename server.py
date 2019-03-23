import socket
#socket object

'''
1
Socket又称"套接字"，
应用程序通常通过"套接字"向网络发出请求或者应答网络请求，
使主机间或者一台计算机上的进程间可以通讯。
2
通常我们用一个Socket表示“打开了一个网络链接”，
而打开一个Socket需要知道目标计算机的IP地址和端口号，
再指定协议类型即可。
3
大多数连接都是可靠的TCP连接。
创建TCP连接时，
主动发起连接的叫客户端，
被动响应连接的叫服务器。
4
TCP协议（传输层）通过三次握手
这三次握手通过socket实现
'''

#服务器
'''
1
服务器进程首先要绑定一个端口(port)
并监听(listen)来自其他客户端的连接。
如果某个客户端连接(bind)过来了，
服务器就与该客户端建立Socket连接，
随后的通信就靠这个Socket连接了。
2
所以，服务器会打开固定端口（比如80）监听，
每来一个客户端连接，
就创建该Socket连接。
由于服务器会有大量来自客户端的连接，
所以，服务器要能够区分一个Socket连接是和哪个客户端绑定的。
一个Socket依赖4项：
服务器地址、
服务器端口、
客户端地址、
客户端端口
来唯一确定一个Socket。
3
但是服务器还需要同时响应多个客户端的请求，
所以，每个连接都需要一个新的进程或者新的线程来处理，
否则，服务器一次就只能服务一个客户端了。

'''
#首先，创建一个基于IPv4和TCP协议的Socket：
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#1ipv4 2tcp
#然后，我们要绑定监听的地址和端口。
'''
# 服务器可能有多块网卡（MAC），
# 可以绑定到某一块网卡的IP地址上，
# 也可以用0.0.0.0绑定到所有的网络地址，
# 还可以用127.0.0.1绑定到本机地址。
# 127.0.0.1是一个特殊的IP地址，表示本机地址，
# 如果绑定到这个地址，客户端必须同时在本机运行才能连接，
# 也就是说，外部的计算机无法连接进来。
端口号需要预先指定。
因为我们写的这个服务不是标准服务，
所以用随便。
请注意，小于1024的端口号必须要有管理员权限才能绑定：
'''
s.bind((socket.gethostname(),1234))#socket.gethostname()作用：获取当前主机的主机名(ip)

#紧接着，调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
s.listen(5)

#接下来，服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接:
while True:
    # 接受一个新连接:
    clientsocket, address = s.accept()#客户端的socket和客户端的ip地址
    print(f"Connetion from{address} has been established!")#在打印字符串时使用函数
    clientsocket.send(bytes("Welcome to the server!","utf-8"))#utf-8一种编码格式
    clientsocket.close()
    '''
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
    '''




