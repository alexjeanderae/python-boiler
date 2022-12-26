# Polymorphism in Python
# Main idea is that a class can behave differently depending on context. Well kind of. Is actually more on methods.
# It is not a doppelganger substitution ability neither that makes copies of a class neither.
# The better way to look at simply is to sum it up as "this method can work with other object types"

# Here we create a country concept out of two implementations without needing to declare much of it. And can even loop though.
# Both implementations (India, USA) here have the same methods names under it.

class India():
     def capital(self):
       print("New Delhi")
 
     def language(self):
       print("Hindi and English")
 
class USA():
     def capital(self):
       print("Washington, D.C.")
 
     def language(self):
       print("English")
 
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language() 

# >>> New Delhi
# >>> Hindi and English
# >>> Washington, D.C.
# >>> English