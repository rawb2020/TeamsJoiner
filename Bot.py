from libs.lib import *

class Bot():
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--use-fake-ui-for-media-stream")
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def login(self):
        # Open https://teams.microsoft.com
        self.driver.get(ms_teams)
        sleep(10)

        # Username
        self.driver.find_element('xpath', email_text_box).send_keys(username)
        self.driver.find_element('xpath', next_button).click()
        sleep(10)

        # Password
        self.driver.find_element('xpath', password_text_box).send_keys(password)
        self.driver.find_element('xpath', next_button).click()
        sleep(10)
        
        # 2FA
        self.driver.find_element('xpath', dont_ask_7_days_checkbox).click()
        # Give 1 minute to accept 2FA
        sleep(60)

        # Stay Logged In
        self.driver.find_element('xpath', next_button).click()
        sleep(15)

    def join_meeting(self, link):
        # Open link
        self.driver.get(link)
        sleep(5)

        # Dirty hack to get rid of protocol handler prompt
        kb.press_and_release('escape')
        
        # Find the join in browser button (theres 2 different pages)
        try:
            join_in_browser_button = self.driver.find_element('xpath', join_in_browser_text)
        except NoSuchElementException:
            join_in_browser_button = self.driver.find_element('xpath', join_in_browser_img)
        
        # Click 'join in browser' button.
        join_in_browser_button.click()
        sleep(10)

    def turn_off_microphone(self):
        # Get the iframe ID
        frame = self.driver.find_element('xpath', experience_container_iframe)
        # Switch to the iframe
        self.driver.switch_to.frame(frame)
        sleep(5)

        # Turn off microphone
        self.driver.find_element('xpath', microphone_toggle_button).click()
        sleep(5)

    def click_join(self):
        # Click join meeting button
        self.driver.find_element('xpath', join_meeting_button).click()

    def stay_in_meeting(self):
        # Stay for 2 hours (duration of class)
        sleep(7200)

def main():
    bot = Bot()
    bot.login()
    
    # Add the variable name of the class u want to join here.
    # Class links can be defined in meetinglinks.py
    bot.join_meeting(class_1)
    bot.turn_off_microphone()
    bot.stay_in_meeting()

if __name__ == '__main__':
    main()