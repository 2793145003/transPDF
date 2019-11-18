# transPDF
pdf translate en -> cn

## 更新
2019.11.18
- PDF读取部分换成了PyMuPDF，真鸡儿好用。感觉我已经天下无敌了xxx
- 不过Google的翻译服务好像挂了，一会再试试……
- 本来想加个界面做成阅读器的，查了一下发现好麻烦。还是算了吧，能用就行了xx
- 还有剪切板的翻译，做了一半觉得按复制键好麻烦，还不如直接全文翻译呢，反正也有原文xx

---
通天塔收费了呜呜呜……哼大不了自己做一个xxx

↑基本上就是基于这种心情随手写的玩意。嗯我知道很垃圾……

## 说明
- 因为是自己用的所以不保证可读性。
- 因为用了谷歌翻译所以可能需要翻墙。
- 可以替换成别的翻译的api。
- 有用的话可以随便拿，能用得上的话我会很开心的x

## 用法
1. 安装依赖
```
pip install -r requirements.txt
```
2. 修改`transPDF.py`中的`url`，也可以直接删掉，把`file`换成pdf路径
3. 运行
```
python transPDF.py
```

## 效果
![image](https://raw.githubusercontent.com/2793145003/transPDF/master/img/1.png)
所用pdf为《Arc-support Line Segments Revisited: An Efficient High-quality Ellipse Detection》

PDF连接：https://arxiv.org/pdf/1810.03243.pdf

## 参考
- PDF下载：https://blog.csdn.net/u012705410/article/details/47708031
- PDF解析：https://segmentfault.com/a/1190000015686181
- python谷歌翻译：https://www.jianshu.com/p/2f9a2b4c3aa3
