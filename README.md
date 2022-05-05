# MyAPPocalypse (UCD Project 4)
Ready to hit the road when your world ends ?

Hopefully the time will never come when all you know is gone and suddenly you find yourself on the road in this big world, but it is never a bad idea to be prepared!
MyAPPocalypse helps you put together your bag for any possible scenario - no matter if you are on the Antarctis or in the Sahara, be assured you have a bag to grab when it is time to leave behind your place.
Here you may define the parameters of your bag (local conditions or special company like child or pet) and then select from the recommended items to fill it. If you are on the roll, you may also directly consult the latest offers of Amazon while cherry-picking from the proposed items, and if you find that something is missing from the list, you can recommend it and once approved, it will be available for selection.
Sign up (even with your social media accounts) and look around, prepare your bag and leave your thoughts for further improvements to raise the odds against vis-major events!

![Responsive Layouts](/static/img/readme/responsive-design.PNG)

Deployed app on [Heroku](https://heroku.com) : https://vast-shore-97005.herokuapp.com / \
Technologies : Python + Django + HTML + CSS + Javascript/jQuery \
Software : [PyCharm](https://www.jetbrains.com/pycharm/)

## Agile Development
### 1. Basic expectations
* Expectations as a user :
  * be able to navigate through the site easily through any device.
  * be able to get informed why the application may be useful.
  * be able to define and pack one or more bags with items.
  * be able to recommend items if it is missing from the list of available items to pack.
  * be able to leave star-based rating and/or text comment about the site.
  * be able to consult / delete own feedbacks / item recommendations.
  * be able to consult / delete / modify own bags.
  * be able to see the all own contributions in one place (profile page).
* Expectations as a site owner :
  * the site to be tastefully and creatively designed.
  * the content is presented in an tasteful way (regarding heavy subject).
  * the site to be clearly structured for easy navigation.
  * the bag packing function works as intended and handle empty/incorrect user inputs.
  * the feedback/rating function works as intended and handle empty/incorrect user inputs.
  * the users' item recommendations for approval / reject to be easily managed.
  * the users' contributions to be easily controlled by admin.
  * the users enjoy spending time with the application, get inspired for a real bag and learn something new.
### 2. Agile Process Overview
The project was developed in 5 sprints with 5 milestone dates. During the development process, the expectations were mapped to user stories with related user acceptance criteria(s), with associated story points (scale from 10 to 50) and with related tasks to perform, each story belonging to one or more from the 5 epics, a group of stories targeting the same area of development. High-importance user stories were marked as priorities in order to set up an order of execution.
The aim was to finalize each iteration for the determined milestone, which means the completion of the tasks related to the user stories which are associated to the given iteration until the deadline. The iterations include user stories belonging to more epics, but each iteration has a higher focus on a given epic, mirroring the development of the work. During the finalisation of the user stories belonging to an iteration, the high-priority user stories got more focus and higher level of attention.
### 3. Agile Tools
During the development, regarding tight time-frame, the classic method was used with table and post-its, however for better presentation, the development process was translated to Github tools.
* [Github Project = Work Project (1)](https://github.com/SofiaHorvath91/ucd_project_4/projects/1)
  * A project 'UCD Project 4 : MyAppocalypse' was created to contain the agile development work done to build up the application, containing milestones and prioritized user stories belonging to different epics. The project grouped the user stories based on three statuses in a Kanban view : To do / In progress / Done, based on the level of completion.
* [Github Milestones = Iterations / Sprints (5)](https://github.com/SofiaHorvath91/ucd_project_4/milestones)
  * Milestones were used to represent a work sprint with precised deadline which is served to keep in line the project development in order to respect the final deadline. During each iteration of the work, a different epic was prioritised, allowing the timely build of the full site and the continous testing from the beginning.
  * The 5 iterations : Iteration 0 / Iteration 1 / Iteration 2 / Iteration 3 / Iteration 4
* [Github Issues = User stories (28)](https://github.com/SofiaHorvath91/ucd_project_4/issues?q=)
  * Issues were used to represent user stories, all created using an issue template ('User Story'). A user story contains the description of the story ('as a ... I can ... so that ...'), the related epic(s), the corresponding user story points, the related tasks and the user acceptance criteria(s). Each story belongs to a milestone sprint (iteration), and each story is labeled based on related epic(s), and high-priority stories are further labeled as priorities. All stories are assigned to admin / site owner.
  * Github Issue template was used to provide a coherent view and content for the user stories, created as Issues.
* [Github Labels = Epics (5) +  High-Priority user stories (13)](https://github.com/SofiaHorvath91/ucd_project_4/labels)
  * Labels were used to connect user stories to one or more of the 5 epics, which are groups of stories targeting the same aspect of development. Each epic is represented by a label colored differently to be able to better distinct them, and the 5 epic together include all kind of works which should be done to build the application.
  * The 5 epics : Admin-specific Action / Feedback / Main Functionality / Site Structure / User Authentication
  * Labels were also used to create a Priority label to be able to tag high-priority user stories which require more attention and work, as they concern the core functionnalities of the site. 
### 4. Agile Method Details
Please find below the 5 iterations and the user stories with respective story points which was expected to be finalized until the milestone of the given iteration, all stories grouped by epics. By clicking on the name of the iterations, you may consult the screenshot of the project dashboard at the end of each iteration, so at each milestone. By clicking on the user stories, you may consult the related Github Issue with all the details about the given story. By clicking on the link of qet to-do user stories, you may consult their list.

[Iteration 0 : Brainstorming about site's main theme and lay out site's basic functionalities. => Milestone : 30/01/2022 (1 Story)](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/Iteration0_End_31012022.png)

* Epic 'Admin-specific Action'
  * [User Story : Project idea and site draft for site owner (admin)](https://github.com/SofiaHorvath91/ucd_project_4/issues/26) (SP 45) => Priority

[Iteration 1 : Setting up the technical skeleton of the site with main framework and APIs to use. => Milestone : 28/02/2022 (8 Stories)](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/Iteration1_End_28022022.png)

* Epic 'User Authentication'
  * [User Story : Basic links' availability for not-authenticated users](https://github.com/SofiaHorvath91/ucd_project_4/issues/1) (SP 40)
  * [User Story : Features' availability for authenticated users](https://github.com/SofiaHorvath91/ucd_project_4/issues/2) (SP 40)
  * [User Story : Login for not-authenticated user with existing account](https://github.com/SofiaHorvath91/ucd_project_4/issues/4) (SP 50) => Priority
  * [User Story : Sign up for not-authenticated user without existing account](https://github.com/SofiaHorvath91/ucd_project_4/issues/5) (SP 50) => Priority
  * [User Story : Switching between connected accounts (created via standard / social way)](https://github.com/SofiaHorvath91/ucd_project_4/issues/6) (SP 45)
  * [User Story : Logout for authenticated users](https://github.com/SofiaHorvath91/ucd_project_4/issues/7) (SP 50)
* Epic 'Site Structure'
  * [User Story : Basic links' availability for not-authenticated users](https://github.com/SofiaHorvath91/ucd_project_4/issues/1) (SP 40)
  * [User Story : Features' availability for authenticated users](https://github.com/SofiaHorvath91/ucd_project_4/issues/2) (SP 40)
  * [User Story : Starting page information](https://github.com/SofiaHorvath91/ucd_project_4/issues/3) (SP 40)
  * [User Story : Understanding site's goal as a general (particularly a not-authenticated) user](https://github.com/SofiaHorvath91/ucd_project_4/issues/8) (SP 35)

[Iteration 2 : Building site's MVC (Model-View-Controller) logic and thus setting up site's main functionalities on backend/frontend. => Milestone : 20/03/2022 (12 Stories)](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/Iteration2_End_20032022.png)

* Epic 'Main Functionality'
  * [User Story : Creating a bag function for authenticated users](https://github.com/SofiaHorvath91/ucd_project_4/issues/9) (SP 50) => Priority
  * [User Story : Adding items to a bag function for authenticated users](https://github.com/SofiaHorvath91/ucd_project_4/issues/10) (SP 50) => Priority
  * [User Story : Consulting current bag weight while adding items to a bag for authenticated users](https://github.com/SofiaHorvath91/ucd_project_4/issues/11) (SP 35)
  * [User Story : Opening pop-up modal with item details and Amazon buying option for authenticated user](https://github.com/SofiaHorvath91/ucd_project_4/issues/12) (SP 38)
  * [User Story : Upon editing existing bag, added items and current weight are displayed for authenticated user](https://github.com/SofiaHorvath91/ucd_project_4/issues/13) (SP 48) => Priority
  * [User Story : Bag Detail page with CRUD quick-actions for authenticated users](https://github.com/SofiaHorvath91/ucd_project_4/issues/14) (SP 50) => Priority
  * [User Story : Authentication- / Owner-based record access for authenticated/not-authenticated/admin users](https://github.com/SofiaHorvath91/ucd_project_4/issues/20) (SP 48) => Priority
* Epic 'User Authentication'
  * [User Story : Authentication- / Owner-based record access for authenticated/not-authenticated/admin users](https://github.com/SofiaHorvath91/ucd_project_4/issues/20) (SP 48) => Priority
* Epic 'Feedback'
  * [User Story : Profile page with CRUD quick-actions for authenticated users](https://github.com/SofiaHorvath91/ucd_project_4/issues/15) (SP 40) => Priority
  * [User Story : Profile page with CRUD quick-actions for authenticated admin users](https://github.com/SofiaHorvath91/ucd_project_4/issues/16) (SP 45)
  * [User Story : Feedback / Recommendation options for authenticated users](https://github.com/SofiaHorvath91/ucd_project_4/issues/17) (SP 45) => Priority
  * [User Story : Feedback management for authenticated admin users](https://github.com/SofiaHorvath91/ucd_project_4/issues/18) (SP 40)
  * [User Story : Sharing site on social media via footer buttons for general users](https://github.com/SofiaHorvath91/ucd_project_4/issues/19) (SP 10)
* Epic 'Site Structure'
  * [User Story : Profile page with CRUD quick-actions for authenticated users](https://github.com/SofiaHorvath91/ucd_project_4/issues/15) (SP 40) => Priority
* Epic 'Admin-specific Action'
  * [User Story : Profile page with CRUD quick-actions for authenticated admin users](https://github.com/SofiaHorvath91/ucd_project_4/issues/16) (SP 45)
  * [User Story : Feedback management for authenticated admin users](https://github.com/SofiaHorvath91/ucd_project_4/issues/18) (SP 40)

[Iteration 3 : Setting up automatic and manual testing, then final deployment of site to Production. => Milestone : 27/03/2022 (1 Story)](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/Iteration3_End_27032022.png)

* Epic 'Admin-specific Action'
  * [User Story : Testing of site functionality and design for authenticated admin](https://github.com/SofiaHorvath91/ucd_project_4/issues/27) (SP 35) => Priority

[Iteration 4 : Correction of frontend/backend issues after deployment in Production and final deployment for evaluation. => Milestone : 05/05/2022 (6 Stories)](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/Iteration4_End_05052022.png)

* Epics 'Admin-specific Action' and 'Main Functionality'
  * [User Story : Correcting site functionality errors to ensure smooth site usage for all type of users](https://github.com/SofiaHorvath91/ucd_project_4/issues/28) (SP 50) => Priority

[User stories left to implement after last Iteration 4](https://github.com/SofiaHorvath91/ucd_project_4/issues?q=is%3Aopen+is%3Aissue)

* Epic 'Admin-specific Action'
  * [User Story : Item CRUD / List View Pages for authenticated admin users](https://github.com/SofiaHorvath91/ucd_project_4/issues/21) (SP 28)
  * [User Story : Recommendation To Item Page for authenticated admin user](https://github.com/SofiaHorvath91/ucd_project_4/issues/22) (SP 25)
* Epic 'Main Functionality'
  * [User Story : Persisting user input upon page reload for authenticated users](https://github.com/SofiaHorvath91/ucd_project_4/issues/23) (SP 30) => Priority
  * [User Story : Modal with further information about possible conditions upon bag creation for authenticated user](https://github.com/SofiaHorvath91/ucd_project_4/issues/24) (SP 25)
* Epic 'Site Structure'
  * [User Story : Modal with further information about possible conditions upon bag creation for authenticated user](https://github.com/SofiaHorvath91/ucd_project_4/issues/24) (SP 25)
  * [User Story : Add images to item pop-up modal with item details for authenticated users](https://github.com/SofiaHorvath91/ucd_project_4/issues/25) (SP 15)
### 5. Agile Statistics
Calculation of the user story points per standard/priority user stories per iterations to see done and remaining work backlog.
* Iteration 0 : 1 User Story = Total 45 User Story Points (4% of Total User Story Points)
  * Standard User Story Points 0 (0%) => Completed 0 (0%) + Uncompleted 0 (0%)
  * Priority User Story Points 45 (4%) => Completed 45 (4%) + Uncompleted 0 (0%)
* Iteration 1 : 8 User Stories = Total 350 User Story Points (32% of Total User Story Points)
  * Standard User Story Points 250 (22%) => Completed 215 (21%) + Uncompleted 35 (1%)
  * Priority User Story Points 100 (10%) => Completed 100 (10%) + Uncompleted 0 (0%)
* Iteration 2 : 12 User Stories = Total 499 User Story Points (45% of Total User Story Points)
  * Standard User Story Points 168 (12%) => Completed 168 (12%) + Uncompleted 0 (0%)
  * Priority User Story Points 331 (33%) => Completed 331 (33%) + Uncompleted 0 (0%)
* Iteration 3 : 1 User Story = Total 35 User Story Points (3% of Total)
  * Standard User Story Points 0 (0%) => Completed 0 (0%) + Uncompleted 0 (0%)
  * Priority User Story Points 35 (3%) => Completed 35 (3%) + Uncompleted 0 (0%)
* Iteration 4 : 6 User Stories = Total 173 User Story Points (16% of Total)
  * Standard User Story Points 93 (9%) => Completed 0 (0%) + Uncompleted 93 (9%)
  * Priority User Story Points 80 (7%) => Completed 50 (4%) + Uncompleted 30 (3%)
* **Total User Story Points 1102 / 28 User Stories : Completed 989 (88%) + Uncompleted 123 (12%)**
  * **Standard User Story Points 511 (43%) => Completed 418 (34%) = 10 User Stories + Uncompleted 93 = 5 User Stories (9%)**
  * **Priority User Story Points 591 (57%) => Completed 571 (54%) = 12 User Stories + Uncompleted 30 = 1 User Story (3%)**

## UX
### 1. Strategy
* Purpose of Project
  * To make sure users have the chance to virtually prepare for a heavy real-life scenario
  * To have users to pack one or more bags with chosen items, depending on user-defined special conditions
  * To allow users leave their toughts and recommendations for further site improvement.
  * To give users an overview and educate them about what is needed in vis-major situations.
### 2. Scope
* I wanted a simple, evident and user-friendly UX experience.
* I wanted clear and informative content.
* I wanted a visually appealing, yet solid design.
* I wanted interesting and thought-provoking site description.
* I wanted smooth and interactive bag-packing and feedback experience.
### 3. Structure
* The layout is simple and clear to ensure the easy navigation through site content by users
* The navigation bar is clear, fixed, visible and responsive with matching site logo. 
* The content is easy to read, bag packing function and feedback-leaving function are smooth with self-explanatory steps.
* The Home page displays clearly the site’s main subject, allows to explore site content, and appeal visitors to stay and sign up / login to discover.
* The Why a Bag page allows users to discover the site's objective and verify the usefulness of site.
* The Login / Sign Up pages allows users to register or to connect if already registered, via standard form or vi social account.
* The Logout page allows logged in users to disconnect from site.
* The Pack A Bag page allows logged in users to define the basic and special parameters of a bag, and then create it.
* The Add Items page allows logged in users to add condition-specific items to their newly created bag, as well as modify the items in their existing bag(s).
* The Bag Details page allows logged in users to consult one of their bags for modification / removal option if needed.
* The Blog page allows users to consult previous feedbacks, as well as the creation of their own star-based / comment feedback(s) and the recommendation of new item(s).
* The Profile page allows users to see their own bags / feedbacks / recommendations in one place, with quick links for delete / new record / modification.
* In the Footer, users can find copyrights and the icon buttons to share site on different social media platforms.
### 4. Skeleton
The very basic skeleton of the site was modelled by Wireframes via Balsamiq, and during site development, additional design elements was added for better UX.
* [Home Page Wireframe](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/balsamiq-home.png)
* [Why A Bag Page Wireframe](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/balsamiq-whyabag.png)
* [Pack A Bag Page Wireframe](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/balsamiq-packmybag.png)
* [Add Items Page Wireframe](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/balsamiq-mybag_add_items.png)
* [Bag Details Bag Page Wireframe](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/balsamiq-mybag_details.png)
* [Blog Page Wireframe](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/balsamiq-blog.png)
* [Profile Page Wireframe](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/balsamiq-profile.png)
* [Sign Up / Login Page Wireframe](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/balsamiq-login_signup.png)
### 5. Style
* Design & Colours
  * When planning the project, I wanted a very simple design, not too grim but neither too playful, so I after firstly goind with a reddish background, I finally decided to choose a simple, but visually appealing blueish background image, and white text with black border to ease the effect of the heavy subject. While the blue shade of the site is rather dark blue, but with some glowing parts and white fonts, the page gives a rassuring, calm atmosphere, emphasizing the importance of being prepared and stable in a dangerous context.
* Font Selection
  * The main font type was chosen with [Google Fonts](https://fonts.google.com/) and is used across the whole of the website: [Cagliostro](https://fonts.google.com/specimen/Cagliostro?query=Cagliostro). This is a well readable font type which yet gives a practical, yet personal feeling feeling which I found suitable for the subject of the site : the topic itself is pragmatic, but the circonstances are very personal.
### 6. Code Structure and Database
* Code Structure\
The project is consisted of one application, MyAPPocalypse, built by using the Django Framework. The business logic is executed by this application, based on the ucd_projct_4 settings, using the static resources like HTML page frame / CSS stylesheet / Javascript-jQuery script.\
The application is completed by the following files/directories :
  * ucd_project_4: Containing settings.py(Settings) and urls.py(Website urls)
  * templates: Containing the base.html as HTML pages' frame
  * static: CSS files, Javascript files, images
  * node_modules : Node installation for Javascript testing with Jest
  * package.json : Json file created for Javascrip testing with Jest
  * manage.py: Main python file for starting the website
  * README.md: Readme documentation
  * Procfile: To run the application
  * Requirements.txt: Containing the python libraries installed
* Database\
The website is a data-centric one with frontend built with HTML, Javascript, CSS along with Bootstrap framework.
The backend consists of Python built with the Django framework with a database of a Postgres for the deployed Heroku version (Production)
[Postgres](https://www.postgresql.org/) is an open source object-relational database system with powerful features
[SQLLite](https://www.sqlite.org/index.html) database was used for local development and testing.
### 7. Database Models
The following models were created to represent the database model structure for the website (visual schema made by [DbDesigner](https://app.dbdesigner.net/)):\
![Database models' visual schema](/static/img/readme/database_models_schema.PNG)
* User Model
  * The User model contains information about the user. It is part of the Django social auth library. As no particular customization was needed ofr User model, get_user_model() lazy loading ws used.
* Climate
  * Capture details of possible climates to associate to the road where the bag will be used
  * Connected to Items (via ManyToMany relation) / Bags (via ForeignKey relation)
  * ClimateSerializer is used to pass Climate to Item model
* Landform
  * Capture details of possible landforms to associate to the road where the bag will be used
  * Connected to Items (via ManyToMany relation) / Bags (via ForeignKey relation)
  * LandformSerializer is used to pass Climate to Item model
* Environment
  * Capture details of possible environments to associate to the road where the bag will be used
  * Connected to Items (via ManyToMany relation) / Bags (via ForeignKey relation)
  * EnvironmentSerializer is used to pass Climate to Item model
* Item
  * Capture details of physical objects to be packed in the bag
  * Models/objects connected to Item model/object via ManyToMany relation : Climate, Landform, Environment
  * Models/objects to which Item model/object is connected via ManyToMany relation : Bag
  * ItemSerializer is used to pass Item to Bag model
* Bag
  * Main object/model of the application
  * Capture details of bag packed for a given scenario (general details & related items)
  * Models/objects connected to Bag model/object via ManyToMany relation : Items
  * Models/objects connected to Bag model/object via ForeignKey relation : Climate, Landform, Environment, User
* Feedback
  * Capture details of feedback provided by the user about the site (rating & comment)
  * Models/objects connected to Feedback model/object via ForeignKey relation : User
* Recommendation
  * Capture details of feedback provided by the user about the site (rating & comment)
  * Models/objects connected to Feedback model/object via ForeignKey relation : User

## Features
### 1. Existing Features
* __Navigation Bar__
  * Featured on all pages, the navigation bar includes links to all subpages and is identical on each page for smooth navigation. The navbar is fixed and fully responsive on all screen sizes: for smaller devices, a hamburger navbar view is included with the help of Bootstrap for better UX and easier navigation. Navbar also shows different available pages based on user's authentication status.

Navbar on Desktop - Logged Out\
![Navbar desktop](/static/img/readme/navbar-desktop-loggedout.png)
Navbar on Desktop - Logged In\
![Navbar mobile](/static/img/readme/navbar-desktop-loggedin.png)
Navbar on Mobile - Logged In\
![Navbar mobile](/static/img/readme/navbar-mobile.png)

User stories :\
As a not authenticated user, I expect to see the basic links and easily find sign up to see more\
As an authenticated user, I expect to see all avaiable site features in navbar

* __Home Page__
  * Presenting MyAPPocalypse, the home page clearly and briefly indicates site objective and also offers entry point to available sites based on  on user's authentication status which allow users to immediately dive into the app. Unregistered or logged out users can know more about the site and/or sign up, logged in users can consult their profile, navigate to the blog or create a new bag.

Home Page - Logged Out\
![Home Page](/static/img/readme/page-home-loggout.png)
Home Page - Logged In\
![Home Page](/static/img/readme/page-home-loggin.png)

User stories :\
As a not authenticated user, I expect to understand site's objective and easily find sign up link\
As an authenticated user, I expect to easily navigate to my profile and to site actions (bag creation, feedback)

* __Login / Sign Up Page__
  * These pages allow user to sign up or to login via standard verification form, or via social media account (Facebook, Twitter, Google).

Login Page\
![Login Page](/static/img/readme/page-login.png)
Sign Up Page\
![Sign Up Page](/static/img/readme/page-signup.png)

User stories :\
As a not authenticated user with account, I expect to login via standard form or social auth buttons (Facebook, Twitter, Google)\
As a not authenticated user without account, I expect to be able to create user account via standard form or sign up via social auth buttons (Facebook, Twitter, Google)\
As an authenticated user, I expect to easily switch account if I use more usernames via standard and social channels\
As general user I expect to be logged out by clicking on Logout option in navbar

* __Why A Bag page__
  * This page has the aim of explaining better the site objective, giving a context to the bag packing function, and informing users about the possible advantages of using the app.

Why A Bag Page\
![Why A Bag Page](/static/img/readme/page-whyabag.png)

User stories \
As general, particularly a not authenticated user, I expect to learn more about the site's objective\
As an admin, I expect to have a site faithful to the mission described on this page

* __Pack A Bag Page__
  * This page allows the users to profit from the main functionality of the site : they can create a bag based on different parameters in which they can then add items with respect to the max weight of bag (calculated upon user weight).

Pack A Bag Page\
![Pack A Bag Page](/static/img/readme/page-packmybag.png)

User stories\
As an authenticated user, I expect to be able to create a bag easily by providing special details\
As an authenticated user, I expect to be navigated through required information to not crash application\
As a not authenticated user, I expect to not to see this page

* __Add Items Page__
  * This page allows user to add items to the newly created or to an existing bag, depending if navigation from Pack My Bag page or Profile/Bag Details pages' edit function. Current weight of bag is dynamically calculated upon adding/removing items to/from bag, and user is alerted is bag's max weight is reached and no more items can be added. While adding items, user may consult the details of the item in a pop-up modal by clicking on the information sign next to it's name. The modal also provides click link to Amazon buying options.
If navigating via Edit Items link , the items already in the bag are preselected and bag's actual weight is displayed for further calculation upon modifying items. Once items are added, changes to be saved to add items to bag.

Add Items Page\
![Add Items Page](/static/img/readme/page-mybag_add_items.png)

Add Items Page - Pop-Up Modal with Item Details\
![Add Items Page - Pop-Up Modal with Item Details](/static/img/readme/page-mybag_modal_item.png)

User stories\
As an authenticated user, I expect to be able to add items to the newly created or to an existing bag\
As an authenticated user, I expect to know the current exact weight of my pag while packing for better planning\
As an authenticated user, I expect to be alerted when maximum bag size is reached to be able to rethink choices\
As an authenticated user, I expect to be able to consult item details in pop-up modal via clicking on information sign\
As an authenticated user, I expect to be offered an Amazon links for buying options of the item while in pop-up modal via clicking on an item's information sign\
As an authenticated user, when adding items to new bag, I expect that starting bag weight is zero\
As an authenticated user, when editing am existing bag, I expect that the items already in the bag are preselected and bag's actual weight is displayed for further calculation\
As a not authenticated user, I expect to not to see this page

* __Bag Details Page__
  * This page allows user to consult the parameters and items of an existing bag the user owns.  While checking the bag, user may consult the details of the added items in a pop-up modal by clicking on the information sign next to it's name (as on Add Item page's modal). The modal also provides click link to Amazon buying options. The page also gives quick link to modify items or delete bag as well as to new bag creator page.

Bag Details Page\
![Bag Details Page](/static/img/readme/page-mybag_details.png)

User stories\
As an authenticated user, I expect to consult the parameters and items of an existing bag what I own\
As an authenticated user, I expect to have quick links for new bag / update bag / delete bag actions\
As an authenticated user, I expect to be able to consult item details in pop-up modal via clicking on information sign\
As an authenticated user, I expect to be offered an Amazon links for buying options of the item while in pop-up modal via clicking on an item's information sign\
As a not authenticated user, I expect to not to see this page

* __Profile Page__
  * This page allows user to consult the provided feedbacks, the given recommendations and the created bags in one place, facilitating the record management for the user. Via profile, it is possible to delete any created record, as well as to navigate toward new record creation and for bags, toward detail and edit pages.
For admins, it is also possible to consult here all the recommendations to be approved or rejected, and approve or reject right on the spot.

Profile Page - Main Sections\
![Profile Page - Main Sections](/static/img/readme/page-profile.png)

Profile Page - Check My Bags\
![Profile Page - Check My Bags](/static/img/readme/page-profile2.png)

Profile Page - Recommendations as owner\
![Profile Page - Recommendations as owner](/static/img/readme/page-profile3.png)

Profile Page - Recommendations as admin\
![Profile Page - Recommendations as admin](/static/img/readme/page-profile4.png)

Profile Page - My Feedbacks as admin (all users' feedbacks visible/deletable)\
![Profile Page - My Feedbacks](/static/img/readme/page-profile5.png)

Profile Page - My Feedbacks as authenticated user (own feedbacks visible/deletable)\
![Profile Page - My Feedbacks](/static/img/readme/page-profile6.png)

User stories\
As an authenticated user, I expect to consult my provided feedbacks, given recommendations and created bags in one place\
As an authenticated user, I expect to have quick links for new inputs / delete inputs, optionally update inputs\
As an authenticated admin user, I expect to consult here all the recommendations to be approved or rejected (status Pending)\
As an authenticated admin user, I expect to be able to approve or reject pending recommendations, and then clear this item from the Recommendations section\
As a not authenticated user, I expect to not to see this page

* __Blog Page__
  * This page allows user to give star-based rating and/or written feedback about the site to share points of improvement and overall satisfaction. User also have the possibility here to recommend an item what the user is missing from the list of existing items. Newly created recommendation appears under My Recommendations section of Profile page. User can also check all exisiting feedbacks, and for own feedbacks in the list, a quick link is provided for removal in case the user wishes to delete it.

Blog Page - Leave Your Feedback\
![Blog Page - Leave Your Feedback](/static/img/readme/page-blog1.png)

Blog Page - Recommend an Item\
![Blog Page - Recommend an Item](/static/img/readme/page-blog2.png)

Blog Page - Check All Feedbacks\
![Blog Page - Check All Feedbacks](/static/img/readme/page-blog3.png)

User stories\
As an authenticated user, I expect to be able to give star-based rating and/or written feedback about the site\
As an authenticated user, I expect to be able to recommend an item what the I miss from the list of existing items\
As an authenticated user, I expect to the feedbacks and recommendations given here appear in the approprite section of my profile\
As an authenticated user, I expect to be able to check all exisiting feedbacks\
As an authenticated user, I expect to be able to delete my feedbacks from list of all feedbacks\
As an authenticated admin user, I expect to be able to delete any feedback item from list\
As a not authenticated user, I expect to not to see this page\

* __Footer__
  * The footer section includes copyrights and it also allows to share this website with other people through social media sites and email via social share buttons. 

Footer\
![Footer](/static/img/readme/page-footer.png)

User stories\
As a general user, I expect to be able to share this site via social media buttons

### 2. Future Features
* Adding item creation page for admin (for giving option between UI and Django admin site)
  * User story : As an admin user, I expect to be able to create items directly via user interface, without navigation to Django admin platform
* Transform recommendation instantly into item upon approval
  * User story : As an admin user, I expect to be able to create item automatically from approved user item recommendation
* Save latest user session information in forms if page rerendered
  * User story : As an authenticated user, I expect that while filling forms, if site rerendered, my latest inputs remain in place
* Add descriptive pop-up for company / locale / condition selection
  * User story : As an authenticated user, I expect more information about the conditions set up while creating a bag
* Give image to item details pop-up modal to illustrate item
  * User story : As an authenticated user, I expect an illustration for the recommended item while checking details in pop-up for better understanding
### 3. Technologies Used
* Languages
  * HTML : The project uses html to build the relevant pages
  * CSS : The project uses CSS to style the relevant pages
  * Javascript : Used for client-side scripting on the site
  * Django : Django is the framework used in this project
  * The Django templating language was used to render pages
  * The Django unit test library was used for unit tests
  * The Django social authentication application was used for social login
  * Python v3.9 : Used for server side coding with a number of libraries (listed in requirements.txt)
* APIs used for social login feature
  * Facebook API (https://developers.facebook.com/)
  * Twitter API (https://developer.twitter.com/)
  * Google API (https://console.cloud.google.com/)
* Libraries and other resources
  * Bootstrap 5.0 (https://getbootstrap.com/docs/5.0)
  * Postgres (https://www.postgresql.org/)
  * SQLLite (https://www.sqlite.org/index.html)
  * GitBash (https://git-scm.com/downloads)
  * Pycharm (https://www.jetbrains.com/pycharm/)
  * Node JS (https://nodejs.org/en/)
  * Github (https://github.com/)
  * Google Fonts (https://fonts.google.com/)
  * Balsamiq (https://balsamiq.com/)
  * Font Awesome (https://fontawesome.com/)
  * JQuery (https://jquery.com)
  * TinyPNG (https://tinypng.com/)
  * CSS Validation Service (https://jigsaw.w3.org/css-validator/)
  * HTML Markup Validation Service (https://validator.w3.org/)
  * Chrome dev tools (https://developers.google.com/web/tools/chrome-devtools)
  * Responsive Design (http://ami.responsivedesign.is/)
  * DbDesigner (https://app.dbdesigner.net/)
  * Unittest (https://docs.djangoproject.com/en/3.2/topics/testing/overview/)
  * JSHint (https://jshint.com/)
  * PEP8 (https://www.python.org/dev/peps/pep-0008/)
  * Jest (https://jestjs.io/)
### 4. Automated tests
* HTML\
Passing the HTML of all pages through the [W3C Markup Validator](https://validator.w3.org/) and errors are only related to special format of input calculated by Python logic and passed to html page via Django.
  * [Home Page Validation](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/w3validator-html-home.pdf)
  * [Why A Bag Page Validation](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/w3validator-html-whyabag.pdf)
  * [Pack A Bag Page Validation](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/w3validator-html-packmybag.pdf)
  * [Add Items Page Validation](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/w3validator-html-mybag_add_items.pdf)
  * [Bag Details Page Validation](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/w3validator-html-mybag_details.pdf)
  * [Profile Page Validation](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/w3validator-html-profile.pdf)
  * [Blog Page Validation](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/w3validator-html-blog.pdf)
  * [Login Page Validation](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/w3validator-html-login.pdf)
  * [Sign Up Page Validation](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/w3validator-html-signup.pdf)
* CSS\
Passing the global CSS file through the [W3C Jigsaw Validator](https://jigsaw.w3.org/css-validator/) and no errors have been found.\
Warnings are coming from dynamic CSS variables and imported style sheets which are out of scope of validator. Also warning appears concerning -webkit/-moz effects, as these elements are out of scope for validator.
  * [CSS Style Validation](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/w3validator-css-style.pdf)
* Javascript/jQuery\
Passing all Javascript code (static/js/js_packmybag.js) through the [JSHint](https://jshint.com/) with [these configurations](https://github.com/SofiaHorvath91/ucd-project-2/blob/main/img/readme/jshint-configuration.PNG) and no errors have been found, only 1 warning shown (for not initialized variable - the value of these variables passed via page script from django view).\
Passing all Javascript (static/js/js_packmybag.js) code through [Jest](https://jestjs.io/) tests (static/js/js_packmybag.test.js) and all tests passed, but one console error was shown as console cannot handle Javascript alert() function.
  * [JSHint Validation](https://github.com/SofiaHorvath91/ucd_project_4/blob/main/img/readme/jshint-result.PNG)
  * [Jest Test Validation](https://github.com/SofiaHorvath91/ucd_project_4/blob/main/img/readme/jest_testing_test_suite.PNG)
  * [Jest Test Console Error](https://github.com/SofiaHorvath91/ucd_project_4/blob/main/img/readme/jest_testing_console_error.PNG)
* Python Code\
Passing the python logic file (myappocalypse/views.py) through the [PEP8 Validator](http://pep8online.com/), errors only due to sometimes long lines (I found that after revision, further breaking would be distracting, and lines stayed in margot in Pycharm tool).\
Passing the python models through Django unit tests (myappocalypse/test.py) and all tests passed.
  * [PEP8 Validation - Pyhthon View - Text file](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/python_pep8_view.txt)
  * [PEP8 Validation - Python Models - Text file](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/python_pep8_model.txt)
  * [PEP8 Validation - Python Tests - Text file](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/python_pep8_test.txt)
  * [Django Unit Tests](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/jest_testing_test_suite.PNG)
### 5. Manual tests
* Desktop\
Mozilla Firefox, Google Chrome, Microsoft Edge: pages are working fine and have the corresponding style, social login works as expected.
* Mobile\
Tested with Samsung A5, Galaxy Fold, iPhone 5, and iPad, and webpage works well, responsive as intended and no style deformations.
* Mozilla Developer Tools\
Tested for available devices, webpage works well, responsive as intended, no style deformations and no error messages in Pycharm debug tool.
### 6. Accessibility tests
The pages available before login were verified about accessibility using [Wave](https://wave.webaim.org/) as Wave cannot handle login feature. Few stylistic errors found (low contrast errors for color), alerts related to heading elements hierarchy, one error for empty header (filled out by Django). As other pages are very similar in terms of HTML-Styling, same results are assumed for them too.
* [Home Page Wave Result](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/wave-home.PNG)
* [Why A Bag Page Wave Result](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/wave-whyabag.PNG)
* [Login Page Wave Result](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/wave-login.PNG)
* [Sign Up Page Wave Result](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/wave-signup.PNG)
### 7. Bugs and Solution
While building the application, I encountered the difficulty of passing information (Item model records from database) from Django view to Javascript code for display on UI. I found the solution in form of transforming the information to Json value in Django view, passing it to script on HTML page and retrieve it by main Javascript from page script. This slows the site a bit, but no timing-out and information is thus consistent through different technologies.
## Deployment
The site was deployed to Heroku (find it [here](https://vast-shore-97005.herokuapp.com/)) while building it with [PyCharm](https://www.jetbrains.com/pycharm/) and pushing it to GitHub Repository and Heroku via [Git Bash](https://git-scm.com/downloads).
1.	GitHub repository => Settings => GitHub Pages
2.	Source => Selecting Branch + Folder (main/docs)
3.	With branch/folder selected, the page refreshes to show deployment status
### 1. Forking Repository
By forking the GitHub Repository, the user can copy the original repository in his/her own GitHub account, allowing the user to view and/or make changes without affecting the original repository.
1.	Open GitHub => GitHub Repository
2.	Top of Repository => Fork option
3.	Copy of the original repository appears in your GitHub account
### 2. Local Clone
1.	Open GitHub => GitHub Repository
2.	Under Repository name => Clone or download option
3.	Clone Repository using HTTPS => Clone with HTTPS => Copy URL
4.	Open Git Bash
5.	Current working directory => Choose location where you want the directory to be cloned
6.	Type git clone, and then paste the URL copied in Step 3.\
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
7.	Press Enter
## Credits
### 1. Content
* The site is based on an original idea and beside verifying general details (like average weight for items based on different products), the words presented on site are my own.
### 2. Media
Pictures were treated with [Photoshop](http://www.apsportable.com/photoshop-cs6-portable-download-4/) and [tinyPNG](https://tinypng.com/) to have a better size for online presentation.
* Site Logo was made by me
* Background image : [VectorStock](https://www.vectorstock.com/royalty-free-vector/world-map-background-on-blue-vector-13276347)
### 3. External Codes used as source / inspiration
* Sticky Menu (Navigation Bar) : [W3Schools](https://www.w3schools.com/howto/howto_js_navbar_sticky.asp)
* Responsive Menu (Navigation Bar) : [Bootstrap](https://getbootstrap.com/docs/4.4/components/navbar/) (also used for general styling like margins, rows)
* Sticky Footer (Footer) : [CSS Tricks](https://css-tricks.com/couple-takes-sticky-footer/)
* Social Media Sharing Buttons (Footer) : [SharingButtons](https://sharingbuttons.io/)
* Pure CSS Collapsible Sections : [Mark Caron (CodePen)](https://codepen.io/markcaron/pen/RVvmaz)
* Pop-up Modal : [W3Schools](https://www.w3schools.com/howto/howto_css_modal_images.asp)
* Universal Amazon Link : [AskDaveTaylor](https://www.askdavetaylor.com/how_to_create_amazon_search_links/)
* Star-based Feedback : [LunarLogic (GitHub)](https://github.com/LunarLogic/starability)
### 4. Acknowledgements
* To the Code Institute for the great course material
* To the [Stack Overflow](https://stackoverflow.com/) & [W3Schools](https://www.w3schools.com/) as a valuable resource for solving issues.
* To [Udemy](https://www.udemy.com/) platform users for their wonderful tutorials
* To the people of Ukrania - I wish I could give everybody the biggest bag possible with all the best things on the world!
### 5. Special Thanks
* My mentor Rahul Lakhanpal for his time, kind words and support.
* My previous private mentor Samu Gábor Tamás who taught me all I knew before UCD
* My Mother who is always there for me and supports me through the hard times
