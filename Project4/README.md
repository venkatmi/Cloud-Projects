P3
==

P3

Application: Want to know where your favorite artist is performing next that is close to you? This simple web application can provide you with the details of the singer and their future events.

Inputs: Enter your favorite artist’s complete name (Starting letters in Caps) and your zipcode(US States only) and see his/her most famous songs, popularity and their next performance closest to you and view their tours around the world .

Description: This is a simple web application that uses three publically available web services (API) (echonest, Songkick and google maps) to read an artist’s complete details, events and then calculate the event whose longitude and latitude is the closest to the zipcode you provided. We also use the google static maps to view the artist's future tour trips around the world. For each of these API’s, the api key was provided by the website to use their services . These keys help them constrict the number of calls made to the website at a time. The fourth service we use is google app engine memcache . We use this service to count the number of views of a particular artist to the total views of the website.

Services used:

Echonest API: The Echo Nest provides methods to return a wide range of data about any music artist.Their most famous songs, genre, biography, famous videos and hotness. It also provides the songkick id for the artist. 

Songkick API: The Songkick API gives you easy access to the biggest live music database in the world: over 3 million upcoming and past concerts.Using this API we identify the artist's future events and all the details of the events including date, time and location (including longitude and latitude).

GoogleMaps Geocoding API: Geocoding is the process of converting addresses (like "1600 Amphitheatre Parkway, Mountain View, CA") into geographic coordinates (like latitude 37.423021 and longitude -122.083739), which you can use to place markers or position the map.This API provides us direct access to this service.We convert the entered zipcode to longitude and latitude and use a function to calculate the closest event to this zipcode.

GoogleMaps Static Image API: We embed a static map of the world containing all the locations of the events the artist would be performing at.This provides a bigger picture and helps the user plan better.

Google AppEngine Memcache service: We use memcache to store the number of views of each artist and the total views of the website. When an user enters an artist name, if the artist had been queried previously it will show the total views for that particular artist. This gives us an idea of the popularity of an artist.

Request:
1) Artist Name 
2) Zipcode 

Response:
1) Artist Name 
2) Artist Image (Click on the image to view the video of the artist)
3) Top songs of the artist 
4) Popularity or Hotness of the Artist
5) Closest event details of the atrtist including date, time and total miles
6) Map showing the entire tour map of the Artist 
7) Total views of the artist in the site 
8) Total views of the site

Execution:
1) Go to the url http://cscloud.ceas.uc.edu:3126 in UC network.
2) Enter the details. For eg:- Artist Name: One Republic and zipcode: 45221. Click Submit button.


