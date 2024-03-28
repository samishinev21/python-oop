
from dough import Dough
from pizza import Pizza
from topping import Topping

d = Dough("Sugar", "Mixing", 20)
t = Topping("Tomato", 20)
p = Pizza("Burger", d, 200)
p.add_topping(t)

print(p.toppings["Tomato"], 20)
print(len(p.toppings), 1)