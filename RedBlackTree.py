__author__ = 'student'

class RedBlackTree():
    def __init__(self, left, right, root, color):
        self.left = left
        self.right = right
        self.root = root
        self.color = color
    def toblack(self):
        self.color = False
    def tored(self):
        self.color = True
    def singlerightrotation(self):
        right = self.right
        left = self.left
        leftleft = left.left
        leftleftleft = leftleft.left
        leftleftright = leftleft.right
        leftright = left.right
        self.root = left.root
        self.left = RedBlackTree(leftleftleft, leftleftright, leftleftleft.root, False)
        self.right = RedBlackTree(leftright, right, self.root, False)
        self.color = True
    def singleleftroration(self):
        left = self.left
        right = self.right
        rightright = right.right
        rightrightright = rightright.right
        rightrightleft = rightright.left
        rightleft = right.left
        self.root = right.root
        self.color = True
        self.left = RedBlackTree(left, rightleft,self.root, False)
        self.right = RedBlackTree(rightrightleft, rightrightright, rightright.root, False)
    def doublebotrotation(self):
        right = self.right
        left = self.left
        leftleft = left.left
        leftright = left.right
        leftrightleft = leftright.left
        leftrightright = leftright.right
        self.root = leftright.root
        self.color = True
        self.left = RedBlackTree(leftleft, leftrightleft,left.root, False)
        self.left = RedBlackTree(leftrightright, right, self.root, False)
    def doubletoprotation(self):
        left = self.left
        right = self.right
        rightright = right.right
        rightleft = right.left
        rightleftright = rightleft.right
        rightleftleft = rightleft.left
        self.root = rightleft.root
        self.color = True
        self.left = RedBlackTree(left, rightleftleft, self.root, False)
        self.right = RedBlackTree(rightleftright, rightright, right.root, False)
    def balance(self):
        left = self.left
        right = self.right
        if left is None or right is None:
            pass
        else:
            leftleft = left.left
            leftright = left.right
            rightright = right.right
            rightleft = right.left

