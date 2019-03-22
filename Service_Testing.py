import User, Screen_Builder

risk_profiles = ["Risky", "Moderate", "Defensive"]

investing_knowledge = ["low", "medium", "high"]

areas_of_interest = ["Technology", "REITs"]

def build_safe_user():

    safe_user = User.User()
    safe_user.setup_profile("Defensive", "low", "REITs")
    safe_user.build_screens()


def build_screen():

    test_screen = Screen_Builder.screen_builder("X", "Y", "Z")
    test_screen.build_screen()

build_safe_user()

build_screen()