class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY
    
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY
    
    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.__find_customer_by_id(customer_id)
        dvd = self.__find_dvd_by_id(dvd_id)
        if dvd.is_rented and dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        elif dvd.is_rented:
            return "DVD is already rented"
        elif customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        else:
            customer.rented_dvds.append(dvd)
            dvd.is_rented = True
            return f"{customer.name} has successfully rented {dvd.name}"        

    def __find_customer_by_id(self, id):
        for customer in self.customers:
            if customer.id == id:
                return customer
            
    def __find_dvd_by_id(self, id):
        for dvd in self.dvds:
            if dvd.id == id:
                return dvd   

    def return_dvd(self, customer_id, dvd_id):
        customer = self.__find_customer_by_id(customer_id)
        dvd = self.__find_dvd_by_id(dvd_id)
        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"
        else:
            return f"{customer.name} does not have that DVD"
        
    def __repr__(self):
        result = ""
        for index, customer in enumerate(self.customers):
            result += f"{customer}\n"
        for index, dvd in enumerate(self.dvds):
            result += f"{dvd}\n"

        return result