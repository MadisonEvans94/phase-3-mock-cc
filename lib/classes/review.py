from classes.customer import Customer
from classes.restaurant import Restaurant

class Review:
    
    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        # adding this instantiated instance to the restaurant's reviews list on creation
        self._restaurant.reviews.append(self)
        self._customer.reviews.append(self)
        self._customer.restaurants.append(self._restaurant)
        self._restaurant.customers.append(self._customer)
        print(self._restaurant.reviews)


    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception("Customer error")
        

    @property
    def restaurant(self):
        return self._restaurant

    @restaurant.setter
    def restaurant(self, restaurant):
        if isinstance(restaurant, Restaurant):
            self._restaurant = restaurant
        else:
            raise Exception("Restaurant error")

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        if rating > 0 and rating < 6:
            self._rating = rating
        else:
            print("Your rating must be a number between 1 and 5, inclusive!")

            raise Exception("Your rating must be a number between 1 and 5, inclusive!")


    def add_customer_to_restaurant(self):
        pass

    def add_review_to_restaurant(self):
        pass

    def add_restaurant_to_customer(self):
        pass

    def add_review_to_customer(self):
        pass
