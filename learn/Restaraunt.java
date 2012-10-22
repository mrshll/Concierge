
class Restaurant {
    private ArrayList<String> cuisines;
    private double distance;
    private double rating;
    private int price;


    /**
     * Change the ArrayList of strings into a binary vector
     * @return binary vector, with a 1 if the restaurant has the tag and a 0 if
     * it does not
     */
    public ArrayList<double> getCuisineVector(){
        //TODO: How can this be done?
        ArrayList<double> vector = new ArrayList<double>();
        return vector;
    }

    /**
     * @return distance the restaurant is from the user
     */
    public double getDistance(){
        return distance;
    }

    /**
     * @return the average rating of the restaurant
     */
    public double getRating(){
        return rating;
    }

    /**
     * @return the relative price of the restaurant (integer 1 - 5)
     */
    public int getPrice(){
        return price;
    }

    public Restaurant(ArrayList<String> cuis, double dist, double rate,
                      int p){
        cuisines = cuis;
        distance = dist;
        rating = rate;
        price = p;
    }

    /**
     * Calculate the score of the restaurant, defined as the inner product of
     * a weight vector and a corresponding feature vector.
     * Note: this is very easily adaptable into an actual learning algorithm,
     * such as linear regression or perceptron.
     * @return a score
     */
    public double score(User user, double latitude, double logitude){
        ArrayList<double> weights = new ArrayList<double>();
        list.add(1.0); //cuisine weight
        list.add(1.0); //rating weight
        list.add(-1.0); //distance weight
        list.add(-1.0); //price weight

        ArrayList<double> values = new ArrayList<double>();
        list.add(cosineSimilarity(getCuisineVector(),
                                  user.getCuisineVector()));
        list.add(rating);
        list.add(distance);
        list.add(Math.abs(user.getPrice() - price);

        return dotProduct(weights, values);

    }

    private double cosineSimilarity(ArrayList<double> xs, ArrayList<double> ys){
        return dotProduct(xs, ys) /
            (Math.sqrt(dotProduct(xs, xs)) * Math.sqrt(dotProduct(ys, ys)));
    }

    private double dotProduct(ArrayList<double> xs, ArrayList<double> ys){
        assert xs.size() == ys.size() : "xs and ys are not the same length";
        double sum = 0.0;
        for (int i = 0; i < xs.size(); i++) {
            sum += xs[i] * ys[i];
        }
        return sum;
    }

}
