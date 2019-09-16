# Neighbourhood

## Author Joe Munyi Mwangi

## Description

This web-app that allows one to choose, change and see whats happening around their neirboorhood. Access social services, security and other ammenitues as well as shopping places.

## BDD

When the user opens the website, he/she will be prompted to sign up or sign in

| Input   |  Behavior | Expected Output|
|:--------|:---------|:--------------|
|Login| Prompts user to create an account or login if they have one| User is allowed to create an accountor login|
|Search| User can search using categories of neighboorhoods| The user will be able to see businesses,health centres and police authorities in the neighbourhood that other users have posted|
|clicking Blog | Opens blog, allows user to create and post news to update others |Opens blog, allows user to create and post news to update others|
|clicking username | Gives all posts by the user |Gives all posts by the user|
|clicking Profile | Allows user to change their credentials | Allows user to change profle picture and names |
|clicking Single post | Allows loged in user to delete or update post, anyone else cannot be allowed to do such, only owner | Allows loged in user to delete or update post |
|Admin can add photo editors, locations and categories|Admin can add photo editors, locations and categories|Admin can add photo editors, locations and categories|

* The user can also add their own business and news.
* The user can create Posts that will be visible to everyone in my neighborhood.
* The user also has a personalized profile where they can edit their profile.
* The user can change My neighborhood when I decide to move out.

## Prerequisites

To get started , one will need to install python3.6 or a higher version, django and postgres using the commands below:

* python3.6
$ sudo apt-get install python3.6.

* django -python framework
$ pip install django==2.2.5

* postgres -for database configurations and set up
$ sudo apt-get install postgresql postgresql-contrib libpq-dev

## Setup/Installation Requirements

* Install Neignboorhood by cloning this repository: <https://github.com/Munyiwamwangi/NeighbourHood.git>
* Install the prerequisites in a virtual environment or globally
* Install all the extensions listed in the requirements.txt file
* Using the command pip install -r requirements.txt

* ## Development server

Run `python3.6 manage.py runserver` for a dev server. Navigate to `<http://localhost:port> 8000/

               __
              |  |   / /
            _ _||_  / /
           | |    |/ /
           | |    |
           | |    |
Hurray ! ; Create and Enjoy Posting and reading other peoples images

* Contact me where necessary through [amadaick@gmail.com]

## Live Demo

Here is a link to a live demo: <https://joeneiba.herokuapp.com/>

## Technologies Used

* Python3.6.8
* postgress -database
* HTML
* CSS
* Django framework

## License

MIT License. Copyright (c) 2018 _Joe Munyi Munyi._
