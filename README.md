# Description

This project is a short ML project of identifying water potability, for more information, you can access the [kaggle dataset](https://www.kaggle.com/adityakadiwal/water-potability).

The goal is to determine if a water sample is potable or not. 

# Disclaimer

This dataset is only generate and it is not very realistic ! Don't use it real life !

# Composition

This project is composed of :

- Notebooks to analyze and create the predictive models.
- Simple web app that uses the generated model. It is hosted [here](http://51.178.17.141/) **(This like will not work after December 2021)**
- Simple scripts that will help retrain model as it implements some Semi Supervised learning.

# Production

Take note there is a branch called `prod` for production. Please take note, this was quick project, no authentication have been implemented, so any one who sends a "GET" request to `/admin_dummy_password` will retrain the model on the newly acquired data.
