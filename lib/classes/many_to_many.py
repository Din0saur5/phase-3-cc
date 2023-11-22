
#Dont forget to pip install statistics
#also tests

from statistics import mean
class Customer:
#all customers used for top negative reviewer bonus class method
    all=[]
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        type(self).all.append(self)
        
#validate first name input as str and btw 1-25 char        
    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, str) and len(first_name) in range(1,26):
            self._first_name = first_name
        else:
            raise Exception("first name must be a str and between 1-25 characters")

#validate last name input same as first name
    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self, last_name):
        if isinstance(last_name, str) and len(last_name) in range(1,26):
            self._last_name = last_name
        else:
            raise Exception("first name must be a str and between 1-25 characters")

#list of all reviews using list comp and Review all class variable
    def reviews(self):
         return [review for review in Review.all if review.customer is self]

#list of restaurants reviewed duplicated removed with set functionality 
    def restaurants(self):
        return list({review.restaurant for review in self.reviews()})

#int num of negative reviews made by a customer 
    def num_negative_reviews(self):
        return len([review for review in self.reviews() if review.rating <=2])
#bool value of wheter or not the customer has reviewed a restaurant
    def has_reviewed_restaurant(self, restaurant):
        return True if restaurant in self.restaurants() else False

#class method for finding top reviewer     
    @classmethod
    def top_negative_reviewer(cls):
        negs = [cust for cust in cls.all if cust.num_negative_reviews()> 0]
        if len(negs) != 0:
            return max(negs, key = lambda n: n.num_negative_reviews())
        else:
            return None
class Restaurant:
#class variable used for class method to find top two resturants
    all = []
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

#validate restaurant name input        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name, str) and len(name)>0:   
            self._name = name
        else:
            raise Exception("Restaurant name must be str with 1 or more characters")    

#list of reviews for resturant from source of truth    
    def reviews(self):
        return [review for review in Review.all if review.restaurant is self]

#list of customers who reviewed restaurant
    def customers(self):
        return list({review.customer for review in self.reviews()})

#returns average rating if there are no ratings it returns 0.0
    def average_star_rating(self):
        if len(self.reviews()) > 0:
            avg = round(mean(map(float, [review.rating for review in self.reviews()])), 1) 
        else:
            avg = 0.0
        return avg
    
#returns up to the top two resturants in decending order (best to worst) 
    @classmethod
    def top_two_restaurants(cls):
        top2= sorted(cls.all, key= lambda n: n.average_star_rating(), reverse=True)[:2]
        return top2 if Review.all!=[] else None

class Review:
#class variable to be used by the other classes as source of truth for all reviews
    all=[]
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        type(self).all.append(self)
        
#validate customer input as Customer class instance
    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self,customer):
        if isinstance(customer, Customer):   
            self._customer = customer
        else:
            raise Exception("customer must be Customer class obj")    

#validate restaurant input as Restaurant class instance    
    @property
    def restaurant(self):
        return self._restaurant
    @restaurant.setter
    def restaurant(self,restaurant):
        if isinstance(restaurant, Restaurant):   
            self._restaurant = restaurant
        else:
            raise Exception("restaurant must be Restaurant class obj")    

#validate rating as int 1-5 and cannot be changed
    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self, rating):
        if isinstance(rating, int) and rating in range(1,6) and not hasattr(self, "rating"):
            self._rating = rating
        else:
            raise Exception("rating must be int from 1-5 and not already assigned")
