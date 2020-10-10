# import x as y allows you to use "y.method()" in the code
# in the case of the animals, it allows you to call a constructor with "animals.Fish()" rather than
# Classes.Creatures.Animals.Fish()
# you can technically access the methods in those classes as well, e.g., "animals.Fish.print()", but it will
# fail since there is no instanced object calling it (i.e. it's missing the "self" argument in the method)
import Classes.Creatures.Animals as animals

f = animals.Fish()
f2 = animals.Fish()
f.print_info()
f2.print_info()
a = animals.Animal()
a2 = animals.Animal()
a.print_info()
a2.print_info()
f2.print_type_count()
a2.print_type_count()
