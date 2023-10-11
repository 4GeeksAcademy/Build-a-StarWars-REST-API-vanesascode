from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
###############################################################################

class Starships(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    model = db.Column(db.String(50))
    starship_class = db.Column(db.String(50))
    manufacturer = db.Column(db.String(50))
    cost_in_credits = db.Column(db.Integer)
    length = db.Column(db.Integer)
    crew = db.Column(db.Integer)
    passengers = db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)
    consumables = db.Column(db.Integer)
    # fav_starship = db.Column(db.Integer, db.ForeignKey('fav_starships.id'))
    # fav_starship_relationship = db.relationship("Fav_Starships", uselist=False)


    def __repr__(self):
        return '<Starships %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "starship_class": self.starship_class,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "consumables": self.consumables,
            "fav_starship": self.fav_starship,

        }

class Fav_Starships(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    starship = db.Column(db.Integer, db.ForeignKey('starships.id'))
    starship_relationship = db.relationship(Starships)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_relationship = db.relationship(User)

    def __repr__(self):
        return '<Fav_Starships %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "starship": self.starship,
            "user": self.user,
        }
    
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    diameter = db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    gravity = db.Column(db.String(50))
    population = db.Column(db.Integer)
    climate = db.Column(db.String(50))
    terrain = db.Column(db.String(50))
    surface_water = db.Column(db.Integer)
#     fav_planet = Column(Integer, ForeignKey('fav_planets.id'))
#     fav_planet_relationship = relationship("Fav_planets", uselist=False)


    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
        }
    

class Fav_Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planet_relationship = db.relationship(Planets)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_relationship = db.relationship(User)

    def __repr__(self):
        return '<Fav_Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "planet": self.starship,
            "user": self.user,
        }
    
class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    mass = db.Column(db.Integer)
    height = db.Column(db.Integer)
    hair_color = db.Column(db.String(50))
    skin_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    birth_year = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    planet = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planet_relationship = db.relationship(Planets)
    starship = db.Column(db.Integer, db.ForeignKey('starships.id'))
    starship_relationship = db.relationship(Starships)
#     fav_character = Column(Integer, ForeignKey('fav_characters.id'))
#     fav_character_relationship = relationship("Fav_Characters", uselist=False)


    def __repr__(self):
        return '<Character %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "mass": self.mass,
            "height": self.height,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "planet": self.planet,
            "starship": self.starship,
        }

class Fav_Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character = db.Column(db.Integer, db.ForeignKey('characters.id'))
    character_relationship = db.relationship(Characters)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_relationship = db.relationship(User)

    def __repr__(self):
        return '<Fav_Characters %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "character": self.character,
            "user": self.user,
        }


    
################################################################################

# STAR WARS DATABASE: 
    
# class Users(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), unique=True)
#     email = Column(String(50), unique=True)

# class Starships(Base):
#     __tablename__ = 'starships'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), unique=True, nullable=False)
#     model = Column(String(50))
#     starship_class = Column(String(50))
#     manufacturer = Column(String(50))
#     cost_in_credits = Column(Integer)
#     length = Column(Integer)
#     crew = Column(Integer)
#     passengers = Column(Integer)
#     cargo_capacity = Column(Integer)
#     consumables = Column(Integer)
#     fav_starship = Column(Integer, ForeignKey('fav_starships.id'))
#     fav_starship_relationship = relationship("Fav_tarships", uselist=False)

# class Fav_Starships(Base):
#     __tablename__ = 'fav_starships'
#     id = Column(Integer, primary_key=True)
#     starship = Column(Integer, ForeignKey('starships.id'))
#     starship_relationship = relationship(Starships)
#     user = Column(Integer, ForeignKey('users.id'))
#     user_relationship = relationship(Users)
    
    
# class Planets(Base):
#     __tablename__ = 'planets'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), unique=True, nullable=False)
#     rotation_period = Column(Integer)
#     diameter = Column(Integer)
#     rotation_period = Column(Integer)
#     gravity = Column(String(50))
#     population = Column(Integer)
#     climate = Column(String(50))
#     terrain = Column(String(50))
#     surface_water = Column(Integer)
#     fav_planet = Column(Integer, ForeignKey('fav_planets.id'))
#     fav_planet_relationship = relationship("Fav_planets", uselist=False)

# class Fav_Planets(Base):
#     __tablename__ = 'fav_planets'
#     id = Column(Integer, primary_key=True)
#     planet = Column(Integer, ForeignKey('planets.id'))
#     planet_relationship = relationship(Planets)
#     user = Column(Integer, ForeignKey('users.id'))
#     user_relationship = relationship(Users)
    
# class Characters(Base):
#     __tablename__ = 'characters'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), unique=True)
#     mass = Column(Integer)
#     height = Column(Integer)
#     hair_color = Column(String(50))
#     skin_color = Column(String(50))
#     eye_color = Column(String(50))
#     birth_year = Column(String(50))
#     gender = Column(String(50))
#     planet = Column(Integer, ForeignKey('planets.id'))
#     planet_relationship = relationship(Planets)
#     starship = Column(Integer, ForeignKey('starships.id'))
#     starship_relationship = relationship(Starships)
#     fav_character = Column(Integer, ForeignKey('fav_characters.id'))
#     fav_character_relationship = relationship("Fav_Characters", uselist=False)
    

# class Fav_Characters(Base):
#     __tablename__ = 'fav_characters'
#     id = Column(Integer, primary_key=True)
#     character = Column(Integer, ForeignKey('characters.id'))
#     character_relationship = relationship(Characters, uselist=False)
#     user = Column(Integer, ForeignKey('users.id'))
#     user_relationship = relationship(Users)
