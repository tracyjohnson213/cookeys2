<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

# Cookeys

The purpose of this web application is to allow sharing of cookie recipes.

The website is deployed to url = https://cookeys2.herokuapp.com/.

The site has been recreated in order to fill the following demonstration:

- Creation of a MongoDB backed Flask web application project that allows users to store and manipulate data records

- Design of well suited database structure including nested relationships between records of different entities

- Creation of CRUD functionality

- Use of HTML and custom CSS for front end

- Incorporation of main navigation menu and structured layout

- Creation of valuable README.md

- Git & Github version control

- Clear separation of code written from code of external sources

- Deployment to Heroku environment

- No inclusion of passwords or secret keys in the project repository

## UX

The website is designed to enable users to find and share cookie recipes.

wireframe, static/assets/cookeyswireframe_v1.xd

### External user’s goal

Find and share personal cookie recipes.

### Site owner’s goal

Promote the sell of tools used to bake.

## Features

Create a web application that allows users to store and easily access cookie recipes.

A front end form and backend code that allows users to add new submission to the site, edit and delete them.

Create front and back end functionality for users to locate tips based on fields; either full search functionality or just a directory.

Provide results in a manner that is visually appealing and user friendly.

### Existing Features

### Features Left to Implement

### Features – Nice to have

## Technologies Used

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - The project uses _HTML5_, a markup language used for structuring and presenting content on the World Wide Web.

