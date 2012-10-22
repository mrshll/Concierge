import java.util.*;
import java.lang.*;

public class User {
    private ArrayList<Restaurant> positiveLabels;
    private ArrayList<Restaurant> negativeLabels;

    /**
     * Gets the cuisine vector to compare to the restaurant's cusine vector
     * @return average vector of all of the positive labels cuisine vectors
     */
    public ArrayList<Double> getCuisineVector(){
        int cuisineLength = positiveLabels.get(0).getCuisineVector().size();

        ArrayList<Double> sumVector = new ArrayList<Double>(cuisineLength);

        for (int i = 0; i < cuisineLength; i++){
            sumVector.set(i, new Double(0.0));
        }

        for (Restaurant restaurant : positiveLabels){
            ArrayList<Double> rVector = restaurant.getCuisineVector();
            for (int i = 0; i < rVector.size(); i++){
                sumVector.set(i, sumVector.get(i) + rVector.get(i));
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
        for (Restaurant r : positiveLabels){
            priceSum += r.getPrice();
        }
        return priceSum / positiveLabels.size();
    }

    public User() {
        positiveLabels = new ArrayList<Restaurant>();
        negativeLabels = new ArrayList<Restaurant>();
    }

    public void addPositiveLabel(Restaurant restaurant){
        positiveLabels.add(restaurant);
    }

    public void addNegativeLabel(Restaurant restaurant){
        negativeLabels.add(restaurant);
    }
}
