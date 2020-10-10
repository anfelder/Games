# adding from x import * statements here causes any higher level "import Classes.Creatures.Animals" statements
# to import everything listed here so it can be done in a single statement
# For example, if main has "import Classes.Creatures.Animals", then all that needs to be done is adding
# an import for a newly created animal here.
# doing "From .Fish import Fish" imports the constructor only I think. You can still access class methods through creature
# probably because animal uses "from Creature import *" if I had to guess.

from .Fish import Fish
from .Animal import Animal
