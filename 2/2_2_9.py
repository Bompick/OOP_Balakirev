class TreeObj:
    def __init__(self, indx, value: str | None = None):
        if type(indx) is int:
            self.indx = indx

        self.value = value
        self.left = None  # ссылка на следующий объект дерева по левой ветви
        self.right = None  # ссылка на следующий объект дерева по правой  ветви

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
    tree = None

    @classmethod
    def predict(cls, root, x):
        link = root
        q = 0
        while link.left or link.right is not None:
            if x[q] == 1:
                link = link.left
                q = q+1
            elif x[q] == 0:
                link = link.right
                q = q + 2

        return link.value

    @classmethod
    def add_obj(cls, obj: TreeObj, node=None, left=True):
        if not cls.tree:
            cls.tree = obj
            return obj
        if left:
            node.left = obj
            return obj
        else:
            node.right = obj
            return obj


root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "программист"), v_11)
DecisionTree.add_obj(TreeObj(-1, "кодер"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "посмотрим"), v_12)
DecisionTree.add_obj(TreeObj(-1, "нет"), v_12, False)

x = [0,1,1]
print(DecisionTree.predict(root, x))


