class MobileLoginPage:

    USERNAME = "username"
    PASSWORD = "password"
    LOGIN_BUTTON = "login"

    def __init__(self, driver):

        self.driver = driver

    def enter_username(
        self,
        username
    ):

        self.driver.find_element(
            "accessibility id",
            self.USERNAME
        ).send_keys(username)

    def enter_password(
        self,
        password
    ):

        self.driver.find_element(
            "accessibility id",
            self.PASSWORD
        ).send_keys(password)

    def login(self):

        self.driver.find_element(
            "accessibility id",
            self.LOGIN_BUTTON
        ).click()