class Restaurant:
    # a list of all existing restaurant names
    all = []
    
    def __init__(self, name):
        if type(name) is not str: 
            raise Exception("Invalid name") 
        self._name = name 
        self.reviews = []
        self.customers = []
        
        
        Restaurant.all.append(name)
    
    @property
    def name(self):
        return self._name
    
    @classmethod
    def updateReviews(cls, review): 
        cls.reviews.append(review)
        
    def updateReviews(self, review): 
        self.reviews.append(review)
        
    def get_average_rating(self):
        total = 0

        for review in self.reviews:
            total += review.rating

        average = total / len(self.reviews)

        return average
    
        


    @classmethod
    def get_all_restaurants(cls):
        return cls.all