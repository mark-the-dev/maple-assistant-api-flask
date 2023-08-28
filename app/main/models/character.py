from .. import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    class_name = db.Column(db.String(32), db.ForeignKey('class.name'), nullable=False)
    
    def __repr__(self):
        return f"Character[id={self.id}, name={self.name}, level={self.level}, class_name={self.class_name}, user_id={self.user_id}]"

class Class(db.Model):
    name = db.Column(db.String(32), primary_key=True)
    
    def __repr__(self):
        return f"Class[name={self.name}]"
    
classes = [
    "Adele",
    "Angelic Buster",
    "Aran",  
    "Archmage(F/P)",
    "Archmage(I/L)",
    "Ark",
    "Battlemage",
    "Beast Tamer",
    "Bishop",
    "Blaster",
    "Blaze Wizard",
    "Bowmaster",
    "Buccaneer",
    "Cadena",
    "Cannonneer",  
    "Corsair",
    "Dark Knight",
    "Dawn Warrior",
    "Demon Avenger",
    "Demon Slayer",
    "Dual Blade",
    "Evan",
    "Hayato",
    "Hero",
    "Hoyoung",
    "Illium",
    "Kain",
    "Kaiser",
    "Kanna",
    "Khali",
    "Kinesis",
    "Lara",
    "Luminous",
    "Marksman",
    "Mechanic",
    "Mercedes",
    "Mihile",
    "Night Lord",  
    "Night Walker",
    "Paladin",
    "Pathfinder",
    "Phantom",
    "Shade",
    "Shadower",
    "Thunder Breaker",
    "Wild Hunter",
    "Wind Archer",
    "Xenon",
    "Zero"
]

def load_classes():
    for c in classes:
        db.session.add(Class(name=c))
    db.session.commit()