import cPickle
from scipy.spatial.distance import cosine
from numpy import array

# Collab is an implementation of the memory-based collaboration filtering
# algorithm found at http://en.wikipedia.org/wiki/Collaborative_filtering

class RatingMatrixNotDefinedException(Exception):
  def __init__(self):
    pass

  def __str__(self):
    return "Rating Matrix Not Defined"

class Collab(object):

  ########################################
  # FUNCTIONS FOR OUTSIDE USE (PUBLIC)
  ########################################

  # load a file into the engine, user for side-effect
  # data is [users][items]
  def load_file(self, file_name):
    with open(file_name) as f:
      self.rating_matrix = cPickle.load(f)
      self.user_count = len(self.rating_matrix)
      self.item_count = len(self.rating_matrix[0])

  # predicts the rating of the reccomendation item at index i
  # by the user whose index is u
  # returns actual rating if that item is already rated
  # this rating is not stored in the rating matrix
  def predict_rating(self, i, u):
    if not self.rating_matrix:
       raise RatingMatrixNotDefinedException

    # find top n users most similar to u that have rated item i
    relevant_users = [ x for x in range(self.user_count)
                                  if not x == u and self._get_rating(i,x) ]
    top_n_most_sim = sorted(relevant_users,
                            key=lambda x: abs(self._user_user_sim(u,x)),
                            reverse=True)[:self.n]

    # return a weighted average of the ratings of the item in question
    weighted_sum = 0.0
    sum_of_weights = 0.0
    for user in top_n_most_sim:
      weight = self._user_user_sim(u, user)
      sum_of_weights += weight
      weighted_sum += weight * self._get_rating(i, user)
    return weighted_sum / sum_of_weights

  # returns true if a user u has recommended reccomendation item i
  # else returns false
  def has_reccomended(self, i, u):
    return False

  #########################################
  # FUNCTIONS NOT FOR OUTSIDE USE (PRIVATE)
  #########################################

  # user-user similarity metric
  # returns a scaler between 0 and 1 representing the similarity
  # between user u1 and user u2. Closer to 1 is more similar.
  #
  # this implementation uses cosine similarity of common rated items
  def _user_user_sim(self, u1, u2):
    co_rated_items = []
    for (r1, r2) in zip(self.rating_matrix[u1], self.rating_matrix[u2]):
      if r1 and r2:
        co_rated_items.append((r1, r2))
    if len(co_rated_items) == 0:
      return 0.0
    u1_vector, u2_vector = zip(*co_rated_items)
    return 1-cosine(array(u1_vector), array(u2_vector))

  # returns the rating of item i by user u. If user u has not rated item i,
  # returns None
  def _get_rating(self, i, u):
    return self.rating_matrix[u][i]

  def __init__(self):
    self.rating_matrix = None
    self.item_count = None
    self.user_count = None
    self.n = 32

if __name__ == "__main__":
  c = Collab()
  c.load_file("data/jester-1-25.pickle")
  print c.predict_rating(0,0)
