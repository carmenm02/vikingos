
# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        
        self.health = health
        self.strength = strength
    
    def attack(self):
        
        return self.strength
    
    def receiveDamage(self, damage):
        
        self.health = self.health - damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        Soldier().__init__(health, strength)
        self.name = name
    def attack(self):
        return super().attack()
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return "{} ha recibido {} puntos de daño".format(self.name,damage)
        else:
            return "{} murió en combate".format(self.name)
    def battleCry(self):
        return "Odin Owns You All"
    

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier().__init__(self,health, strength)
    def attack(self):
        return super().attack()
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return " Un Saxon recibió {} puntos de daño".format(damage)
        else:
            return "Un Saxon murió en combate"
    

# War


class War(Soldier):
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking (self, viking):
        self.vikingArmy.append(viking)
    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)
    def VikingAttack(self):
        import random
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        result = saxon.receiveDamage(viking.attack())
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result
    def saxonAttack(self):
        import random
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        result = viking.receiveDamage(saxon.attack())
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result
    def shoStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings ganan"
        elif len(self.vikingArmy) == 0:
            return "Saxons ganan"
        elif len(self.vikingArmy) >= 1 and len(self.saxonArmy) >=1:
            return "Continua la batalla"
