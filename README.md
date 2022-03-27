# MyAPPocalypse (UCD Project 4)
Ready to hit the road when your world ends ?

Hopefully the time will never come when all you know is gone and suddenly you find yourself on the road in this big world, but it is never a bad idea to be prepared!
MyAPPocalypse helps you put together your bag for any possible scenario - no matter if you are on the Antarctis or in the Sahara, be assured you have a bag to grab when it is time to leave behind your place.
Here you may define the parameters of your bag (local conditions or special company like child or pet) and then select from the recommended items to fill it. If you are on the roll, you may also directly consult the latest offers of Amazon while cherry-picking from the proposed items, and if you find that something is missing from the list, you can recommend it and once approved, it will be available for selection.
Sign up (even with your social media accounts) and look around, prepare your bag and leave your thoughts for further improvements to raise the odds against vis-major events!

![Responsive Layouts](/static/img/readme/responsive-design.PNG)

Deployed app on [Heroku](https://heroku.com) : https://vast-shore-97005.herokuapp.com / \
Technologies : Python + Django + HTML + CSS \
Software : [PyCharm](https://www.jetbrains.com/pycharm/)

## UX
### 1. User stories
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
### 2. Strategy
* Purpose of Project
  * To make sure users have the chance to virtually prepare for a heavy real-life scenario
  * To have users to pack one or more bags with chosen items, depending on user-defined special conditions
  * To allow users leave their toughts and recommendations for further site improvement.
  * To give users an overview and educate them about what is needed in vis-major situations.
### 3. Scope
* I wanted a simple, evident and user-friendly UX experience.
* I wanted clear and informative content.
* I wanted a visually appealing, yet solid design.
* I wanted interesting and thought-provoking site description.
* I wanted smooth and interactive bag-packing and feedback experience.
### 4. Structure
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
### 5. Skeleton
The very basic skeleton of the site was modelled by Wireframes via Balsamiq, and during site development, additional design elements was added for better UX.
* [Home Page Wireframe](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/balsamiq-home.png)
* [Why A Bag Page Wireframe](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/balsamiq-whyabag.png)
* [Pack A Bag Page Wireframe](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/balsamiq-packmybag.png)
* [Add Items Page Wireframe](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/balsamiq-mybag_add_items.png)
* [Bag Details Bag Page Wireframe](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/balsamiq-mybag_details.png)
* [Blog Page Wireframe](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/balsamiq-blog.png)
* [Profile Page Wireframe](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/balsamiq-profile.png)
* [Sign Up / Login Page Wireframe](https://github.com/SofiaHorvath91/ucd_project_4/blob/master/static/img/readme/balsamiq-login_signup.png)
### 6. Style
* Design & Colours
  * When planning the project, I wanted a very simple design, not too grim but neither too playful, so I decided to rely on a visually appealing, reddish background image with matching theme, and white text with black border to ease the effect of the heavy subject. I wanted to avoid too much black or too dark theme as I wanted to emphasize the hope and the chance you give to yourself, not the sad conditions what give the context.
* Font Selection
  * The main font type was chosen with [Google Fonts](https://fonts.google.com/) and is used across the whole of the website: [Cagliostro](https://fonts.google.com/specimen/Cagliostro?query=Cagliostro). This is a well readable font type which yet gives a practical, yet personal feeling feeling which I found suitable for the subject of the site : the topic itself is pragmatic, but the circonstances are very personal.
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

* __Home Page__
  * Presenting MyAPPocalypse, the home page clearly and briefly indicates site objective and also offers entry point to available sites based on  on user's authentication status which allow users to immediately dive into the app. Unregistered or logged out users can know more about the site and/or sign up, logged in users can consult their profile, navigate to the blog or create a new bag.

Home Page - Logged Out\
![Home Page](/static/img/readme/page-home-loggout.png)
Home Page - Logged In\
![Home Page](/static/img/readme/page-home-loggin.png)

* __Login / Sign Up Page__
  * These pages allow user to sign up or to login via standard verification form, or via social media account (Facebook, Twitter, Google).

Login Page\
![Login Page](/static/img/readme/page-login.png)
Sign Up Page\
![Sign Up Page](/static/img/readme/page-signup.png)

* __Why A Bag page__
  * This page has the aim of explaining better the site objective, giving a context to the bag packing function, and informing users about the possible advantages of using the app.

Why A Bag Page\
![Why A Bag Page](/static/img/readme/page-whyabag.png)

* __Pack A Bag Page__
  * This page allows the users to profit from the main functionality of the site : they can create a bag based on different parameters in which they can then add items with respect to the max weight of bag (calculated upon user weight).

Pack A Bag Page\
![Pack A Bag Page](/static/img/readme/page-packmybag.png)

* __Add Items Page__
  * This page allows user to add items to the newly created or to an existing bag, depending if navigation from Pack My Bag page or Profile/Bag Details pages' edit function. Current weight of bag is dynamically calculated upon adding/removing items to/from bag, and user is alerted is bag's max weight is reached and no more items can be added. While adding items, user may consult the details of the item in a pop-up modal by clicking on the information sign next to it's name. The modal also provides click link to Amazon buying options.
If navigating via Edit Items link , the items already in the bag are preselected and bag's actual weight is displayed for further calculation upon modifying items. Once items are added, changes to be saved to add items to bag.

Add Items Page\
![Add Items Page](/static/img/readme/page-mybag_add_items.png)

Add Items Page - Pop-Up Modal with Item Details\
![Add Items Page - Pop-Up Modal with Item Details](/static/img/readme/page-mybag_modal_item.png)

* __Bag Details Page__
  * This page allows user to consult the parameters and items of an existing bag the user owns.  While checking the bag, user may consult the details of the added items in a pop-up modal by clicking on the information sign next to it's name (as on Add Item page's modal). The modal also provides click link to Amazon buying options. The page also gives quick link to modify items or delete bag as well as to new bag creator page.

Bag Details Page\
![Bag Details Page](/static/img/readme/page-mybag_details.png)

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

Profile Page - My Feedbacks\
![Profile Page - My Feedbacks](/static/img/readme/page-profile5.png)

* __Blog Page__
  * This page allows user to give star-based rating and/or written feedback about the site to share points of improvement and overall satisfaction. User also have the possibility here to recommend and item what the user is missing from the list of existing items. Newly created recommendation appears under My Recommendations section of Profile page. 
User can also check all exisiting feedbacks, and for own feedbacks in the list, a quick link is provided for removal in case the user wishes to delete it.

Blog Page - Leave Your Feedback\
![Blog Page - Leave Your Feedback](/static/img/readme/page-blog1.png)

Blog Page - Recommend an Item\
![Blog Page - Recommend an Item](/static/img/readme/page-blog2.png)

Blog Page - Check All Feedbacks\
![Blog Page - Check All Feedbacks](/static/img/readme/page-blog3.png)

* __Footer__
  * The footer section includes copyrights and it also allows to share this website with other people through social media sites and email via social share buttons. 

Footer\
![Footer](/static/img/readme/page-footer.png)
