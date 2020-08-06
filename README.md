# Full Stack Frameworks Project

The project I created for Code Institute's Full Stack Frameworks conclusion was based on a fictional online art gallery and shop. The purpose of this site was to showcase a range of prints and allow the user to purchase them, using Stripe authentication. I named this online store 'CITIZEN9'.
 
## UX
 
I started the UX process by looking at a variety of popular online shops, such as ASOS, Amazon and Society6, to see how a user would navigate their shopping experience. I focused on the shopping basket structure and the ease of the buying processs. 
I then created my user stories based on my research, and from the videos in the course content.

After I created my user stories I turned my attention to the UI of the site. I knew I wanted to create a 'clean' look and feel to the website, with easy navigation at the top. I decided on the name and thought the logo should come from Google Fonts. I then created some wireframes based upon this.

The user stories and low-fidelity wireframes are located in the UI-UX folder.

## Database schema

An example of the data structure in sqlite is as follows;

**Products**

```
  {
    "pk": "1",
    "model": "products.product",
    "fields": {
      "sku": "64838",
      "name": "Colourful, bold lines",
      "description": "Colourful, bold lines",
      "price": 5,
      "category": 1,
      "image": "0001.jpg"
    }
```

**Categories**

```
  {
    "pk": 1,
    "model": "products.category",
    "fields": {
      "name": "photography",
      "friendly_name": "Photography"
    }
  }
```

## Data Modelling

As stated in the course requirements, we were to create two custom views that went beyond what is shown in the course content. Mine can be found in shopping_basket/views.py

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

* Feature 8 - **update** - alter number of items in shopping basket, without having to return to store.

* Feature 9 - **delete** - delete from shopping basket.

* Feature 10 - **create account** - user can create an account.

* Feature 11 - **payment** - user can submit payment details through stripe.


### Features Left to Implement

* An email authentication to verify the users email.

* An account profile, so a user can review past orders.

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
* pip is the package installer for Python.
8. [db.sqlite3](https://www.sqlite.org/index.html)
* SQLite is the relational database management system.
9. [Masonry](https://masonry.desandro.com/)
* A JavaScript grid layout library for the image gallery.
10. [Gitpod](https://www.gitpod.io/)
* The development environment used.


## Testing

I decided to manually test the site. Each page was tested on Chrome, Firefox, Safari, Opera, Internet Explorer using the following the testing criteria;

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
* User can sort the returns by price

7. Add to shopping basket
* User can select item from image gallery
* Add quantity from 1-99 to shopping basket
* Cannot enter a null value or more than 99+
* Return to shop link working

8. Shopping basket
* Shopping basket nav link works
* You can see thumbnail of artwork purchasing, the quantity and price
* User should be able to update total number of items inside shopping basket
* User can permanently delete items from basket
* Option to 'keep shopping' and this returns user to store, while saving items in basket
* 'keep shopping' button working
* Total should be displayed at the bottom of the table
* Shopper should be prompted to spend a certain sum if order total less than £20
* £0.25 should be added to order if not qualifying for free delivery
* Delivery should be free if order total is more than £20
* If shopping basket emptied user sees notification basket is empty and return to store button
* Return to store button working
* Secure checkout button working

9. Checkout
* Crispy forms should be displaying with form validation
* Create an account link working if not an authenticated user
* Login link working for authenticated user
* If user is logged in 'Save this delivery information to my profile' text showing
* Connection is secure symbol showing in url
* Stripe payment should validate any card on typing in details
* Stripe payment should submit
* Page should return to checkout success

11. Payment Verification through Stripe
* For the testing process I used test card details, provided by stripe. These were:
* Card: 4242424242424242
* Date: 04/24
* CVC: 242
* ZIP: 42424
* Verified this in Stripe Webhooks - should return 'succeeded'

10. Checkout success
* Thank you message with users email displayed
* Return to store button working

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

I followed, with meticulous detail, the instructions on how to build an online shop from the course content. I would also like to give credit to Tutor Support, who pointed me in the right direction if I became stuck.

### Content

I initially wanted to use the 'Art Images: Drawing/Painting/Sculptures/Engravings' dataset from Kaggle. I tried using this dataset initially but soon realised this was not fit for my purpose, so I had to create my own dataset.

I started by looking at images from the open source image gallery website [unsplash.com](https://unsplash.com/) and then modeled my dataset on the course demonstration. You can see the structure in the 'fixtures' folder or an example is shown above in the Database Schema.

The content is entirely fictional and created by myself, therefore it is very limited. I would ideally have liked a huge database of artworks available to the user, but for all intents and purposes it showcases a limited 
number of artworks and demonstrates the purpose of the site.

### Media

All images for this project were obtained from the open source platform [unsplash.com](https://unsplash.com/).

The favicon was generated by [favicon.ico](https://favicon.io/favicon-generator/).

### Acknowledgements

I received inspiration for this project from [Society6](https://society6.com/) and [Artfinder](https://www.artfinder.com/). 

I'd like to acknowledge Code Institute for providing very thorough instructions on how to complete this online shop.
