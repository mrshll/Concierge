# Collab is an implementation of the memory-based collaboration filtering
# algorithm found at http://en.wikipedia.org/wiki/Collaborative_filtering

class Collab(object):

  ########################################
  # FUNCTIONS FOR OUTSIDE USE (PUBLIC)
  ########################################

  # load a file into the engine, user for side-effect
  def load_file(file_name):
    pass

  # predicts the rating of the reccomendation item at index i
  # by the user whose inde is u
  # returns actual rating if that item is already rated
  # this rating is not stored in the rating matrix
  def predict_rating(i, u):
    return None

  # returns true if a user u has recommended reccomendation item i
  # else returns false
  def has_reccomended(i, u):
    return False

  #########################################
  # FUNCTIONS NOT FOR OUTSIDE USE (PRIVATE)
  #########################################

  # user-user similarity metric
  # returns a scaler between 0 and 1 representing the similarity
  # between user u1 and user u2. Closer to 1 is more similar.
  #
  # this implementation uses pearson's R
  def _user_user_sim(u1, u2)
    return 0.0
