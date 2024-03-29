# Testing

# Browser Compatibility

## Chrome

Chrome Navbar

![Chrome Navbar](documentation/testing/atletico-crud-chrome-navbar.png)

Chrome Home Page

![Chrome Home Page](documentation/testing/atletico-crud-chrome-home.png)

Chrome Register Page

![Chrome Register Page](documentation/testing/atletico-crud-chrome-register.png)

Chrome Log-In Page

![Chrome Log-In Page](documentation/testing/atletico-crud-chrome-log-in.png)

Chrome Profile Page

![Chrome Profile Page](documentation/testing/atletico-crud-chrome-profile.png)

Chrome Countries Page

![Chrome Countries Page](documentation/testing/atletico-crud-chrome-countries.png)

Chrome Leagues Page

![Chrome Leagues Page](documentation/testing/atletico-crud-chrome-leagues.png)

Chrome Clubs Page

![Chrome Clubs Page](documentation/testing/atletico-crud-chrome-clubs.png)

Chrome Players Page

![Chrome Players Page](documentation/testing/atletico-crud-chrome-players.png)

Chrome Addition of Country/Leage/Club/Player

![Chrome Addition of Country/Leage/Club/Player](documentation/testing/atletico-crud-chrome-addition.png)

Chrome Edit Country/League/Club/Player Page

![Chrome Edit Club Page](documentation/testing/atletico-crud-chrome-edit.png)

Chrome Delete Modal

![Chrome Delete Modal](documentation/testing/atletico-crud-chrome-delete-modal.png)

Chrome Log-Out

![Chrome Log-Out](documentation/testing/atletico-crud-chrome-log-out.png)

## Edge

Edge Countries

![Edge Countries](documentation/testing/atletico-crud-edge-countries.png)

Edge Leagues

![Edge Leagues](documentation/testing/atletico-crud-edge-leagues.png)

Edge Clubs

![Edge Clubs](documentation/testing/atletico-crud-edge-clubs.png)

Edge Players

![Edge Players](documentation/testing/atletico-crud-edge-players.png)

Edge Form

![Edge Form](documentation/testing/atletico-crud-edge-form.png)

## Safari (Mobile)

Safari Home Page

![Safari Home Page](documentation/testing/atletico-crud-safari-home.jpg)

Safari Register Page

![Safari Register Page](documentation/testing/atletico-crud-safari-register.jpg)

Safari Sidenav Page

![Safari Sidenav Page](documentation/testing/atletico-crud-safari-sidenav.jpg)

Safari Log-In Page

![Safari Log-In Page](documentation/testing/atletico-crud-safari-log-in.jpg)

Safari Profile Page

![Safari Profile Page](documentation/testing/atletico-crud-safari-profile.jpg)

Safari Countries Page

![Safari Countries Page](documentation/testing/atletico-crud-safari-countries.jpg)

Safari Leagues Page

![Safari Leagues Page](documentation/testing/atletico-crud-safari-leagues.jpg)

Safari Clubs Page

![Safari Clubs Page](documentation/testing/atletico-crud-safari-clubs.jpg)

Safari Players Page

![Safari Players Page](documentation/testing/atletico-crud-safari-players.jpg)

Safari Edit Player Page

![Safari Edit Player Page](documentation/testing/atletico-crud-safari-edit-player.jpg)

Safari Delete Modal

![Safari Delete Modal](documentation/testing/atletico-crud-safari-delete-modal.jpg)

Safari Log-Out

![Safari Log-Out](documentation/testing/atletico-crud-safari-log-out.jpg)

# Code Validation

## HTML

The following screenshots and hyperlinks show that the same warning is raised for all pages. The warning is due to the lack of heading on a section element relating to flash messages. This is due to the extension of base.html to all other html pages via template inheritance. Giving the section a heading is not appropriate in this instance.

[Home Page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fatletico-crud.herokuapp.com%2F)

![Home](documentation/testing/atletico-crud-html-validation-home.png)

[Register Page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fatletico-crud.herokuapp.com%2Fregister)

![Register](documentation/testing/atletico-crud-html-validation-register.png)

