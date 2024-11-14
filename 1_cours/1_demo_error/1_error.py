#visualiser la gestion des erreurs en python

v = 0
w = 42
x = 'a'

#(w/v) + x

try:
    (w/v) + x
    print("Ok pas erreur")
except TypeError:
    print("Merci d'utiliser des chiffres")
except ZeroDivisionError:
    print("Division par 0")
finally:
    print("Script terminé")
