import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import whatsapp_msg
from login_info import email, password, google_pass

class tinder_bot():
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=self.chrome_options)
        #self.driver = webdriver.Chrome()
        print("\n\n\nWebdriver created\n\n\n")

    def login(self):
        # Open Website
        self.driver.get('https://tinder.com/')

        print("\n\nOpened Website\n\n")

        #Wait for Website to fully load and popups to appear
        #sleep(5)
        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button'))
            )
            self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button').click()
            sleep(1)
            # Click on Login from Facebook on the popup
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()
        except Exception:
            try:
                # If Login from Facbook is not there then click on more options and then click on it
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/button'))
                        )
                self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/button').click()
                sleep(1)
                self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()
            except Exception:
                sleep(1)
                # Close Account Recovery popup
                self.login()
        print("\n\nSwitching to Facebook Page now\n\n")
        try:
            # switch to login popup
            base_window = self.driver.window_handles[0]
            sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[1])
            print("\n\nSwitched Succesfully to FB page\n\n")
            ## Facebook Login
            sleep(10)
            email_in = self.driver.find_element_by_name('email')
            email_in.send_keys(email)
            pass_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
            pass_in.send_keys(password)
            self.driver.find_element_by_xpath('//*[@id="u_0_0"]').click()
            print("\n\nSubmitted Email and passowrd to FB page\n\n")
        except Exception as e:
            print("\n\n\nFB Login page Failed!\nError:",e,"\n\n\n")

        try:
            self.driver.find_element_by_xpath('//*[@id="u_0_b"]')
            try:
                print("\n\nGoogle Sign-in required\n\n")
                self.fb_authentication()
                self.driver.switch_to.window(self.driver.window_handles[1])
                # Click ok after logging in from Google
                sleep(5)
                self.driver.find_element_by_xpath('//*[@id="pop_content"]/div[1]/div[3]/div[1]/label/input').click()
                sleep(5)
                self.driver.find_element_by_xpath('//*[@id="checkpointSubmitButton"]').click()
                self.driver.switch_to.window(base_window)
                sleep(6)
            except Exception as e:
                print("\n\n\nFacebook Authentication Failed!\nError:",e,"\n\n\n")
        except Exception:
            ## Switching back to main window
            self.driver.switch_to.window(base_window)
            print("\n\nNo Google Sign-in required!!\n\n")
            sleep(6)
        try:
            sleep(1)
            # Handle Ops something went wrong
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[1]/div')
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button').click()
            self.login()
        except Exception:
            # Close Prompts
            ## Location prompt
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
            print("\n\nWe are insideeeeeeeeee!!!!!\n\n")
            #WebDriverWait(self.driver, 10).until(self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]'))

        ## Notification prompt
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]').click()

        ## Privacy Policy Accpet
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()

        sleep(4)
        print("\n\n\n\nEVERYTHING IS DONE!!!!\n\n\n\n")

    def fb_authentication(self):
        try:
            # Click continue
            self.driver.find_element_by_xpath('//*[@id="checkpointSubmitButton"]').click()
            print("\n\n\nClicked submit for Google\n\n\n")
            # Select "Login with Google Account" and then continue
            sleep(5)
            print("\n\nTrying to slect Google log-in option\n\n")
            self.driver.find_element_by_xpath('//*[@id="u_3_9"]/div[2]/label[1]/span').click()
            self.driver.find_element_by_xpath('//*[@id="checkpointSubmitButton"]').click()
            print("\n\nSelected and moving forward!!\n\n")
            # Login to Google
            sleep(5)
            self.driver.find_element_by_xpath('//*[@id="u_5_0"]/div[2]/div[1]/div/div[2]/div/div/button').click()
            # Enter Google Email
            sleep(5)
            self.driver.switch_to.window(self.driver.window_handles[2])
            print("\n\n\nSwitched to Google login page\n\n\n")
            google_email_in = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
            google_email_in.send_keys(email)
            self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
            sleep(5)
            goog_password_in = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
            goog_password_in.send_keys(google_pass)
            self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()

            sleep(5)
        except Exception as e:
            print("\n\n\nGoogle Login Failed!\nError: ",e)




    def like(self):
        # Clicking on the right swipe button
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()
        
    def dislike(self):
        # Clicking on the left swipe button
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def add_home_screen_popup(self):
        # Close the "Add Tinder to your homescreen" popup
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]').click()

    def close_match(self):
        # If you get match then close that popup
        self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a').click()

    def go_global(self):
        # Go Global if you run out of profiles
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[2]/button').click()

    def auto_swipe(self):
        # Wait for the Tinder animation to complete
        sleep(4)
        like_counts = 0
        new_match = 0

        # Run infinitely
        while True:
            sleep(1)
            try:
                # Like the profile
                self.like()
                like_counts += 1
            except Exception:
                try:
                    # If Home screen popup arrives
                    sleep(1)
                    self.add_home_screen_popup()
                    sleep(2)
                except Exception:
                    try:
                        # If we get a match (Luck factor)
                        self.close_match()
                        new_match += 1
                    except Exception:
                        try:
                            # If we finished all the likes
                            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div')
                            print("\n\n\nFinished LIKES!!!\n\n\n")
                            self.driver.quit()
                            break
                        except:
                            try:
                                # Go Global
                                sleep(3)
                                self.go_global()
                                #continue
                            except Exception as e:
                                print(e)
                                break
        if like_counts == 1:
            like_counts -= like_counts
        return like_counts, new_match

# Run the bot and open Chrome
#bot = tinder_bot()

#while True:
    # Log via Facebook
    #bot.login()

    # Get profile's info
    #num_likes, num_matches = bot.auto_swipe()

    # Send Whatsapp msg
    #send_whatsapp_msg(num_likes, num_matches)

    #sleep(60*60*12)

# TESTING!!!!!!!!!!!!!!!!!

while True:
    bot = tinder_bot()
    bot.login()
    num_likes, num_matches = bot.auto_swipe()
    print(num_likes, num_matches)
    whatsapp_msg.send_whatsapp_msg(num_likes, num_matches)
    for i in range(2):
        print("\n\nSleeping for 6 Hours\n\n")
        sleep(60*60*6)