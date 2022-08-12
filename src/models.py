import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    user = relationship(User)
    user_id = Column(Integer, ForeignKey('user.id'))
    favorite_planets = Column(Integer, ForeignKey('planets.id'))
    Favorite_people = Column(Integer, ForeignKey('people.id'))

class Vehicles(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    cargo_capacity = Column(String(250), nullable=False) 
    consumables = Column(String(250), nullable=False) 
    cost_in_credits = Column(String(250), nullable=False) 
    crew = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    max_atmosphering_speed = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)
    pilots = Column(Integer, ForeignKey('people.id'))
    films = Column(String(250), nullable=False) 
    url = Column(String(250), nullable=False) 
    vehicle_class = Column(String(250), nullable=False)

class People(Base):
    __tablename__ = 'people'
    
    id = Column(Integer, primary_key=True)
    birth_year = Column(Integer, primary_key=True)
    eye_color = Column(String(250), nullable=False)
    films = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False) 
    homeworld = Column(String(250), nullable=False)
    mass = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    starships = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    vehicles = relationship(Vehicles)
    species = relationship("Species", backref="vehicles")
    species_id = Column(Integer, ForeignKey('species.id'))

        
class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    climate = Column(String(250), nullable=False)
    diameter = Column(Integer, primary_key=True)
    films = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    population = Column(Integer, primary_key=True)
    people_id = Column(Integer, ForeignKey('people.id'))
    residents = relationship(People)
    rotation_period = Column(String(250), nullable=False)
    surface_water = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)

class Species(Base):
    __tablename__ = 'species'

    id = Column(Integer, primary_key=True)
    average_height = Column(String(250), nullable=False)
    average_lifespan = Column(String(250), nullable=False) 
    classification = Column(String(250), nullable=False)
    designation = Column(String(250), nullable=False)
    eye_colors = Column(String(250), nullable=False) 
    hair_colors = Column(String(250), nullable=False)  
    language = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False) 
    films = Column(String(250), nullable=False) 
    skin_colors = Column(String(250), nullable=False) 
    url = Column(String(250), nullable=False)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    homeworld = relationship(Planets)
    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship(People) 


render_er(Base, 'diagram.png')