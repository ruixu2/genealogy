class FamilyTree:
    def __init__(self, p):
        self.p=p
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# 创建树的节点
root = Person("祖父")
father = Person("父亲")
mother = Person("母亲")
son = Person("儿子")
daughter = Person("女儿")
grandson = Person("孙子")

# 构建树结构
root.add_child(father)
root.add_child(mother)  # 假设这里也添加了母亲，尽管在典型的父子树中她可能不是父亲的直接子节点
father.add_child(son)
father.add_child(daughter)
son.add_child(grandson)

# 注意：在实际的家谱中，母亲和父亲通常是同一级别的节点，且都可能是祖父或祖母的子节点。
# 上面的树结构是为了简化示例而创建的，不代表真实的家谱结构。

# 遍历树的函数（深度优先搜索）
def traverse_tree(node):
    print(node.name)  # 访问当前节点
    for child in node.children:
        traverse_tree(child)  # 递归访问每个子节点

# 调用遍历函数
traverse_tree(root)