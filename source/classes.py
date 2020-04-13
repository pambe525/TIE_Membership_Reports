from abc import ABC, abstractmethod
from selenium import webdriver

'''
Abstract Base Class for Selenium Web Scripting using Template Method pattern.
This class also has the Factory Methods to create concrete classes for explara and google suite
'''
class WebScript(ABC):

    @staticmethod
    def for_explara_export(username, password):
        return ExplaraWebScript(username, password)

    @staticmethod
    def for_google_upload(username, password):
        pass

    def run_script(self):
        self.login()
        self.logout()

    @abstractmethod
    def login(self):
        raise NotImplementedError

    @abstractmethod
    def load_page(self):
        raise NotImplementedError

    @abstractmethod
    def run(self):
        raise NotImplementedError

    @abstractmethod
    def get_result(self):
        raise NotImplementedError

    @abstractmethod
    def logout(self):
        raise NotImplementedError


''' 
Concrete class to access Explara hub and download membership data
'''
class ExplaraWebScript(WebScript):

    def __init__(self, username, password):
        self.login_url = "https://hub.tie.org/login"
        self.members_url = "https://hub.tie.org/cm/group/membership/active/gid/3293"
        self.username = username
        self.password = password
        self.webdriver = webdriver.Firefox()

    def login(self):
        self.webdriver.get(self.login_url)
        self.webdriver.find_element_by_id("usernameSignIn").send_keys(self.username)
        self.webdriver.find_element_by_id("passwordSignIn").send_keys(self.password)
        self.webdriver.find_element_by_id("loggedInUserPage").click()
        print("Logged in successfully")

    def load_page(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

    def get_result(self):
        raise NotImplementedError

    def logout(self):
        self.webdriver.find_element_by_class_name("dropdown-item logout").click()
        self.webdriver.quit()

