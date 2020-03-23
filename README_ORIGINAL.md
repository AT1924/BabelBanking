# Babel Fish Banking

Mainvest Take Home Interview

Time estimate: 1-3 hours

Mainvest would like to create a viral waitlist for its new moonshot product: Babel Fish Banking. It’s such an awesome FinTech product it is impossible to describe.

Please create a web application with the following features:

* People can sign up for the waitlist to get access to Babel Fish Banking
* Signing up for the waitlist gives you a Waitlist Rank and a unique referral link
* People signing up for the waitlist through your referral link will lower your Waitlist Rank. Your Waitlist Rank will be some combination of your original waitlist sign up date and how many people signed up with your referral link
* You can use any language, framework or tool you want.
* Please include a brief summary (1-3 sentences) of what you did and list any choices / assumptions you made
* Please include a link to your repository on Github when you are done. 
* Please ignore all CSS / styling. We don’t care how ugly it is.
*  Feel free to focus on whatever aspect of this project corresponds to your strongest skill set. If you’re more comfortable doing back end, just write the endpoints. If you’re more comfortable writing front end code, ignore the endpoints. If you want to do both, that’s fine too.


Configuring your repo:
Dependencies:
* python/python3,
* pip (https://pip.pypa.io/en/stable/installing/)
* virtualenv: `sudo pip install virtualenv`


* clone this repo
* `virtualenv env -p python3`
* `source env/bin/activate`
* `pip install -r requirements.txt`
* `cd waitlist`
* `python manage.py migrate`
* `python manage.py runserver`
* open up `http://localhost:8000`

Front end: For the purposes of this project, you can write all of your code in `waitlist/index.html`.

Back end: You can find the views in `waitlist/rest/views.py` and the urls is `waitlist/waitlist/urls.py`
