import math
class RecommendationEngine:
  def __init__(self, restaurants, user):
    self.restaurants = restaurants
    self.user = user

  def sortRestaurants():
    restaurantScores = [score(x) for x in self.restaurants]
    restaurantScorePairs = zip(self.restaurants,restaurantScores)
    sortedPairs = sorted(restaurantScorePairs, lambda x, y: cmp(x[1],y[1]))
    return zip(*sortedPairs)[0] #zip(*) is unzipping

  def score(restaurant):
    weights = []
    weights.append(1.0); #cuisine weight
    weights.append(1.0); #rating weight
    weights.append(-1.0); #distance weight
    weights.append(-1.0); #price weight

    values = [] 
    values.append(self.cosineSimilarity(self.getCuisineVector(),
                                        user.getCuisineVector()))
    values.append(rating);
    values.append(distance);
    values.append(math.abs(user.getPrice() - price));
    return dotProduct(weights, values)

  def cosineSimilarity(xs, ys):
    return dotProduct(xs, ys) / (math.sqrt(self.dotProduct(xs, xs)) * math.sqrt(self.dotProduct(ys, ys)))

  def dotProduct(xs, ys):
    sum = 0.0
    for i in range(xs.size()): 
      sum += xs[i] * ys[i]
    return sum
   
  
