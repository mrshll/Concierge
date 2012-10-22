class User {
    private ArrayList<Restaurant> positiveLabels;
    private ArrayList<Restaurant> negativeLabels;

    /**
     * Gets the cuisine vector to compare to the restaurant's cusine vector
     * @return average vector of all of the positive labels cuisine vectors
     */
    public ArrayList<double> getCuisineVector(){
        ArrayList<double> sumVector = ArrayList<double>(positiveLabels[0].size());
        for (int i = 0; i < positiveLabels[0].size(); i++){
            sumVector[i] = 0;
        }

        for (Restaurant restaurant : positiveLabels){
            ArrayList<double> rVector = restaurant.getCuisineVector();
            for (int i = 0; i < rVector.size(); i++){
                sumVector[i] += rVector[i];
            }
        }

        for (double d : sumVector){
            d = d / positiveLabels.size();
        }
        return sumVector;
    }

    /**
     * Gets the customer's preferred price for a meal, the average of all of
     * their positively labeled restaurants
     * @return an average of the positively labeled restaurants' prices
     */
    public double getPrice() {
        double priceSum = 0.0;
        for (restaurant r : positiveLabels){
            priceSum += r.getPrice();
        }
        return priceSum / positiveLabels.size();
    }
}
