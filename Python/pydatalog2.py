from pyDatalog import pyDatalog

#declarar cuáles son los términos (work_in), nombres de los predicados y variables que utilizaremos

pyDatalog.create_terms('X, Y, Z, is_, faster_than, is_named, faster_than_named') #todo lo que vas a ocupar

#se escriben hechos

+ is_('Steamboat','Titanic')
+ is_('Sailboat','Mistral')
+ is_('Rowboat','PondArrow')
+ faster_than('Steamboat', 'Sailboat')
+ faster_than('Sailboat', 'Rowboat')
+ faster_than('Steamboat', 'Rowboat')
+ faster_than('Titanic', 'Mistral')
+ faster_than('Mistral', 'PondArrow')
+ faster_than('Titanic', 'PondArrow')

#is_named(X,Y) <= is_(X,Y) #x es el nombre de y, si  x significa y
#is_named(X,Y) <= is_(X,Z) & is_named(Z,Y) #recursiva

#faster_than_named(X,Y) <= is_(X,Y) #x es el nombre de y, si  x significa y
#faster_than_named(X,Y) <= is_(X,Z) & faster_than_named(Z,Y) #recursiva


print(faster_than(X,'PondArrow')) #pregunta, ¿quién es más rápido que PondArrow?
