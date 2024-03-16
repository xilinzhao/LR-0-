# LR(0)语法分析器
(1)根据LR(0)分析法编写一个语法分析程序，输入已知文法，由程序自动构造识别该文法活前缀DFA并生成LR(0)分析表。

(2)所开发的程序可适用于不同的文法和任意输入串，且能判断该文法是否为LR(0)文法。

(3)对输入的任意符号串，所编制的语法分析程序应能正确判断此串是否为文法的句子（句型分析），并要求输出分析过程。

### 使用的基本概念和原理

活前缀：对于任一文法G[S]，若S’经过任意次推导得到αAω，继续经过一次推导得到αβω，若γ是αβ的前缀，则称γ是G的一个活前缀。

LR(0)项目集规范族:对于构成识别一个文法活前缀的DFA项目集(状态)的全体我们称之为这个文法的LR(0)项目集规范族。

LR(0)文法：假若一个文法G的拓广文法G'的活前缀识别自动机中的每个状态(项目集)不存在下述情况︰（1）既含移进项目又含归约项目;（2）含有多个归约项目；则称G是一个LR(0)文法。

总体流程：

![](test/图片1.png)

详细设计:

![](test/图片2.png)

创建LR(0)分析表：

![](test/图片3.png)

黑盒测试等价类划分法：

测试用例：

输入文法：E->aAcBe  A->b  A->Ab  B->d

输入字符串：abcde /abce

预计结果：是LR(0)文法，第一种是文法的句子，第二种不是

运行结果展示：

![](test/图片4.png)

![](test/图片5.png)
