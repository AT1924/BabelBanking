


For my implementation of the Babel Fish Banking system I utilized the Vue.js/Django structure already set up
up in the project. I pass information using axios get requests that are triggered on click of the submit button
at the homepage after submissions are checked for illegal characters. The database was modified to include the 
User schema which has the columns username, place, link. Username is the name that is submitted for the user 
when they sign up. Place is the rank of each person in line, and link is the reference number that if submitted
by another user allows the owner to increase their rank by one. Instead of having a particular link that users
visit to modify the database my application uses individual reference numbers that can be submitted at the same
time that a user submits their request to be added to the waitlist. I did this because I believe that it 
accomplished the same functionality in an easier and more understandable way. At creation of a user in the
database they are assigned a reference number that is used to modify their place in line.

CODE ADDITIONS:
I added the Vue signup method in index.html as well as modified the WaitlistView class in views.py. I also
added the SignUpView class in views that performs most of the backend logic. A url to rest/signup was added 
as well.

ERRORS:
    For some reason when starting up the server I receive warnings about unapplied migrations. The suggested fix
    does not seem to get rid of the problem and may make it worse, however it also does not seem to effect 
    functionality of the app.