* [CSS3](https://www.w3.org/Style/CSS/current-work.en.html) - The project uses Cascading Style Sheets(_CSS_), a style sheet language used for describing the presentation of a document written in a markup language like HTML.

- [JavaScript](https://www.javascript.com/) - The project uses _JavaScript_, a programming language that conforms to the ECMAScript specification.

* [Python](https://www.python.org/) - The project uses _Python_, an interpreted, high-level, general-purpose programming language.

- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The project uses _Flask_, which depends on the Jinja template engine and the Werkzeug WSGI toolkit.

* [MongoDB](https://www.mongodb.com/) - The project uses _MongoDB_, is a popular database for modern apps, and _MongoDB_ Atlas, the global cloud database on AWS, Azure, and GCP

- [Adobe XD](https://www.adobe.com/products/xd.html) - _Adobe XD_ is a vector-based UI/UX design tool for web apps and mobile apps.

- [Wires wireframe kits for Adobe-XD](https://www.behance.net/gallery/55462459/Wires-free-wireframe-kits-for-Adobe-XD) - _wireframe UX kits_ for mobile and web, built exclusively for Adobe XD.

* [favicon.cc](https://www.favicon.cc/) - _favicon.cc_ is a tool to create or download favicon icons.

- [Wrike](https://wrike.com) - _Wrike_ is an Online Project Management Software platform.

- [StackEdit](https://www.stackedit.io) - README.md was generated within _StackEdit_, a full-featured, open-source Markdown editor based on PageDown, the Markdown library used by Stack Overflow and the other Stack Exchange sites.

* [Tidy Gherkins](https://chrome.google.com/webstore/detail/tidy-gherkin/nobemmencanophcnicjhfhnjiimegjeo?hl=en-GB) - _Tidy Gherkins_ allows generation of Cucumber steps for Java/Ruby/Javascript step definitions from your Gherkin feature files consistent in layout.

- [Diagram.io](https://dbdiagram.io) for database dbdiagram, static/assets/cookeysdbdiagram.pdf

* [Gitpod](https://www.gitpod.io/) - _Gitpod_ is a development environment for any GitLab, GitHub, and Bitbucket project.

- [Github](https://www.github.com/) - _Github_ is a repository hosting service.

* [Heroku](https://heroku.com) - _Heroku_ is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.


## Testing

### Scenarios
click link to go to page

- [x] |navbar logo|/get_recipes|
- [x] |footer logo|/get_recipes|
- [x] |navbar add|/add_recipe|
- [x] |footer add|/add_recipe|
- [x] |recipe click for recipe|/get_cookie/<cookie_name>|
- [x] |/get_cookie/<cookie_name> edit|/edit_recipe/<recipe_id>|
- [ ] |/get_cookie/<cookie_name> delete||--FAILED
- [ ] |navbar find||--FAILED
- [ ] |footer find||--FAILED

view on homepage /get_recipes
- [x] all recipes in database
- [x] recipes.cookie_name
- [x] recipes.summary
- [x] link = click for recipe

click click for recipe link on get_cookie and view
- [x] cookie name
- [x] ingredients
- [x] steps
- [x] category
- [x] author
- [x] edit button
- [x] delete button

click link on get_cookie and view
- [x] |edit button|/edit_recipe/<recipe_id>|
- [ ] |delete button|request for confirmation of deletion|--FAILED
- [x] |category|

click confirm on confirmation of delete
- [ ] recipe is deleted from database and system returns to get_recipes--FAILED

- [ ] verify deletion of recipe--FAILED

view form fields for add_recipe
- [x] cookie name
- [x] <categories>
- [x] qty
- [x] ingredients
- [x] sales pitch
- [x] step
- [x] first name
- [x] last name
- [x] image_source

view form buttons for add_recipe
- [x] add name
- [x] add qty & ingredient
- [x] add step
- [x] add author
- [x] upload image
- [x] add recipe

click form button on add_recipe view addition in preview table 
|button|addition|
- [x] |add name|ccokie name|
- [x] |add qty & ingredient|qty & ingredient|
- [x] |add step|step|
- [x] |add author| first name & last name|
- [ ] |upload imageimage_thumbnail|--FAILED
- [x] |add recipe

click add recipe button on add_recipe form
- [ ] confirm addition and return to get_recipes--FAILED

verify field value additions for add_recipe
- [x] cookie name
- [x] <categories>
- [x] qty
- [x] ingredients
- [x] sales pitch
- [x] step
- [x] first name
- [x] last name
- [x] image_source

view form fields for edit_recipe
- [x] cookie name
- [x] <categories>
- [x] qty
- [x] ingredients
- [x] sales pitch
- [x] step
- [x] first name
- [x] last name
- [x] image_source

edit form fields for edit_recipe
- [x] cookie name
- [x] <categories>
- [x] qty(s)
- [x] ingredients
- [x] sales pitch
- [x] step(s)
- [x] first name
- [x] last name
- [x] image_source

click update recipe button on edit_recipe form
- [ ] confirm update of each field and return to get_recipes--FAILED

verify form field value updates for edit_recipe
- [ ] cookie name--FAILED
- [ ] <categories>--FAILED
- [ ] qty(s)--FAILED
- [ ] ingredients--FAILED
- [ ] sales pitch--FAILED
- [ ] step(s)--FAILED
- [ ] first name--FAILED
- [ ] last name--FAILED
- [ ] image_source--FAILED
- [ ] image_thumbnail--FAILED

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

## Credits

### Content

The text for the site was copied from

- 3 ingredient sugar cookies, https://www.delish.com/cooking/recipe-ideas/recipes/a45306/3-ingredient-sugar-cookies/

- 5 ingredient easy chocalate chip cookies, https://www.allrecipes.com/recipe/244642/5-ingredient-easy-chocolate-chip-cookies/

- 3 ingredient peanut butter cookies, https://www.biggerbolderbaking.com/3-ingredient-peanut-butter-cookies/

- chocolate kiss powder puff cookies, https://www.averiecooks.com/chocolate-kiss-powder-puff-cookies/

### Media

The photos used in this site were obtained from Google images.

- sugar cookies

- chocalate chip cookies

Recipes:

### Acknowledgements

- I received inspiration for this project from template: https://materializecss.com/, https://startbootstrap.com/previews/business-casual/

### Personal Assessment Review:

|Usability and Visual Impact|score |

|--|--|

|Project Purpose | |

|UX design||

|Suitability for purpose||

|Navigation||

|Ease of use||

|Information Architecture||

|Defensive Design||

|Layout and Visual Impact|score|

|--|--|

|Responsive Design||

|Image Presentation||

|Color scheme and typography||

|Code Quality|score|

|--|--|

|use of HTML||

|use of CSS||

|use of JavaScript||

|use of Python||

|use of template language||

|S/W practices| score|

|--|--|

|directory structure and file naming||

|version control||

|testing implementation||

|readme file||

|comments||

|data store integration||

|deployment implementation||

|deployment write up||

0 = _requirement ignored_

1 = _only partially implemented_

2 = _technical issues or flaws_

3 = _simple but achieve requirement_

4 = _achieved with excellence_
