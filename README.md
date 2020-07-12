# baike_spider
爬虫入门之爬取百度百科的1000个页面(标题+内容)，保存在一个html文件

注意：因为百度百科页面的元素经常会变，需要大家修改 解析文件parser.py里面的 _get_new_data函数的 title_node = soup.find('dl', class_='lemmaWgt-lemmaTitle-').find('h1') 与 
summary_node = soup.find('div', class_='lemma-summary')
