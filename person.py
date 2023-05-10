class Person:
    def __init__(self, name, gender, birthdate=None, deathdate=None, occupation=None, father=None, mother=None, spouses=None, children=None, biography=None):
        self.name = name  # 姓名
        self.gender = gender  # 性别，用字符串表示，如 '男' 或 '女'
        self.birthdate = birthdate  # 出生日期，用 datetime.date 对象表示
        self.deathdate = deathdate  # 死亡日期，用 datetime.date 对象表示，若未逝世则为 None
        self.father = father  # 父亲，用 Person 对象表示，若未知则为 None
        self.mother = mother  # 母亲，用 Person 对象表示，若未知则为 None
        self.spouses = spouses or []  # 配偶，用 Person 对象的列表表示
        self.children = children or []  # 子女，用 Person 对象的列表表示
        self.occupation =occupation  # 职业，用字符串表示
        self.biography =biography  # 生平事迹，用字符串表示
