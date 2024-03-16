from PyQt5.QtGui import *


class LR:
    def __init__(self):
        self.formula = []  # 存储产生式
        self.dot_formula = []  # 存储带.的产生式
        self.VN = []  # 非终结符集
        self.VT = []  # 终结符集
        self.V = []  # 终结符和非终结符集
        self.items = []  # 存储LR0项目集规范族
        self.ver = []  # 存放自动机转换函数
        self.table = []  # 存放LR(0)分析表

    def get_formula(self):
        with open("grammar.txt", "r") as f:
            for line in f:
                line = line.replace('\n', "")
                self.formula.append(line)
            f.close()

    def print_formula(self, ui):
        ui.textEdit_2.setText("输入的文法为：")
        for gram in self.formula:
            ui.textEdit_2.append(gram)

    # 划分终结符和非终结符
    def get_v(self):
        for s in self.formula:
            x, y = s.split("->")
            if x not in self.VN:
                self.VN.append(x)

            for v in y:
                if v.isupper():
                    if v not in self.VN:
                        self.VN.append(v)
                else:
                    if v not in self.VT:
                        self.VT.append(v)
        self.VT.append("#")
        self.V.extend(self.VN)
        self.V.extend(self.VT)

    # 为所有产生式加点
    def dot_gram(self):
        str0 = "S'->." + self.formula[0][0]
        self.dot_formula.append(str0)
        str1 = "S'->" + self.formula[0][0] + "."
        self.dot_formula.append(str1)

        for gram in self.formula:
            for i in range(len(gram) - 2):
                tmp = gram[:3 + i] + "." + gram[3 + i:]
                self.dot_formula.append(tmp)

    # 返回非终结符产生的A->.aBb形式
    def get_VN_gram(self, v):
        res = []
        for gram in self.dot_formula:
            index = gram.find("->")
            if gram[0] == v and gram[index + 2] == ".":
                res.append(gram)
        return res

    # CLOSURE函数
    def Closure(self, I):
        closure = I
        for it in I:
            if it not in closure:
                closure.append(it)
            x, y = it.split(".")
            if y == "":
                continue
            v = y[0]
            if v in self.VN:
                res = self.get_VN_gram(v)
                for re in res:
                    if re not in closure:
                        closure.append(re)
        return closure

    # Go函数
    def Go(self, I, v):
        tmp = []
        for it in I:
            x, y = it.split(".")
            if y != "":
                if y[0] == v:
                    new_it = x + y[0] + "." + y[1:]
                    tmp.append(new_it)

        if len(tmp) != 0:
            new_item = self.Closure(tmp)
            return new_item

    # 判断item是否已经存在, 存在返回位置，不存在返回-1
    def is_inItems(self, new_item):
        if new_item is None:
            return -1
        new_set = set(new_item)
        num = 0
        for item in self.items:
            old_set = set(item)
            if old_set == new_set:
                return num
            num = num + 1
        return -1

    # 添加DFA的转换函数
    def myAppend(self, xx, v, xy):
        t = []
        t.append(xx)
        t.append(v)
        t.append(xy)
        self.ver.append(t)

    # 构建item的集合
    def get_items(self):
        # 初始化,生成I0
        item = []
        item.append(self.dot_formula[0])
        it = self.Closure(item)
        num = 0
        self.items.append(it)
        num = num + 1
        for item in self.items:
            for v in self.V:
                new_item = self.Go(item, v)
                # 判断状态不为空
                if new_item is not None:
                    if self.is_inItems(new_item) == -1:
                        self.items.append(new_item)
                        x = self.is_inItems(item)
                        y = self.is_inItems(new_item)
                        self.myAppend(x, v, y)
                        num = num + 1
                    else:  # 存在于状态集items中
                        x = self.is_inItems(item)
                        y = self.is_inItems(new_item)
                        self.myAppend(x, v, y)

    # 输出LR(0)项目集规范族
    def print_items(self, ui):
        ui.textEdit_2.append("\nLR(0)项目集规范族:")
        for i in range(len(self.items)):
            ui.textEdit_2.append("closure-I{0}: {1}".format(i, self.items[i]))

    # 输出DFA的转换函数形式
    def print_ver(self, ui):
        ui.textEdit_2.append("\n自动机转换函数形式:")
        for f in self.ver:
            ui.textEdit_2.append("f(I{0}, {1})=I{2}".format(f[0], f[1], f[2]))

    # 判断文法是否为LR(0)
    def judge_isLR0(self, ui):
        for item in self.items:
            shiftNum = 0
            protocolNum = 0
            for it in item:
                x, y = it.split(".")
                if y == "":
                    protocolNum = protocolNum + 1
                elif y[0] in self.VT:
                    shiftNum = shiftNum + 1
            if protocolNum > 1 or (protocolNum >= 1 and shiftNum >= 1):
                ui.textEdit_3.setText("该文法不是LR(0)的!")
                return -1
        ui.textEdit_3.setText("该文法是LR(0)的!")
        return 1

    def is_informula(self, new_gram):
        if new_gram is None:
            return -1
        for i in range(len(self.formula)):
            if new_gram == self.formula[i]:
                return i
        return -1

    # 创建LR(0)分析表
    def creat_table(self):
        tmp = []
        tmp1 = []
        index_tmp1 = 0
        for item in self.items:
            t = []
            for it in item:
                x, y = it.split(".")
                if y == "":
                    if it == self.dot_formula[1]:
                        t.append("-1")
                    else:
                        t.append("0")
                        new_gram = x + y
                        tmp1.append(self.is_informula(new_gram))

                else:
                    t.append(y[0])
            tmp.append(t)
        for index_temp in range(len(tmp)):
            t = []
            for v in self.VT:
                # S'->E. 接受项目
                if "-1" in tmp[index_temp]:
                    if v == "#":
                        t.append("acc")
                    else:
                        t.append("")
                # .在最后，规约项目
                elif "0" in tmp[index_temp]:
                    for vt in self.VT:
                        t.append("R" + str(tmp1[index_tmp1] + 1))
                    index_tmp1 = index_tmp1 + 1
                    break
                # .后面为终结符 移进项目
                elif v in tmp[index_temp]:
                    for f in self.ver:
                        if f[0] == index_temp and f[1] == v:
                            t.append("S" + str(f[2]))
                            break
                else:
                    t.append("")
            # .后面为非终结符 待约项目
            for v in self.VN:
                if v in tmp[index_temp]:
                    for f in self.ver:
                        if f[0] == index_temp and f[1] == v:
                            t.append(str(f[2]))
                            break
                else:
                    t.append("")
            self.table.append(t)

    # 打印LR(0)分析表
    def print_table(self, ui):
        # 显示在表格上
        label_x = self.VT + self.VN
        model = QStandardItemModel(len(self.items), len(self.VN) + len(self.VT))
        model.setHorizontalHeaderLabels(label_x)
        label_y = []
        for i in range(len(self.items)):
            label_y.append(str(i))
        model.setVerticalHeaderLabels(label_y)
        for i in range(len(self.items)):
            for j in range(len(self.V)):
                model.setItem(i, j, QStandardItem(self.table[i][j]))
        ui.tableView.setModel(model)

    # 按格式输出字符串分析信息
    def print_analyseinfo(self, status_stack, output_stack, input_stack, string, model, v):
        s = "".join(status_stack)
        o = "".join(output_stack)
        reverse_input_stack = input_stack[::-1]
        i = "".join(reverse_input_stack)
        list = [s, o, i, "wrong" if string == "" else string]
        for j in range(4):
            model.setItem(v, j, QStandardItem(list[j]))

    # LR(0)分析过程
    def analyse(self, ui):
        status_stack = ['0']
        input_stack = ['#']
        output_stack = ['#']
        v = []
        v.extend(self.VT)
        v.extend(self.VN)
        f = open("./string.txt", 'r')
        string = f.read()
        f.close()
        for s in string[::-1]:  # 逆序
            if s in self.VT:
                input_stack.append(s)
            else:
                # 字符串含有其它终结符
                ui.textEdit_3.setText("输入串不是该文法的句子！")
                return
        label_x = ["状态栈", "符号栈", "输入串", "Action/Goto"]
        model = QStandardItemModel(len(self.items), 4)
        model.setHorizontalHeaderLabels(label_x)
        j = 0
        while True:
            s1 = status_stack[-1]  # 状态栈
            s2 = input_stack[-1]  # 输入栈
            index1 = int(s1)  # 第几个项目集
            index2 = v.index(s2)  # s2在V中的位置
            string = self.table[index1][index2]  # 获得对应的table表中的信息
            self.print_analyseinfo(status_stack, output_stack, input_stack, string, model, j)
            j = j + 1
            if string == "":
                ui.textEdit_3.setText("输入串不是该文法的句子！")
                # ui.tableView_2.setModel(model)
                break
            elif string[0] == "S":  # Action[s,a]
                status_stack.append(string[1])
                input_stack.pop()
                output_stack.append(s2)
            elif string[0] == "R":
                x, y = self.formula[int(string[1]) - 1].split("->")
                status_stack = status_stack[:-len(y)]  # 出栈
                output_stack = output_stack[:-len(y)]  # 出栈
                input_stack.append(x)  # 进栈
            elif string == "acc":
                ui.textEdit_3.setText("输入串是该文法的句子！")
                break
            else:
                status_stack.append(string)
                input_stack.pop()
                output_stack.append(s2)
        ui.tableView_2.setModel(model)

    def main(self, ui):
        self.get_formula()
        self.print_formula(ui)
        self.get_v()
        self.dot_gram()
        self.get_items()
        self.print_items(ui)
        self.print_ver(ui)
        if self.judge_isLR0(ui) == 1:
            self.creat_table()
            self.print_table(ui)


def main(ui):
    lr = LR()
    lr.main(ui)
    return lr

