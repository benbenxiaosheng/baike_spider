import urllib3

# 创建PoolManager对象生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
http = urllib3.PoolManager()

# get方式请求
response = http.request('GET', 'http://www.baidu.com')

# 获得状态码, html源码(utf-8解码)
print(response.status,response.data.decode('utf-8'))