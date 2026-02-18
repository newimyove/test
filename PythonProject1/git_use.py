from ast import literal_eval
from turtledemo.clock import current_day


class Node:

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree:

    def __init__(self):
        self.root = None
        self.help_queue = []

    def level_build(self, node: Node):
        if self.root is None:
            self.root = node
            self.help_queue.append(node)
        else:
            self.help_queue.append(node)
            if self.help_queue[0].lchild is None:
                self.help_queue[0].lchild = node
            else:
                self.help_queue[0].rchild = node
                del self.help_queue[0]

    def pre_order(self, cur_node: Node):
        if cur_node is None:
            return
        print(cur_node.elem, end=' ')
        self.pre_order(cur_node.lchild)
        self.pre_order(cur_node.rchild)

    def mid_order(self, cur_node: Node):
        if cur_node is None:
            return
        self.mid_order(cur_node.lchild)
        print(cur_node.elem,end=' ')
        self.mid_order(cur_node.rchild)

    def post_order(self, cur_node: Node):
        if cur_node is None:
            return
        self.post_order(cur_node.lchild)
        self.post_order(cur_node.rchild)
        print(cur_node.elem, end=' ')

    def level_order(self):
        help_queue=[]
        help_queue.append(self.root)
        while help_queue:
            print(help_queue[0].elem,end=' ')
            if help_queue[0].lchild:
                help_queue.append(help_queue[0].lchild)
            if help_queue[0].rchild:
                help_queue.append(help_queue[0].rchild)
            help_queue.pop(0)
if __name__ == '__main__':
    tree = BinaryTree()
    for i in range(1, 11):
        new_node = Node(i)
        tree.level_build(new_node)
    # print('the result of pre_order:')
    # tree.pre_order(tree.root)
    # print()
    # print('the result of mid_order')
    # tree.mid_order(tree.root)
    # print()
    # tree.post_order(tree.root)
    # print()
    tree.level_order()
