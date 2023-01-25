# **GT Modellista Blog - Introduction**
GT Modellista is blog site for car enthusiasts to share their passions with other like-minded individuals from around the world. This project is a Full-Stack development website built using the Django framework. GT Modellista allows registered users to post articles in two seperate categories, 'Build Threads' for vehicles and 'Diecasts' for scale-model collections. Registered users are also able to like and comment on posts made by other members of the community.

[GT Modellista](https://gt-modellista.herokuapp.com/) - The live site can be viewed here.

![Am I Responsive?](docs/read-me/responsive.png)

## **TABLE OF CONTENTS**
<hr>

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
 - [**Testing**](#testing)
 - [**Technologies Used**](#technology-used)
 - [**Deployment**](#deployment)
 - [**Credits**](#credits)

## **USER EXPERIENCE (UX)**
<hr>

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

## **DESIGN**
<hr>

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
- [Pexels](https://www.pexels.com/) was used for the header images.
- The GTM logo is my own design and post list images are my own images.

### **Wireframes**
Wireframes for each page are linked here:

[Home Page](docs/read-me/home-page.png)

[About Page](docs/read-me/about-page.png)

[Build Threads Page](docs/read-me/build-threads.png)

[Create Build Thread](docs/read-me/create-build-thread.png)

[Build Thread Posts](docs/read-me/view-build-thread-post.png)

FEATURED WIREFRAME

MY THREADS WIREFRAME

[Partners Page](docs/read-me/partners.png)

[Partnerss Posts](docs/read-me/view-partners-post.png)

[Signup Page](docs/read-me/signup-page.png)

[Login Page](docs/read-me/login-page.png)

### **Database Schema**
![Database Schema](docs/read-me/data-schema.png)

## **FEATURES**
<hr>

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

### **Home Page**
- Upon landing on the homepage the user is presented with a header banner which details the sites purpose and contains a click button which directs the user to the account registration page.
- Underneath the header is the carousel image real of 3 'Featured' build thread blog posts. Featured posts are selected by Admin. Navigation icons are displayed on each side of the image and a counter tab is displayed at the bottom of the image to display which image is being displayed.
- At the bottom of the page is a 'Trending' section displaying the build threads with the most likes.

### **About Page**
- The 'About' page contains a header with styled image and the page title.
- Underneath the header is a brief description of the GT Modellista site.

### **Build Threads Blog Page**
- Upon landing on the 'Build Threads' page the user is presented with a header containing a styled image and the page title and subtext.
- Contained within the header is a click button which redirects the user to the 'Create Thread' page.
- The Build Threads page is the main focal point of the GT Modellista site and contains each blog post by an authenticated user.
- The page will paginate the Build Thread cards to display 6 per page.
- Each Build Thread card will display the thread title, image, author's username and the date and time the post was published.
- Each card contains a like icon and like counter to display how many likes the post has.
- Build Threads can be opened to view by clicking the thread's image.

### **Create Build Thread Page**
- The Create Thread page allows authenticated users to post their own Build Thread blog post.
- The create a thread form contains mandatory fields for: Vehicle Year, Vehicle Model, Vehicle Make, a link to upload an image, a text box for the user's story and a text box for the vehicle's modifications.
- Each text box uses Summernote to allow text styling to be applied.
- The create thread confirm button is located at the bottom of the page.
- If an unauthenticated user tries to access the Create Thread page they are presented with an access denied error.

### **Edit Build Thread Page**

### **Thread Details Page**
- Once a Build Thread is selected the user is brought to the Thread Details page.


### **Comments Section**

### **Featured Threads Page**

### **My Threads Page**

## **ACCOUNTS**
<hr>


## **TESTING**
<hr>

## **TECHNOLOGIES USED**
<hr>

## **DEPLOYMENT**
<hr>

## **Credits**
<hr>