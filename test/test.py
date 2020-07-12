import urllib.request


def main():

    url = "https://baike.baidu.com/item/Python/407313"

    # 服务器给的响应
    response = urllib.request.urlopen(url)

    # 返回一个二进制字符串: b'',无法正常阅读
    html = response.read()

    # 进行解码操作
    code_of_html = html.decode('utf-8')

    # 打印查看网页源代码
    print(code_of_html)


if __name__ == '__main__':
    main()