# Tinder Bot which sends you WhatsApp messages


I made a Tinder Bot using selenium Python, which auto swipes, and then sends a report on your WhatsApp, and then again starts swiping after 12 hours (Tinder free account has 100 likes per day). All hosted on Heroku, so we can do our work!

**Platforms used:**
[Heroku](https://www.heroku.com/) (For hosting our app) and [Twilio](https://www.twilio.com/) (For sending WhatsApp messages)

## How to use it:

**Below are the requirements for this project:**

 1. Python 3.6 or above
 2. Heroku account
 3. Twilio account (Watch [this video](https://www.youtube.com/watch?v=pQeFxdT3FGY) to get started with Twilio WhatsApp sandbox)
 4. Selenium installed (Watch [this video](https://www.youtube.com/watch?v=dz59GsdvUF8) after installing selenium with `pip install selenium`) 
 5. Set up Heroku account for Selenium to run. (Watch [this video](https://www.youtube.com/watch?v=Ven-pqwk3ec))

**Below are the instructions on how can you use it:**

 1. Download or git clone this repository to your local machine.
 2. Open that directory in your cmd.
 3. Install all the dependencies with `pip install -r requirements.txt`
 4. Open file `login_info.py` and enter your email & password/s, and save it.
 5. Open `whatsapp_msg.py` and add your authentication codes and your number in it, and save it.
 6. Now git remote your Heroku app to this directory, and push it to Heroku.
 7. Now under the resources tab inside your Heroku app dashboard, you will find Clock under Free dynos. Click on edit, turn it on, and press confirm.

You can check all the errors it's throwing on Heroku by running `heroku logs -t` on your terminal to get logs in realtime.

If you want to run it locally, then comment all `chrome_options` lines & `self.driver = webdriver.Chrome(executable_path...` and uncomment `self.driver = webdriver.Chrome()`. You will be ready to go!

> **Note:** This repository is not yet complete. You can help me make it
> perfect by forking it, making changes to it and then making pull
> request

### Problem I'm Facing

While running on Heroku's server, Facebook detects unusual login from the USA, so it temporarily blocks me and forces me to create a new password.

It runs fine locally, but while running on Heroku, this problem occurs.
