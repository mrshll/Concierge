import math
from recommendation_item.models import Restaurant

class RecommendationEngine:
  def __init__(self, restaurants, user):
    self.restaurants = restaurants
    self.user_profile = user.get_profile()

  def sortRestaurants(self):
    restaurantScores = [self.score(x) for x in self.restaurants]
    restaurantScorePairs = zip(self.restaurants,restaurantScores)
    sortedPairs = sorted(restaurantScorePairs, lambda x, y: cmp(y[1],x[1]))
    print sortedPairs,
    return zip(*sortedPairs)[0] #zip(*) is unzipping

  def score(self,restaurant):
    weights = []
    weights.append(1.0) #cuisine weight
    weights.append(1.0) #rating weight
    weights.append(-1.0) #price weight

    values = []
    values.append(self.cuisineSimilarity(restaurant.cuisines,
                                         self.user_profile.get_fav_cuisines()))
    values.append(restaurant.rating)
    values.append(math.fabs(self.user_profile.get_avg_price() - restaurant.price))
    return self.dotProduct(weights, values)

  def cuisineSimilarity(self, restaurantCuisines, userCuisines):
    similarity = 0
    for i in restaurantCuisines:
      if i in userCuisines:
        similarity += userCuisines[i]
    return similarity

  def dotProduct(self, xs, ys):
    sum = 0.0
    for i in range(len(xs)):
      sum += xs[i] * ys[i]
    return sum

