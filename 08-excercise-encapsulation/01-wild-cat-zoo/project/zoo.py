from lion import Lion
from tiger import Tiger
from cheetah import Cheetah

class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []
    
    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price

            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        
        elif self.__budget < price and self.__animal_capacity > len(self.animals):
            return "Not enough budget"
        
        else:
            return "Not enough space for animal"
        
    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return "Not enough space for worker"
        
    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
            
        return f"There is no {worker_name} in the zoo"
    
    def pay_workers(self):
        due_sum = 0

        for worker in self.workers:
            due_sum += worker.salary

        if self.__budget >= due_sum:
            self.__budget -= due_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"
        
    def tend_animals(self):
        due_sum = 0

        for animal in self.animals:
            due_sum += animal.money_for_care

        if self.__budget >= due_sum:
            self.__budget -= due_sum
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."
        
    def profit(self, amount):
        self.__budget += amount
    
    def animals_status(self):
        result = f"You have {len(self.animals)} animals"

        grouped_animals = {}

        for animal in self.animals:
            class_name = animal.__class__.__name__
            if class_name in grouped_animals:
                grouped_animals[class_name].append(animal)
            else:
                grouped_animals[class_name] = [animal]
        
        for (animal_name, animals) in grouped_animals.items():
            result += f"\n----- {len(animals)} {animal_name}s:\n"
            animals_string = [repr(animal) for animal in animals]
            result += "\n".join(animals_string)

        return result
    
    def workers_status(self):
        result = f"You have {len(self.workers)} workers"

        grouped_workers = {}

        for worker in self.workers:
            class_name = worker.__class__.__name__
            if class_name in grouped_workers:
                grouped_workers[class_name].append(worker)
            else:
                grouped_workers[class_name] = [worker]
        
        for (worker_name, workers) in grouped_workers.items():
            result += f"\n----- {len(workers)} {worker_name}s:\n"
            workers_string = [repr(worker) for worker in workers]
            result += "\n".join(workers_string)

        return result