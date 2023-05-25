from .page import Page


class LoginPage(Page):
    def login(self, email, password):
        self.click_element("com.ajaxsystems:id/login")

        email_field = self.find_element("//android.widget.EditText[1]")
        email_field.send_keys(email)

        password_field = self.find_element("//android.widget.EditText[2]")
        password_field.send_keys(password)

        self.click_element("com.ajaxsystems:id/next")
        