[Log In Page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fatletico-crud.herokuapp.com%2Flogin)

![Log In](documentation/testing/atletico-crud-html-validation-login.png)

[Profile Page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fatletico-crud.herokuapp.com%2Fprofile%2Fadmin)

![Profile](documentation/testing/atletico-crud-html-validation-profile.png)

[Countries Page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fatletico-crud.herokuapp.com%2Fcountries)

![Countries](documentation/testing/atletico-crud-html-validation-countries.png)

[Leagues Page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fatletico-crud.herokuapp.com%2Fleagues%2F0)

![Leagues](documentation/testing/atletico-crud-html-validation-leagues.png)

[Clubs Page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fatletico-crud.herokuapp.com%2Fclubs%2F0)

![Clubs](documentation/testing/atletico-crud-html-validation-clubs.png)

[Players Page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fatletico-crud.herokuapp.com%2Fplayersa%2F0)

![Players](documentation/testing/atletico-crud-html-validation-playersa.png)

The following pages can be validated by visiting the respective page, right clicking on the page and selecting _View page source_. The source code can then be copied and pasted into the HTML validator providing the option of _Check by text input_ has been selected on the validator page. For this reason, no hyperlinks have been provided however the following screenshots show that the same warning is raised for all pages. The warning is due to the lack of heading on a section element relating to flash messages. This is due to the extension of base.html to all other html pages via template inheritance. Giving the section a heading is not appropriate in this instance.

Add Country Page

![Add Country](documentation/testing/atletico-crud-html-validation-add-country.png)

Add League Page

![Add League](documentation/testing/atletico-crud-html-validation-add-league.png)

Add Club Page

![Add Club](documentation/testing/atletico-crud-html-validation-add-club.png)

Add Player Page

![Add Player](documentation/testing/atletico-crud-html-validation-add-playersa.png)

Edit Country Page

![Edit Country](documentation/testing/atletico-crud-html-validation-edit-country.png)

Edit League Page

![Edit League](documentation/testing/atletico-crud-html-validation-edit-league.png)

Edit Club Page

![Edit Club](documentation/testing/atletico-crud-html-validation-edit-club.png)

Edit Player Page

![Edit Player](documentation/testing/atletico-crud-html-validation-edit-playera.png)

Form Page

![Form](documentation/testing/atletico-crud-html-validation-form.png)

Confirmation Page

![Confirmation](documentation/testing/atletico-crud-html-validation-confirmation.png)

## CSS

The hyperlink and screenshot below shows that the only error displaying when validating the CSS is related to the link used to import Materialize CSS. As this code is essential for the app's style and is also not code that I have written, this error is ignored.

