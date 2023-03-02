class Customer:

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self.reviews = []
        self.restaurants = []


    @property 
    def first_name(self):
        return self._first_name


    @first_name.setter
    def first_name(self, name): 
        if len(name) <= 1 or len(name) >=25: 
            raise Exception("Invalid")
        if type(name) != str: 
            raise Exception("Invalid")
        self._first_name = name
        

    @property 
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, name):
        if len(name) <= 1 or len(name) >=25: 
            raise Exception("Invalid")
        if type(name) != str: 
            raise Exception("Invalid")
        self._last_name = name
        
  

    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"
   
    def get_num_reviews(self):
        return len(self.reviews)

    def add_review(self, restaurant, rating):
        from classes.review import Review
        review = Review(self, restaurant, rating)
        print(rating)
        self.reviews.append(review)