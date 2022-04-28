import random

"""
나무는 MAX_LEVEL 값에 따라 커질 수록 위로 자라게 됩니다.
나뭇잎은 나무의 가장 말단부(가장 높은 위치)의 나뭇 가지를 의미합니다.

MAX_LEVEL: 나무의 최대 크기
LEAFS: 나뭇 가지에 달리는 다음 단계 나뭇 가지 개수

LEAFS_ANGLE_RANGE: 나무가 무작위로 생성될 때, 허용 가능한 잎의 각도

BRANCH_COLOR: 나뭇 가지 색
LEAF_COLOR: 나뭇잎 색
"""

MAX_LEVEL = 4
LEAFS = 2

LEAFS_ANGLE_RANGE = (-90, 90)

TRUNK_COLOR = (0, 0, 0)
LEAF_COLOR = (0, 0, 0)


class Tree:
    def __init__(self, dna):
        """DNA를 받아 나무를 정의합니다"""

        # dna = {level1: [leaf1, leaf2, ...], level2: [leaf1, leaf2, ...], ...}
        self.dna = {}

        n = 0
        for level in range(MAX_LEVEL):
            self.dna[level] = []
            for leaf in range(level ** (LEAFS - 1)):
                self.dna[level].append(dna[n])
                n += 1

    @staticmethod
    def random():
        """무작위의 나무를 하나 생성합니다"""
        # 나무의 첫번째 부분에 해당하는 몸통은 지표면에서 직각(0)으로 설정
        dna = [0]
        for i in range(LEAFS ** MAX_LEVEL - 1):
            dna.append(random.randint(*LEAFS_ANGLE_RANGE))
        return Tree(dna)

    def get_leafs(self, level):
        """해당하는 레벨의 모든 잎을 불러옵니다"""
        return self.dna[level].copy()

    def render(self, surf, pos, level):
        return
