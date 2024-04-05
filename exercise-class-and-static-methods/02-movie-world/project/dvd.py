class DVD:
    MONTHS = {"1": "January", "2": "February", "3": "March", "4": "April", "5": "May", "6": "June", 
            "7": "July", "8": "August", "9": "September", "10": "October", "11": "November", "12": "December"}
    
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False
    
    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        date_tokens = date.split(".")
        creation_year = int(date_tokens[2])
        creation_month = DVD.number_to_month(date_tokens[1])
        return cls(name, id, creation_year, creation_month, age_restriction)
    
    def number_to_month(number):
        return DVD.MONTHS[number]
    
    def status(value):
        if value == False:
            return "not rented"
        else:
            return "rented"
    
    def __repr__(self):
        result = f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) "
        result += f"has age restriction {self.age_restriction}. Status: {DVD.status(self.is_rented)}"
        return result
