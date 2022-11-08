class TreeObj:

    def __init__(self, index, value = None):
        self.index = index
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left
    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def right(self):
        return self.__right
    @right.setter
    def right(self, value):
        self.__right = value

class DecisionTree:

    @classmethod
    def predict(cls, root, x):
        res = root
        lst = x
        i = 0
        while res.left != None or res.right != None:
            if x[i] == 1:
                i = root.left.index
                res = res.left
            else:
                i = root.right.index
                res = res.right
        return res.value

    @classmethod
    def add_obj(cls, obj, node = None, left = True):
        if node:
            if left == True:
                node.left = obj
            else:
                node.right = obj
        return obj


root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)
x = [1, 1, 0]
res = DecisionTree.predict(root, x) # будет программистом
print(res)