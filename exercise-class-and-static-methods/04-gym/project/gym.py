class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []
    
    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)
    
    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):                                                  
        result = ""
        sub = None
        plan = None

        for subscription in self.subscriptions:
            if subscription.id == subscription_id:
                result += f"{subscription}\n"
                sub = subscription

        for customer in self.customers:
            if customer.id == sub.customer_id:
                result += f"{customer}\n"

        for trainer in self.trainers:
            if trainer.id == sub.trainer_id:
                result += f"{trainer}\n"

        plan_result = ""

        for current_plan in self.plans:
            if sub.exercise_id == current_plan.id:
                plan = current_plan
                plan_result += f"{plan}\n"

        for equipment in self.equipment:
            if plan.equipment_id == equipment.id:
                result += f"{equipment}\n"

        result += plan_result

        return result