from project.next_id import NextId

class Customer(NextId):
    id = 0
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()
    
    def __repr__(self):
        return f"Customer <{Customer.id}> {self.name}; Address: {self.address}; Email: {self.email}"