#!/usr/bin/python
import sys
import sqlite3 as db

class Pokemon(object):
    __data = []
    name = ''
    number = 0
    def __init__(self):
        conn = db.connect('pokedex.sqlite')
        query = conn.cursor()
        data = query.execute('SELECT sname.name, pokemon.species_id, pokemon.height, pokemon.weight, pokemon.base_experience, flavor.flavor_text FROM pokemon JOIN pokemon_species as species  ON pokemon.species_id = species.id JOIN pokemon_species_names as sname ON sname.pokemon_species_id = species.id JOIN pokemon_species_flavor_text as flavor ON pokemon.species_id = flavor.species_id WHERE species.generation_id == 1 AND sname.local_language_id == 9 AND flavor.language_id == 9 AND flavor.version_id == 1 ORDER BY pokemon.species_id')
        self.__data = data.fetchall()

    def catch(self, aNumber):
        record = [aRec for aRec in self.__data if aRec[1] == myInput]
        self.name = record[0][0]
        self.number = record[0][1]

    def catchall(self):
        for aMon in self.__data:
            print aMon[0]
    def __str__(self):
        return '''
Name:   %s
ID:     %s
    ''' % (self.name, self.number)


myInput = int(sys.argv[1])
if myInput > 0 and myInput < 152:
    poke = Pokemon()
    poke.catch(myInput)
    poke.catchall()
else:
    print('Please enter 1-151')