[CSS Validation](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fatletico-crud.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

![CSS](documentation/testing/atletico-crud-css-validation.png)

## JavaScript

The screenshot below shows that the only issue with the JavaScript used for this project is an undefined variable _M_. This arises due to the initialization JavaScrip code used by Materialize CSS and can therefore be ignored.

![JS Hint](documentation/testing/atletico-crud-js-hint-validation.png)

## Python

The following screenshots show that [pep8 online](http://pep8online.com/) found no errors in the python code for init.py, models.py, routes.py and app.py.

The files env.py and any python files in the _migrations_ folder were not validated as this is not required.

Init

![Init](documentation/testing/atletico-crud-python-validation-init.png)

Models

![Models](documentation/testing/atletico-crud-python-validation-models.png)

Routes

![Routes](documentation/testing/atletico-crud-python-validation-routes.png)

App

![App](documentation/testing/atletico-crud-python-validation-app.png)

# Lightouse

## Countries

![Countries Lighthouse](documentation/testing/atletico-crud-lighthouse-countries.png)

## Leagues

![Leagues Lighthouse](documentation/testing/atletico-crud-lighthouse-leagues.png)

## Clubs

![Clubs Lighthouse](documentation/testing/atletico-crud-lighthouse-clubs.png)

## Players

![Players Lighthouse](documentation/testing/atletico-crud-lighthouse-players.png)

# Responsiveness

## Countries

### Countries Large

![Countries Large](documentation/testing/atletico-crud-responsiveness-countries-large.png)

### Countries Medium

![Countries Medium](documentation/testing/atletico-crud-responsiveness-countries-medium.png)

### Countries Small

![Countries Small](documentation/testing/atletico-crud-responsiveness-countries-small.png)

## Leagues Page

### Leagues Large

![Leagues Large](documentation/testing/atletico-crud-responsiveness-leagues-large.png)

### Leagues Medium

![Leagues Medium](documentation/testing/atletico-crud-responsiveness-leagues-medium.png)

### Leagues Small

![Leagues Small](documentation/testing/atletico-crud-responsiveness-leagues-small.png)

## Clubs Page

### Clubs Large

![Clubs Large](documentation/testing/atletico-crud-responsiveness-clubs-large.png)

### Clubs Medium and Below

![Clubs Medium And Below](documentation/testing/atletico-crud-responsiveness-clubs-med-and-below.png)

## Players Page

### Players Large

![Players Large](documentation/testing/atletico-crud-responsiveness-players-large.png)

### Players Medium and Below

![Players Medium And Below](documentation/testing/atletico-crud-responsiveness-players-med-and-below.png)

# User Story Tests

- As a user, I want to be able to register as a user on the website.

![Chrome Register Page](documentation/testing/atletico-crud-chrome-register.png)

- As a user, I want to be able to log in and log out from the website.

![Chrome Log-In Page](documentation/testing/atletico-crud-chrome-log-in.png)

![Chrome Log-Out](documentation/testing/atletico-crud-chrome-log-out.png)

- As a user, I want to be able to read/view countries, leagues, clubs and players that have already been inducted into the database.

![Chrome Countries Page](documentation/testing/atletico-crud-chrome-countries.png)

![Chrome Leagues Page](documentation/testing/atletico-crud-chrome-leagues.png)

![Chrome Clubs Page](documentation/testing/atletico-crud-chrome-clubs.png)

![Chrome Players Page](documentation/testing/atletico-crud-chrome-players.png)

- As a user, I want to be able to submit a form to suggest a player that should be added to the database.

![Chrome Form](documentation/testing/atletico-crud-chrome-form.png)

- As a user, I want to be able to receive confirmation that my form has been sent.

![Chrome Confirmation](documentation/testing/atletico-crud-chrome-confirmation.png)

- As a user, I want to be able to navigate to view all countries, leagues, clubs and players from the navbar.

![Chrome Navbar](documentation/testing/atletico-crud-chrome-navbar.png)

- As a user I want to be able to view the website across multiple devices and screen sizes.

![Am I Responsive](documentation/testing/atletico-crud-am-i-responsive.png)

- As an admin, I want to be able to create/add data to the database.

![Chrome Addition of Country/Leage/Club/Player](documentation/testing/atletico-crud-chrome-addition.png)

- As an admin, I want to be able to read/view data on the database.

![Chrome Countries Page](documentation/testing/atletico-crud-chrome-countries.png)

![Chrome Leagues Page](documentation/testing/atletico-crud-chrome-leagues.png)

![Chrome Clubs Page](documentation/testing/atletico-crud-chrome-clubs.png)

![Chrome Players Page](documentation/testing/atletico-crud-chrome-players.png)

- As an admin, I want to be able to update/edit data within the database.

![Chrome Edit Club Page](documentation/testing/atletico-crud-chrome-edit.png)

- As an admin, I want to be able to delete data from the database.

![Chrome Delete Modal](documentation/testing/atletico-crud-chrome-delete-modal.png)

- As an admin, I want to receive confirmation that actions involving creating, editing or deleting have been successful or unsuccessful.

![Chrome Flash Message](documentation/testing/atletico-crud-chrome-flash.png)

- As an admin I want to be able to create/add, read/view, update/edit and delete content on the website across multiple devices and screen sizes.

![Safari Add Country Page](documentation/testing/atletico-crud-safari-add-country.jpg)

![Safari Edit Player Page](documentation/testing/atletico-crud-safari-edit-player.jpg)

![Safari Delete Modal](documentation/testing/atletico-crud-safari-delete-modal.jpg)

# Error Handling

## Error Code 404

The code below diverts users to a custom Error 404 page which is also shown in the screenshot below.

```python
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
```

![Error 400 Page](documentation/testing/atletico-crud-error-handling-404.png)

## Error Code 500

The code below diverts users to a custom Error 500 page which is also shown in the screenshot below.

```python
@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 500 status explicitly
    return render_template('500.html'), 500
```

![Error 500 Page](documentation/testing/atletico-crud-error-handling-500.png)

# Unfixed Bugs

## Risk of Invalid Image URLs

There is a risk that the *image_urls* used for the country flags, league logos, club badges and players are updated at source which would cause the image to stop displaying on my site. This is something that I would monitor and if it were to happen, I could log in as an admin to rectify the issue by editing the *image_url* to one that works correctly.

## Editing a Country/League/Club Name or Image URL Workaround

In order to prevent duplicate entries of Countries/Leagues/Clubs into the database which would cause a Postgres error, the following code was written into the Add and Edit routes for the Country, League and Club models. The example below is taken from the Club model.

```python
        existing_club = Club.query.filter(
            func.lower(Club.club_name) == request.form.get(
                "club_name").lower()).first()
        if existing_club:
            flash("Club Already Exists!")
            return redirect(url_for("clubs", league_id=0))

        exisitng_club_img = Club.query.filter(
            func.lower(Club.club_image_url) == request.form.get(
                "club_image_url").lower()).first()
        if exisitng_club_img:
            flash("Image Already in Use!")
            return redirect(url_for("clubs", league_id=0))
```

This worked well for preventing the Postgres error when attempting to add duplicate data, however, it has given rise to the requirement to use a frustrating workaround when utilising the Edit Country/League/Club functionality which is discussed below.

### Description of Scenario

When editing a Country/League/Club, it is not possible to update the image without changing the name of the Country/League/Club too. This is due to the `existing country/league/club` check within the Add and Edit routes which will flash the message "Country/League/Club Already Exists!".

Similarly, it is not possible to add the same country/league/country_image_url to the same data table. This is due to the `existing_country/league/club_img` check within the Add and Edit routes which will flash the message "Image Already In Use!".

This could be frustrating for a user as if an user wanted to edit the image used to represent _England_ whilst keeping the name the same, it would not be possible and the flash message would display "Country Already Exists!".

Similarly, if an user only wanted to edit the name of a country/league/club associated with an image, it would not be possible and the flash message would display "Image Already In Use!".

### The Workaround

Imagine a scenario where _England_ was incorrectly entered as _England**s**_ in Country Name whilst the Country Image URL added was correct. The workaround to be able to rectify this error via the Edit Country functionality is as follows:

- Click Edit Country/League/Club.
- Enter an arbitrary value _e.g. ABC_ into the Country Name field to replace _England**s**_.
- Enter an arbitrary value _e.g. www.google.com_ into the Country Image URL field to replace the correct Country Image URL.
- Click the Edit Country button and the data will successfully update and will display a non-sensical Country of _ABC_ with the image URL _www.google.com_.
- Now, repeat the above process but enter the desired country name _England_ into the Country Name field to replace _ABC_ and enter the correct Country Image URL back into the Country Image URL field to replace _www.google.com_.
- Click the Edit Country button and the data will successfully update to give a Country with the name England and the image displayed will be the England flag.

Although this workaround is frustrating, it does prevent duplicate entries into the database causing a Postgres error which does take priority as an issue vs. this workaround in my opinion.

I would like to fix this 'Workaround Bug' in future however at the moment, the only user impacted by this will be the admin. If care is taken during the data creation phase, this workaround should not be required and it is credible to suggest that should an error occur during this phase, the admin could utilise the workaround or could simply delete the entry and start again.

The only credible situation where this workaround would need to be utilised frequently (annually) would be at the end of a season when clubs within leagues change due to promotion/relegation.

It is also worth noting that this issue does not occur for the Players data which is stored on MongoDB.