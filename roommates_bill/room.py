class Bill:
    """
    Object that contains data about a bill, such as
    total amount and period of bill.
    """
    def __init__(self, service, amount, period):
        self.service = service
        self.amount = int(amount)
        self.period = period


class Roommate:
    """
    Creates a roommate person who lives in the home
    and pays a share of a bill.
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, roommate):
        weight = self.days_in_house / (self.days_in_house + roommate.days_in_house)
        to_pay = round(bill.amount * weight,2)
        return to_pay