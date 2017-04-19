import re
import urllib.request

# ------ 获取网页源代码的方法 ---
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

urls ="https://www.taobao.com/"
# ------ getHtml()内输入任意帖子的URL ------
html = getHtml(urls)
# ------ 修改html对象内的字符编码为UTF-8 ------
html = html.decode('UTF-8')
with open("text.html",'w') as f:
    f.write(html)
