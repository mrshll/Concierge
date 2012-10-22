/*
 * RecommendationEngine is a recommender for a single, specific user
 */

class RecommendationEngine {

    public ArrayList<Restaurant> recommend(double latitude, double longitude,
                                           String username) {
        // get restaurants and user from database
        ArrayList<Restaurant> restaurants = new ArrayList<Restaurant>();
        User user = new User();

        // sort restaurants by score
        sort(restaurants, RestaurantSortByScore(user, latitude, longitude));

        return restaurants;
    }
}

class RestaurantSortByScore implements Comparator<Restaurant> {
    private User user;
    private double latitude;
    private double longitude;

    public RestaurantSortByScore(User u, double lat, double lon){
        user = u;
        latitude = lat;
        longitude = lon;
    }

    public int compare(Restaurant o1, Restaurant o2){
        double r1Score = o1.score(user, latitude, longitude);
        double r2Score = o2.score(user, latitude, longitude);
        if (r1Score > r2Score) return 1;
        if (r1Score == r2Score) return 0;
        return -1;
    }
}
