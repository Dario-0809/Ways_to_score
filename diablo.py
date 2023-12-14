# .Incomplete

class Gold:
    def __init__(self, gold) -> None:
        self.gold = gold

    def decrease_gold(self, c):
        self.gold = self.gold - c

class Sword(Gold):
    def __init__(self, d) -> None:
        self.durability = d
    
    def max_power_sword(self, d):
        self.durability = d
        return self.durability

    def defeat_monster(self, k):
        self.durability = self.durability - k
    
    def repair_sword(self):
        if self.durability <= 0:
            return -1
        else:
            return self.max_power_sword
        
game = str(input())
m, d, k, c = map(int, game.split())

