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

        if self.order_type == 'international':
            flat_fee = 3
            total = ((1 + self.tax) * self.qty * base_price) + flat_fee
            return total

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

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
