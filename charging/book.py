from django.conf import settings


class Book:
    CHARGES = settings.CHARGES

    def __init__(self, cost=0):
        # regular charge of the books per day
        self.cost = cost

    def cost_to_rent(self, quantity, duration):
        return self.cost * duration * quantity


class Regular(Book):
    def __init__(self):
        config = self.CHARGES["Regular"]

        super().__init__(config["cost"])

        # Minimum changes will be considered as $ 2 if days rented is less than 2 days
        self.minimum_duration = config["minimum_duration"]
        self.minimum_cost = config["minimum_cost"]

    def cost_to_rent(self, quantity, duration):
        # Handle minimum charge case
        if duration < self.minimum_duration:
            return self.minimum_cost

        # Regular books: for the first 2 days charges will be $ 1 per day
        cost_first_two_days = 2 * 1
        # and $ 1.5 thereafter
        cost_following_days = self.cost * (duration - 2)

        return (cost_first_two_days + cost_following_days) * quantity


class Novels(Book):
    def __init__(self):
        config = self.CHARGES["Novels"]

        super().__init__(config["cost"])

        # Minimum changes will be considered as $ 4.5 if days rented is less than 3 days
        self.minimum_duration = config["minimum_duration"]
        self.minimum_cost = config["minimum_cost"]

    def cost_to_rent(self, quantity, duration):
        # Handle minimum charge case
        if duration < self.minimum_duration:
            return self.minimum_cost

        return self.cost * duration * quantity


class Fiction(Book):
    def __init__(self):
        config = self.CHARGES["Friction"]
        super().__init__(config["cost"])
