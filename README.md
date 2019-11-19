# transPDF
pdf translate en -> cn

## 更新
2019.11.19
- 换成google.cn翻译了，一是没有墙，二是翻译效果比之前的山寨包好太多了

2019.11.18
- PDF读取部分换成了PyMuPDF，真鸡儿好用。感觉我已经天下无敌了xxx
- 本来想加个界面做成阅读器的，查了一下发现好麻烦。还是算了吧，能用就行了xx
- 还有剪切板的翻译，做了一半觉得按复制键好麻烦，还不如直接全文翻译呢，反正也有原文xx

---
通天塔收费了呜呜呜……哼大不了自己做一个xxx

↑基本上就是基于这种心情随手写的玩意。嗯我知道很垃圾……

## 说明
- 因为是自己用的所以不保证可读性。
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
所用pdf为《How does the brain solve visual object recognition?》

PDF连接：https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3306444/pdf/nihms352068.pdf

## 参考
- PDF下载：https://blog.csdn.net/u012705410/article/details/47708031
- PDF解析：https://segmentfault.com/a/1190000015686181
- python谷歌翻译：https://www.jianshu.com/p/2f9a2b4c3aa3
