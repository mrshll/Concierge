import java.util.*;
import java.lang.*;

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
    public ArrayList<Double> getCuisineVector(){
        String[] possibleCuisines = new String[] { "Afghan", "American",
            "Argentine", "Asian", "Austrian", "Bagels", "Bakery", "Barbecue",
            "Belgian", "Bistro", "Brazilian", "British", "Buffet", "Burgers",
            "Cafe", "Cajun", "Californian", "Calzones", "Cambodian",
            "Caribbean", "Catering", "Cheesesteaks", "Chicken", "Chinese",
            "Chowder", "Coffee", "Colombian", "Contemporary", "Continental",
            "Creole", "Crepes", "Cuban", "Czech", "Deli", "Dim Sum", "Diner",
            "Dominican", "Donuts", "Eastern European", "Eclectic", "English",
            "Ethiopian", "European", "Fast Food", "Filipino", "Fish and Chips",
            "Fondue", "French", "Frozen Yogurt", "Fusion", "Gastropub",
            "German", "Greek", "Grill", "Gyros", "Haitian", "Halal", "Hawaiian",
            "Healthy", "Hookah Bar", "Hot Dogs", "Ice Cream", "Indian",
            "Indonesian", "International", "Irish", "Israeli", "Italian",
            "Japanese", "Juices", "Korean", "Korean Barbeque", "Kosher",
            "Latin", "Latin American", "Lebanese", "Malaysian", "Mediterranean",
            "Mexican", "Middle Eastern", "Mongolian", "Moroccan", "Nepalese",
            "Noodle Bar", "Norwegian", "Organic", "Oysters", "Pacific Rim",
            "Pakistani", "Pan Asian", "Pasta", "Pasteries", "Persian",
            "Peruvian", "Pho", "Pizza", "Polish", "Polynesian", "Portuguese",
            "Pub Food", "Puerto Rican", "Ribs", "Salad", "Salvadoran",
            "Sandwiches", "Seafood", "Singaporean", "Smoothies", "Soul Food",
            "Soup", "South American", "South Pacific", "Southern",
            "Southwestern", "Spanish", "Steak", "Subs", "Sushi", "Taiwanese",
            "Tapas", "Tea", "Tex Mex", "Thai", "Tibetan", "Traditional",
            "Turkish", "Ukrainian", "Vegan", "Vegetarian", "Venezuelan",
            "Venusian", "Vietnamese", "Wings", "Wraps"};


        ArrayList<Double> vector = new ArrayList<Double>();
        for (int i = 0; i < possibleCuisines.length; i++){
            if (cuisines.contains(possibleCuisines[i])){
                vector.add(new Double(1.0));
            } else {
                vector.add(new Double(0.0));
            }
        }
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
        ArrayList<Double> weights = new ArrayList<Double>();
        weights.add(1.0); //cuisine weight
        weights.add(1.0); //rating weight
        weights.add(-1.0); //distance weight
        weights.add(-1.0); //price weight

        ArrayList<Double> values = new ArrayList<Double>();
        values.add(cosineSimilarity(getCuisineVector(),
                                  user.getCuisineVector()));
        values.add(rating);
        values.add(distance);
        values.add(Math.abs(user.getPrice() - price));

        return dotProduct(weights, values);

    }

    private double cosineSimilarity(ArrayList<Double> xs, ArrayList<Double> ys){
        return dotProduct(xs, ys) /
            (Math.sqrt(dotProduct(xs, xs)) * Math.sqrt(dotProduct(ys, ys)));
    }

    private double dotProduct(ArrayList<Double> xs, ArrayList<Double> ys){
        assert xs.size() == ys.size() : "xs and ys are not the same length";
        double sum = 0.0;
        for (int i = 0; i < xs.size(); i++) {
            sum += xs.get(i) * ys.get(i);
        }
        return sum;
    }

}
