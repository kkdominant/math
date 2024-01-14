## 极限

`def my_limit(expression,tendency,dir=None):`

* expression：也就是表达式
* tendency:就是$x$趋于多少，趋于0就写0
* dir:direction,方向,默认左右两侧、可选"+"或者"-"

**示例:**

![image-20240114145827636](https://typoracsdnzhihu.oss-cn-nanjing.aliyuncs.com/ing/image-20240114145827636.png)

## 积分:

`def my_int(expression,a=None,b=None)`

expression:表达式

默认是不定积分、如果是定积分就输入下限a，上限b

![image-20240114150035490](https://typoracsdnzhihu.oss-cn-nanjing.aliyuncs.com/ing/image-20240114150035490.png)

[之前我们在证明过下面这个结论](https://mp.weixin.qq.com/s/JZX3BvcP5vumN110nHSP3Q):

![image-20240114150411661](https://typoracsdnzhihu.oss-cn-nanjing.aliyuncs.com/ing/image-20240114150411661.png)

因为$n$为正整数,于是我们可以从1遍历循环一下验证结论的正确性:

![image-20240114150744070](https://typoracsdnzhihu.oss-cn-nanjing.aliyuncs.com/ing/image-20240114150744070.png)

`由于我很懒、就写了这么点、之前写了一个简易的gui但是展示不是很美观,后续更新的话可能会更新在github上,https://github.com/kkdominant/math由于公众号跳不了超链接、就放个链接吧`
