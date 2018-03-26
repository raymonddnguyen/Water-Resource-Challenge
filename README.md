# Water-Resource-Challenge

Small Challenge for Professor Wayne Hayes's Lab

Directions:

Your challenge is to publish a simple Python code on GitHub and run it within a hosted Continuous Integration service. Your code must download data directly from the URL http://rapid-hub.org/data/angles_UCI_CS.csv, notice and print the top line is a header, add a third header column, and then repeat the next lines of data as well as the cosine values for each angle---that is, print all values of “station_id”, “angle_degrees” and associated cosine values in the standard output. (PS: the data file does not go into the repo. Your code must download the data, because the data may change behind your back, although the format of the data will not change.) You might use the Ubuntu or MacOS capabilities of Travis CI, or the Windows capabilities of AppVeyor, depending on your preferred OS. Note that these services are free for open source software. Hint: this challenge requires the inclusion of a YAML file (*.yml) in your repository and that this YAML file shall be tailored to the hosted Continuous Integration service you selected.
