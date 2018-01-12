"""Classes for melon orders."""

class AbstractMelonOrder(object):
    """Abstract base class that other melon orders inherit from"""

    def __init__(self, species, qty, country_code=None):
        """Initializes all melon orders"""

        self.species = species
        self.qty = qty
        self.shipped = False
        if country_code:
            self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == 'Christmas':
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17
    country_code = 'You forgot to assign a country code!'
    flat_fee = 3

    def get_total(self):
        """Calculate price with international flat fee"""

        base_price = 5

        if self.species == 'Christmas':
            base_price = base_price * 1.5

        total = ((1 + self.tax) * self.qty * base_price) + flat_fee
        return total


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """Child class for govt only orders"""
    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed
