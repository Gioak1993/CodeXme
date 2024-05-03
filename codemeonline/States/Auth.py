"""The authentication state."""
import reflex as rx
from sqlmodel import select
import bcrypt
from .Logged import User


def hash_password(password: str) -> str:
    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Convert the hashed password to a string for storage
    return hashed_password.decode('utf-8')

def verify_password(password: str, hashed_password: str) -> bool:
    # Check if the provided password matches the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

class AuthState(rx.State):
    """The authentication state for sign up and login page."""

    username: str
    email:str 
    password: str
    confirm_password: str
    user_id_cookie: str = rx.Cookie(path="/")

    def signup(self):
        """Sign up a user."""
        with rx.session() as session:
            if self.password != self.confirm_password:
                return rx.window_alert("Passwords do not match.")
            if session.exec(select(User).where(User.user_name == self.username)).first():
                return rx.window_alert("Username already exists.")
            if session.exec(select(User).where(User.email == self.email)).first():
                return rx.window_alert("Email its linked already with an account.")
            hashed_password = hash_password(self.password)
            self.user = User(user_name=self.username, password_hash=hashed_password, email=self.email.lower())
            session.add(self.user)
            session.expire_on_commit = False
            session.commit()
            return rx.redirect("/")

    def login(self):
        """Log in a user."""

        with rx.session() as session:
            user = session.exec(
                select(User).where(User.email == self.email.lower())
            ).first()
            if user:
                is_correct_password = verify_password(self.password, user.password_hash)
                if is_correct_password == True:
                    self.user = user
                    self.user_id_cookie = user.id
                    print(self.user_id_cookie)
                    return rx.redirect("/")
                else:
                    return rx.window_alert("Invalid username or password.")
            else:
                return rx.window_alert("Invalid username or password")
            
    def logout(self):
        """Log out a user."""
        if self.user_id_cookie == "2":
            print(self.user_id_cookie)
        self.user_id_cookie = ""
        print(self.user_id_cookie)
        return rx.redirect("/")

    def check_login(self):
        """Check if a user is logged in."""
        if not self.logged_in:
            return rx.redirect("/login")
    
    @rx.var
    def logged_in(self):
        """Check if a user is logged in."""
        return self.user_id_cookie != ""