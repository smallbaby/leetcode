# -*- coding: utf-8 -*-
# __author__ = 'kai.zhang01'
# create date = 2018/03/15
# 毕业后工作好多年。使用二叉树的场景比较少，最近想起来，温习下
'''
二叉树的特点：
1、左、右树，二叉查找树
2、左不空，永远小于根节点的值
3、右不空，永远大于根节点的值
优势在于查找、插入数据的时间复杂度 O(log n)
常用的有查找树、平衡树、红黑树等

python来实现二叉树



'''
# 节点对象
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # add insert def
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        if data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def find(self, data, parent = None):
        '''
        查找
        :param data:
        :param parent:
        :return:
        '''
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.find(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.find(data, self)
        else:
            return self, parent

    def child_cnt(self):
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    def delete(self, data):
        '''
        删除节点
        1.无子节点  直接删
        2. 有一个，将下一个移到当前位置
        3. 有2个，对数据判断，排序
        :param data:
        :return:
        '''
        # 先找到节点
        node, parent = self.find(data)
        if node is not None:
            # 判断这个node下有多少个子节点
            c_cnt = node.child_cnt()
            if c_cnt == 0:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            elif c_cnt == 1:
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
            else:
                # 2个子节点
                parent = node
                succ = node.right
                while succ.left:
                    parent = succ
                    succ = succ.left
                node.data = succ.data
                if parent.left == succ:
                    parent.left = succ.right
                else:
                    parent.right = succ.right

    def compare_trees(self, node):
        '''
        比较
        :param node:
        :return:
        '''
        if node is None:
            return False
        if self.data != node.data:
            return False
        res = True

        if self.left is None:
            if node.left:
                return False
        else:
            res = self.left.compare_trees(node.left)
        if not res:
            if self.right is None:
                if node.right:
                    return False
            else:
                res = self.right.compare_trees(node.right)
        return res

    # 打印
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print self.data
        if self.right:
            self.right.print_tree()


    def tree_data(self):
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node.data
                node = node.data

    def pre_loop(self, node):
        if node == None:
            return

        stack = []

        while node or stack:
            while node:
                print node.data # 前序
                stack.append(node)
                node = node.left
            node = stack.pop()
            #print node.data # 中序
            node = node.right





    def later_loop(self, node):
        if node == None:
            return
        s1 = []
        s2 = []
        s1.append(node)
        while s1:
            node = s1.pop()
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
            s2.append(node)
        while s2:
            print s2.pop().data



    def level_loop(self, node):
        if node is None:
            return

        q = []
        q.append(node)

        while q:
            node = q.pop(0)
            print node.data
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)







# 1 创建单节点，左右为空
root = Node(10)
'''
    None<--⑩->None

'''
root.insert(2)
print root.data, root.left.data

root.insert(11)
root.insert(12)
print root.loop(22)
