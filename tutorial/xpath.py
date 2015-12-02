#coding=utf-8
'''
Created on 2015年11月21日

@author: Qiang
'''
#//定位根节点
#/往下层寻找
#提取文本内容:/text()
#提取属性内容:/@xxxx
#以相同的字符开头时,starts-with(@属性名称,属性字符相同部分)
#标签套标签,string(.)

from lxml import etree
html = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>测试-常规用法</title>
</head>
<body>
<div id="content">
    <ul id="useful">
        <li>这是第一条信息</li>
        <li>这是第二条信息</li>
        <li>这是第三条信息</li>
    </ul>
    <ul id="useless">
        <li>不需要的信息1</li>
        <li>不需要的信息2</li>
        <li>不需要的信息3</li>
    </ul>

    <div id="url">
        <a href="http://jikexueyuan.com">极客学院</a>
        <a href="http://jikexueyuan.com/course/" title="极客学院课程库">点我打开课程库</a>
    </div>
    
</div>
    <div id="test-1">需要的内容1</div>
    <div id="test-2">需要的内容2</div>
    <div id="testfault">需要的内容3</div>
    <div id="qt">
        我左青龙，
        <span id="tiger">
            右白虎，
            <ul>上朱雀，
                <li>下玄武。</li>
            </ul>老牛在当中，
        </span>龙头在胸口。
    </div>
</body>
</html>
'''
selector = etree.HTML(html)
#'//*/ul[@id="useful"]/li/text()'
#'//div[@id="content"]/ul[@id="useful"]/li/text()'
#'//ul[@id="useful"]/li/text()'
liText = selector.xpath('//ul[@id="useful"]/li/text()')

for li in liText:
    print li
print '==============='
#'//a/@href'
#'//div[@id="url"]/a/@href'
aHref = selector.xpath('//div[@id="url"]/a/@href')
for href in aHref:
    print href
print '==============='
aTitle = selector.xpath('//a/@title')
for title in aTitle:
    print title
print '==============='
aText = selector.xpath('//div[@id="url"]/a/text()')
for text in aText:
    print text
print '==============='
aTextOne = selector.xpath('//div[@id="url"]/a[1]/text()')
for text in aTextOne:
    print text
print '==============='
startText = selector.xpath('//div[starts-with(@id,"test")]/text()')
for text in startText:
    print text
print '==============='
qtString = selector.xpath('//div[@id="qt"]')[0]
qtInfo = qtString.xpath('string(.)')
info = qtInfo.replace('\n','').replace(' ','')
print info 