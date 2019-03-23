import socket
#客户端
'''
大多数连接都是可靠的TCP连接。
创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器。
举个例子，
当我们在浏览器中访问新浪时，
我们自己的计算机就是客户端，
浏览器会主动向新浪的服务器发起连接。
如果一切顺利，新浪的服务器接受了我们的连接，
一个TCP连接就建立起来的，
后面的通信就是发送网页内容了。
'''
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
'''
客户端要主动发起TCP连接，
必须知道服务器的IP地址和端口号。
新浪网站的IP地址可以用域名www.sina.com.cn自动转换到IP地址，
但是怎么知道新浪服务器的端口号呢？

答案是作为服务器，
提供什么样的服务，
端口号就必须固定下来。
由于我们想要访问网页，
因此新浪提供网页服务的服务器必须把端口号固定在80端口，
因为80端口是Web服务的标准端口。
其他服务都有对应的标准端口号，
例如SMTP服务是25端口，
FTP服务是21端口，等等。
端口号小于1024的是Internet标准服务的端口，
端口号大于1024的，可以任意使用。
'''
s.connect((socket.gethostname(),1234))
#接收数据时，调用recv(max)方法，一次最多接收指定的字节数(可以改变成自己想要的如下：）
#message = s.recv(1024)
#解码，由于server那边定义了以utf-8编码的二进制传输，所以此处需要解码二进制
#print(message.decode('utf-8'))

full_message = ''
while True:
    message = s.recv(4)
    if len(message) <= 0:
        break
    full_message += message.decode('utf-8')

print(full_message)
