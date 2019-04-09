import User, Screen_Builder, Screen

risk_profiles = ["Risky", "Moderate", "Defensive"]

investing_knowledge = ["low", "medium", "high"]

areas_of_interest = ["Technology", "REITs"]

def build_safe_user():

    safe_user = User.User()
    safe_user.setup_profile("Defensive", "low", "REITs")


def build_screen_url():

    # builds a url using Screen_Builder.py and screen_builder
    print("Service_Testing.py build_screen")
    test_screen = Screen_Builder.screen_builder("X", "Y", "Risky")
    test_screen.build_screen()
    print("Screen")
    print(test_screen.screen_url)

def setup_screen():

    screen = Screen()