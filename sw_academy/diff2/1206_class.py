import sys
sys.stdin = open("input.txt", "r")

class Building:
    good_view_count = 0

    def __init__(self, level):
        self.level = level
        self.left = None
        self.right = None
        self.view_count = 256
    
    def delete(self):
        Building.good_view_count += self.view_count
        del self
    
    # def __del__(self):
    #     Building.good_view_count += self.view_count
    #     # print(f"del building {self.level} - view_count : {self.view_count}")
    
    def addRight(self, right):
        self.right = right
        right.left = self

        Building.compare(self, right)
        if self.left is not None:
            Building.compare(self.left, right)
            self.left.delete()
    
    @staticmethod
    def compare(left, right):
        diff = left.level - right.level
        if diff >= 0:
            left.view_count = min(left.view_count, diff)
            right.view_count = 0
        else:
            diff *= -1
            right.view_count = min(right.view_count,diff)
            left.view_count = 0

             

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    buildings = list(map(int, input().split()))
    pointer = Building(0)
    for building in buildings:
        new_building = Building(building)
        pointer.addRight(new_building)
        pointer = new_building
    print(f"#{test_case} {Building.good_view_count}")
    Building.good_view_count = 0
        