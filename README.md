# **GT Modellista Blog - Introduction**
GT Modellista is blog site for car enthusiasts to share their passions with other like-minded individuals from around the world. This project is a Full-Stack development website built using the Django framework. GT Modellista allows registered users to post articles in two seperate categories, 'Build Threads' for vehicles and 'Diecasts' for scale-model collections. Registered users are also able to like and comment on posts made by other members of the community.

[GT Modellista](https://gt-modellista.herokuapp.com/) - The live site can be viewed here.

![Am I Responsive?](docs/read-me/responsive.png)

<hr>

## **TABLE OF CONTENTS**

 - [**User Experience (UX)**](#user-experience)
    * [User Stories](#user-stories)
    * [Agile Methodology](#agile-methodology)
    * [The Scope](#the-scope)
 - [**Design**](#design)
    * [Colours](#colours)
    * [Typography](#typography)
    * [Media](#media)
    * [Wireframes](#wireframes)
    * [Database Schema](#database-schema)
 - [**Features**](#features)
   * [Navigation](#navigation)
   * [Footer](#footer)
   * [Home Page](#home-page)
   * [About Page](#about-page)
   * [Build Threads Blog Page](#build-threads-blog-page)
   * [Featured Threads Page](#featured-threads-page)
   * [My Threads Page](#my-threads-page)
   * [Create Build Thread Page](#create-build-thread-page)
   * [Thread Details Page](#thread-details-page)
 - [**Testing**](#testing)
 - [**Technologies Used**](#technology-used)
 - [**Deployment**](#deployment)
 - [**Credits**](#credits)

<hr>

## **USER EXPERIENCE (UX)**

### **User Stories**

Unregistered site user:

- As a user, I can understand the site's purpose as soon as I land on the homepage.
- As a user, I can navigate the sites content without difficulty or confusion.
- As a user, I can view a list of all the blog posts in the 'Build Threads', 'Featured' and 'Partners' sections of the site.
- As a user, I can click on and view each blog post so I can view the content.
- As a user, I can view 'Featured Build Threads'.
- As a user, I can view how many likes each blog post has received.
- As a user, I can view the comments made on each blog post.
- As a user, I can easily locate and visit the social media links.
- As a user, I can sign up and register to the site.

Regsitered site user:

- As a user, I can perform the same actions as an unregistered site user.
- As a user, I can log in to allow me to create content and interact with the community.
- As a user, I can easily create a new blog post in the 'Build Threads' section of the site.
- As a user, I can edit/delete blog posts I have created.
- As a user, I can like/unlike blog posts.
- As a user, I can post comments on blog posts.
- As a user, I can edit/delete my comments on blog posts.
- As a user, I can view a list of the posts I have previously liked.

Site Admin/Superuser:

- As a user, I can perform the same functionalities as unregistered and registered users.
- As a user, I can create, edit and delete blog posts and post content to allow control over inappropriate content.
- As a user, I can manage the Build Threads feature functionality to maintain control over blog posts that are 'Featured Build Threads'.
- As a user, I can publish articles in the 'Sponsors and Partners' section of the site.

### **Agile Methodology**

For planning the developement and implementation of GT Modellista, a project kanban board was used as an Agile Tool through Github. This project board utilised issues as 'User Stories', a link can be found [here](https://github.com/AndyL86/gt-modellista/issues).

To help define the functionalities and prioritise key features, these 'User Stories' were broken down into 3 categories of importance; 'Must Have', 'Should Have' and 'Could Have'.

'Must Have' represents a feature or functionality that is essential to the site, 'Should Have' is a defined requirement needed for the site and 'Could Have' is determined to be optional.

### **The Scope**

#### **The Site's Main Goals:**
- To provide users with a user-friendly and positive experience when using GT Modellista.
- To provide users with a clear understanding of the site's purpose.
- To provide controlled functionality based on a user's permissions.
- To provide user's with a profile that allows them to manage their own content.

<hr>

## **DESIGN**

### **Colours**
- For the colour schema of the site I opted for a dark theme for the header and footer, using #24272C with a contrasting lighter neutral page background colour of #C0C4CA. This is so user's can easily differentiate between the different sections of the page. I used [ColourSpace](https://mycolor.space/) to generate the colour pallette I wanted.
- The button styling was inspired by the retro PlayStation 1 game 'Gran Turismo 2'. For the background colour I used #f7b91e.
- The Navigation menu and Header font colour chosen is rgb(201, 203, 204).

### **Typography**
- I chose 'Roboto Slab' for my Navigation menu and Header Title fonts, with a supporting font of 'serif' incase of loading failure. This font ide was inspired by a VW Golf GTI badge.
- The Header text and Build Thread title text use 'Noto Sans JP' and 'sans serif' as a backup. This was chosen for its clean presentation and easy readability.
- All fonts were sourced through [Google fonts](https://fonts.google.com/).

### **Media**
- [Balsamiq](https://balsamiq.com/) was used for the design of my wireframes and database schema.
- [Pexels](https://www.pexels.com/) and [Unsplash](https://unsplash.com/) were used for the header and Partners images.
- The GTM logo is my own design and post list images are my own images.

### **Wireframes**
Wireframes for each page are linked here:

[Home Page](docs/read-me/home-page.png)

[About Page](docs/read-me/about-page.png)

[Build Threads Page](docs/read-me/build-threads.png)

[Create Build Thread](docs/read-me/create-build-thread.png)

[Build Thread Posts](docs/read-me/view-build-thread-post.png)

[Featured Page](docs/read-me/featured.png)

[My Threads Page](docs/read-me/my-threads-page.png)

[Signup Page](docs/read-me/signup-page.png)

[Login Page](docs/read-me/login-page.png)

### **Database Schema**
![Database Schema](docs/read-me/data-schema.png)

<hr>

## **FEATURES**

### **Navigation**

#### **Desktop Navigation**
- The navigation bar is located at the top of each page on the site and has a sticky functionality to pin the nav bar at the top of the page when scrolled. This is to allow the user ease of navigation when browsing the site.
- The menu contains links for the 'Home Page', 'About Page', 'GT Modellista Page' and a dropdown link containing the 'Featured Threads Page', 'Register Account Page' and a 'Login Page' link. 
- Once the user is logged in the dropdown menu includes a link to the user's 'My Threads Page' and the login link is replaced with the 'Logout Page' link.
- The navbar is fully responsive and collapses into a burger menu for mobile devices.
![Desktop Nav](docs/read-me/desktop-nav.png)

#### **Mobile Navigation**
- Presented as a burger menu for design responsiveness.
- Once clicked a dropdown menu appears including all the page links as above, including the dropdown menu.
![Mobile Nav](docs/read-me/mobile-nav.png)


### **Footer**
- 
![Footer](docs/read-me/footer.png)

### **Home Page**
- Upon landing on the homepage the user is presented with a header banner which details the sites purpose and contains a click button which directs the user to the account registration page.
- Underneath the header is the carousel image real of 3 'Featured' build thread blog posts. Featured posts are selected by Admin. Navigation icons are displayed on each side of the image and a counter tab is displayed at the bottom of the image to display which image is being displayed.
- At the bottom of the page is a 'Popular' section displaying the build threads with the most likes.

### **About Page**
- The About page contains a header with styled image and the page title.
- Underneath the header is a brief description of the GT Modellista site.

### **Build Threads Blog Page**
- The Build Threads page contains all posts created by authenticated users. 
- Upon landing on the Build Threads page the user is presented with a header containing a styled image, page title and subtext. 
- Contained within the header is a click button which redirects the user to the Create Thread page.
- The page will paginate the Build Thread cards to display 6 per page.
- Each Build Thread card will display the thread title, image, author's username and the date and time the post was published.
- Each card contains a like icon and like counter to display how many likes the post has.
- Build Threads can be opened to view by clicking the thread's image.

#### **Desktop**
![Blog List](docs/read-me/blog-list.png)


### **Featured Threads Page**
- The Featured threads page displays posts selected specifically by admin.
- The header displays an image with the page title and subtext.
- Blog posts are presented in 2 columns with larger blog post cards to give a bold impression to the user.
- No users are authenticated to post build threads directly into featured.

### **My Threads Page**
- Authenticated users can view a list of their posted build threads.
- At the bottom of each blog post card displays the edit and delete buttons
![My Threads](docs/read-me/my-threads.png)

### **Create Build Thread Page**
- The Create Thread page allows authenticated users to post their own Build Thread blog post.
- The create thread form contains mandatory fields for: Vehicle Year, Vehicle Model, Vehicle Make, a link to upload an image, a text box for the user's story and a text box for the vehicle's modifications.
- Each text box uses Summernote to allow text styling to be applied.
- The create thread confirm button is located at the bottom of the page.
- If an unauthenticated user tries to access the Create Thread page they are presented with an access denied error.
![Create Thread](docs/read-me/create-post.png)

### **Thread Details Page**
- When a Build Thread is selected the user is brought to the Thread Details page detailing all the information the author has provided.
- The main body of the page displays the vehicle year, make and model as the page title, below this are 2 text box areas containing the 'Story' and 'Modifications' sections and the thread image.
- Below the image is a 'heart' icon with a number counter, this allows authenticated users to like the thread and provides a total number of likes to all users.
- Alternatively, if the heart icon has already been selected showing a like, the heart can be unselected to remove the like.
![Thread Details](docs/read-me/thread-details.png)

### **Comments Section**
- At the bottom of the page all users are able to view the comments section.
- Authenticated users are able to leave comments.
![Comments Section](docs/read-me/comments.png)

#### **Edit/Delete Comments**
![Edit/Delete Comments](docs/read-me/edit-comments.png)

<hr>

## **ACCOUNTS**

### **Register Account**
![Regsiter Account](docs/read-me/register.png)

### **Log in**
![Log In](docs/read-me/login.png)

### **Sign out**
![Sign Out](docs/read-me/signout.png)

### **Access denied**
![Access Denied](docs/read-me/denied.png)

<hr>

## **TESTING**

Testing and results can be found [here](TESTING.md)

<hr>

## **TECHNOLOGIES USED**

### Languages used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)

### Libraries and Programs Used

- [Git](https://git-scm.com/)<br>
   Used for version control alongside GitHub.
- [GitHub](https://github.com/)<br>
   Used to store the project and utilise git version control.
- [Heroku](https://id.heroku.com)<br>
   Used to deploy project.
- [Cloudinary](https://cloudinary.com/)<br>
   Cloud based storage, used for storing any media submitted by users.
- [ElephantSQL](https://www.elephantsql.com/)<br>
   Used to host the PostgreSQL database.
- [W3C - HTML](https://validator.w3.org/)<br>
   Used to validate all HTML code.
- [W3C - CSS](https://jigsaw.w3.org/css-validator/)<br>
   Used to validate all CSS code.
- [CI PEP8 Testing](https://pep8ci.herokuapp.com/)<br>
   Used to validate all Python code.
- [Google Fonts](https://fonts.google.com/)<br>
   Used to provide the font styling.
- [Bootstrap](https://getbootstrap.com/)<br>
   Used to for helping with the HTML design and layout.
- [Fontawesome](https://fontawesome.com/)<br>
   Used to implement effective icons.
- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)<br>
   Used during the development to debug and test responsiveness.
- [Balsamiq](https://balsamiq.com/)<br>
   Used to build both the database schema diagram and design wireframes.

<hr>

## **DEPLOYMENT**

### ** Create Github Repository **
- Log in to your Github account.
- Navigate to repositories and select 'New'.
- Select the 'Code Institute' template from the 'Repository Template' menu.
- Give your repository a name and select 'Create Repository'.
- When the repository has been created select 'Gitpod' to open a new workspace.

### ** Heroku **
- Log in to your Heroku account [Heroku](https://id.heroku.com).
- From the home page select 'New', then select 'Create New App' from the drop-down.
- Provide a name for your app and selectyour regrion.
- Add 3 new keys along with your relevant value information: 'SECRET_KEY', 'DATABASE_URL' and 'ClOUDINARY_URL'. 
- At the top of the page select the 'Deploy' tab.
- For the preferred deployment method select 'Github'.
- Search for your repository name and connect.
- Additionally, automatic deploys can be enabled for deployment after each push to Github.

### ** Fork this project **
- Sign in to Github and go to my [repository](https://github.com/AndyL86/gt-modellista)
- At the top of the page select 'Fork'.
- The Fork will now be added to your repositories.

### ** Clone this project **
- Sign in to Github and go to my [repository](https://github.com/AndyL86/gt-modellista)
- Select the green 'Code' button.
- Select from one of the cloning options HTTPS, SSH or Github CLI. Click the clipboard icon to copy the URL.
- Open git bash
- Enter ‘git clone’ into the text box and then paste the respository URL and select enter. 

For more information on cloning please read the github documentation [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

<hr>

## **Credits**