HIVEMIND : DESIGN DOC

================================================================================

Summary: Hivemind (working title) is an as-of-yet loosely defined API that
combines datapoints from a large set of social services (through their
respective APIs) and provides a platform to (machine) learn based on a user's
full web-presence.

Challenges and Points of Interest:
- INTRA-API RELATIONSHIPS:
  The foremost and potentially most difficult problem is determining which of
  the huge set of datapoints are relevant to different machine learning tasks.
  Or more explicitly, how different API's data relate to eachother. How does a 
  datapoint in one API correlate to datapoints in another, and is it dependent 
  on the way a particular user uses each service?
- LEARNING TASK DEFINEABILITY:
  If this is meant to serve as an API for learning, there has to be some way for
  the end-user (developer) to customize and define exactly what they want to
  learn on. The main problem is that machine learning is EXPENSIVE. Do we run
  the learning on our own machines? Probably not. We have to figure out a very
  restricted way that a user can interact with the API that will fulfil most
  devs' needs.

Obviously this is in the earliest possible stage. I find it helpful to think of
this project in terms of an API that will be used for the parent project,
Concierge (see CONCIERGE_README.txt)

