# Coloring-Map-with-CSP

We were given a list of countries in South America and the colors we can use. First 
we needed to keep the border neighbors of each of the countries in South America in a data 
structure. I created a dictionary named graph and kept the country-neighbor key-pairs here.
According to our algorithm, first of all, we need to color the country with the most neighbors. In 
other words, I thought that we should sort the countries according to the number of neighbors, so I 
wrote a method called sortCountriesByNeighbors. Then I have a method called colorTheCountry. In 
this method, the countries are colored using back-tracking. I have a counter called 'counter'. Initially, 
I initialize its value from 0, and if the value of the counter is equal to the color value, there is no other 
color we can try. In such a case there is no solution so it will print 'unsolved problem' to the screen. 
Apart from these, I have a method called isColorCorrect. In this method, I checked whether the 
coloring is correct. If one of the neighbors of a country has the same color as the country, it means 
that we have made the wrong coloring here. By calling this method called isColorCorrect within the 
colorTheCountry method, our operations continue according to whether the coloring is correct or 
not.
<br><br>
Variables: X={"Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Falkland Islands", 
"Guyana", "Paraguay","Peru", "Suriname", "Uruguay", "Venezuela"}
<br><br>
Domains: D={"blue", "green", "red", "yellow"}
<br><br>
Constraints: adjacent regions must have different colors.<br>
C={ ( "Argentina" != "Bolivia", "Brazil", "Chile", "Paraguay", "Uruguay"),
("Bolivia" != "Argentina", "Brazil", "Chile", "Paraguay", "Peru"),
("Brazil" != "Argentina", "Bolivia", "Colombia", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", 
"Venezuela"),
("Chile" != " Argentina", "Bolivia", "Peru"),
("Colombia" !="Brazil", "Ecuador", "Peru", "Venezuela"),
("Ecuador" != "Colombia", "Bolivia", "Peru"),
("Guyana" != "Brazil", "Suriname", "Venezuela"),
("Paraguay" !="Argentina", "Bolivia", "Brazil"),
("Peru" != "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador"),
("Suriname" != "Brazil", "Guyana"),
("Uruguay" !="Argentina", "Brazil"),
("Venezuela" != "Brazil", "Colombia", "Guyana") }
