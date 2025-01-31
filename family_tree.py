from person import Person
class FamilyTree:
    def __init__(self, mom=None,papa=None):
        self.mom=mom
        self.papa=papa
        self.mom_mom=None
        self.mom_papa=None
        self.papa_mom=None
        self.papa_papa=None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
    def add_mom_mom(self,p):
        self.mom_mom=p
    def add_mom_papa(self,p):
        self.mom_papa=p
    def add_papa_mom(self,p):
        self.papa_mom=p
    def add_papa_papa(self,p):
        self.papa_papa=p
    
    
    


# 创建树的节点
root = Person(name="祖父")
father = Person(name="父亲")
mother = Person(name="母亲")
son = Person(name="儿子")
daughter = Person(name="女儿")
grandson = Person(name="孙子")

ft=FamilyTree(papa=root)
# 构建树结构
ft.add_child(father)
ft.add_child(mother)  # 假设这里也添加了母亲，尽管在典型的父子树中她可能不是父亲的直接子节点

f=FamilyTree(papa=father)

f.add_child(son)
f.add_child(daughter)


# 注意：在实际的家谱中，母亲和父亲通常是同一级别的节点，且都可能是祖父或祖母的子节点。
# 上面的树结构是为了简化示例而创建的，不代表真实的家谱结构。

# 遍历树的函数（深度优先搜索）
def traverse_tree(node):
    print(node.name)  # 访问当前节点
    for child in node.children:
        traverse_tree(child)  # 递归访问每个子节点

# 调用遍历函数
traverse_tree(root)