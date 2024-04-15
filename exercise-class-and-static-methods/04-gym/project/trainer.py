from project.next_id import NextId

class Trainer(NextId):
    id = 0
    def __init__(self, name):
        self.name = name
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Trainer <{Trainer.id}> {self.name}"