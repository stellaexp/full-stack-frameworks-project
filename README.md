# Full Stack Frameworks Project

The project I created for Code Institute's Full Stack Frameworks conclusion was based on a fictional online art gallery and shop. The purpose of this site was to showcase a range of prints and allow the user to purchase them, using Stripe authentication. I named this online store 'CITIZEN9'.
 
## UX
 
I started the UX process by looking at a variety of popular online shops, such as ASOS, Amazon and Society6, to see how a user would navigate their shopping experience. I then focused on the shopping basket structure and the ease of the buying processs. 
I then created my user stories based on my research, and from the videos in the course content.

I knew I wanted to create a 'clean' look and feel to the website, with easy navigation at the top. I decided on the name and thought the logo should come from Google Fonts. I then created some wireframes based upon this.

The user stories and low-fidelity wireframes are located in the UI-UX folder.

## Features

The purpose of this project was to showcase our knowledge of front and backend technologies, using stripe payments.
 
### Existing Features

* Feature 1 - **login** - user can login.

* Feature 2 - **logout** - user can logout.

* Feature 3 - **browse** - user can browse prints/gallery.

* Feature 4 - **filter** - by category.

* Feature 5 - **sort** - by price.

* Feature 6 - **search** - user can search keywords to find artworks.

* Feature 7 - **add** - add to shopping basket.

* Feature 8 - **update** - add more items to shopping basket, without having to return to store.

* Feature 9 - **delete** - delete from shopping basket.

* Feature 10 - **create account** - user can create an account.

* Feature 11 - **payment** - user can submit payment details through stripe.


### Features Left to Implement

* An email authentication to verify the users email.

* An account profile, so a user can review past orders.

Although not a feature, I would really liked a more robust dataset so the user has more to work with.

## Technologies Used

1. [Balsamiq](https://balsamiq.com/)
* Used to create low-fidelity wireframes.
2. [Bootstrap](https://flask.palletsprojects.com/en/1.1.x/)
* Robust front-end library for HTML, CSS and JS.
3. [Google Fonts](https://fonts.google.com/)
*  For appealing typography.
4. [jQuery](https://jquery.com/)
*  The project uses jQuery to simplify DOM manipulation.
5. [Python](https://www.python.org/)
*  The backend programming language.
6. [Django](https://www.djangoproject.com/)
* The project is built on this high-level Python Web framework.
7. [pip](https://pip.pypa.io/en/stable/)
* pip is the package installer for Python
8. [Masonry](https://masonry.desandro.com/)
* A JavaScript grid layout library for the image gallery.


## Testing

I decided to manually test the application. Each page was tested on Chrome, Firefox, Safari, Opera, Internet Explorer using the following the testing criteria;

1. Login nav link
* Link should work
* Form should take a username and a password field
* User is now logged in

2. Logout nav link
* Link should work
* User should be asked if they want to logout
* User is now logged out

3. Browsing
* 'Search prints' button takes user to the shop
* User can see all artworks in the gallery

4. Filter by category in nav
* Nav link works
* User should be able to sort by All, Painting, Sculpture, Collage, Photography

5. Sort by price
* Navlink takes them to a pre-sorted page (low to high)
* User can select high to low

6. Search by keywords
* Search button/finder works
* User can search the database and it will return relevant results and number of matches
* If no matches in the database it should return "0 Artworks found for ..."

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

I followed, with meticulous detail, the instructions on how to build an online shop from the course content. I would also like to give credit to mentor support, who pointed me in the right direction if I became stuck.

### Content

I initially wanted to use the 'Art Images: Drawing/Painting/Sculptures/Engravings' dataset from Kaggle. Unfortunately, however, this was just not suitable for my purpose, so I had to create my own dataset.

I started by looking at images from the open source website unsplash.com and then modeled my dataset on the course demonstration. You can see the structure in the 'fixtures' folder.

The content is entirely fictional and created by myself, therefore it is very limited. I would ideally have liked a huge database of artworks available to the user, but for all intents and purposes it showcases a limited 
number of artworks and demonstrates the purpose of the site.

### Media

All images for this project were obtained from the open source platform [unsplash.com](https://unsplash.com/).

### Acknowledgements

I received inspiration for this project from [Society6](https://society6.com/) and [Artfinder](https://www.artfinder.com/). 

I'd like to acknowledge Code Institute for providing very thorough instructions on how to complete this online shop.
