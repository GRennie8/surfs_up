# Surfs Up
Advanced Data Storage and Retrieval with `Jupyter Notebook`, `SQLite` and `SQLAlchemy`

## Overview
The purpose of this analysis is to review a dataset consisting of weather conditions in Oahu, Hawaii. This database will be used to provide information that will convince an investor that opening up a Surf n' Shake shop is a good business idea. The idea is that the shop will sell surf boards and ice cream throughout the year, but the investor is hesitant because he invested in a similar business that failed due to the weather conditions. This analysis will help to convince the investor based on real weather data.

## Results
I have merged both months temperature statistics into one DataFrame for easier analysis.

<img width="650" alt="Screen Shot 2022-07-06 at 2 21 22 PM" src="https://user-images.githubusercontent.com/104115586/177640683-fd1d4f60-ae74-43ef-b53b-481e5bde54e1.png">



 - Average temperature between June and December is 75 and 71 degrees respectively, show a moderate temperature and very little fluctuation between the two    periods from an average standpoint.
 - Maximum temperatures of 85 (June) and 83 (December) are also remarkable similar.
 - Minimum temperature of 56 (December) and 64 (June) show the greatest variance, and reflects a much lower temperature level in December that may not be conducive to ice cream or surfing. However, with standard deviations of 3.25 (June) and 3.74 (December) we would expect a little more variation in December.

### Additional queries
I have also created a merged DataFrame to display the precipitation statistics for the months of June and December.

<img width="761" alt="Screen Shot 2022-07-06 at 2 21 31 PM" src="https://user-images.githubusercontent.com/104115586/177641505-84335941-6b25-45e3-9aec-971dcc992c99.png">

 - Average rainfall across both months is pretty low which leads us to believe there is never any consistent downpours in the area, ideal for a surf and ice cream shop!
 - I would also suggest gathering as much wind related data as possible. Wind direction and speed are very important factors when it comes to surfing. The most ideal conditions are Offshore wind (wind blowing towards the water from the land). If this is a rare occurence at a chosen site then I would recommend finding a location which has a high number of offshore winds.
 
 ## Summary
 Overall I would have to say that Oahu, Hawaii is an excellent choice for a surf and ice cream shop due to the ideal weather year round. This can lead to a steady stream of business througout the whole year without the need to worry about 'seasonal changes'. Once wind data has been analysed I think the wheels can be put in motion for this new business venture.
