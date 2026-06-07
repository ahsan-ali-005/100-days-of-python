# Create PasswordValidator class

class PasswordValidator:

    def __init__(self, password):
        self.password = password

    def validate_pass(self):

        if len(self.password) < 8:
            print("❌ Password must be at least 8 characters long")
            return

        # 2. Conditions using flags
        has_lower = False
        has_upper = False
        has_digit = False
        has_special = False

        for char in self.password:
            if char.islower():
                has_lower = True
            if char.isupper():
                has_upper = True
            if char.isdigit():
                has_digit = True
            if not char.isalnum():
                has_special = True

        # 3. Final validation
        if has_lower and has_upper and has_digit and has_special:
            print("✅ Password is STRONG")
        else:
            print("❌ Password is WEAK")
            print("Password must contain:")
            if not has_lower:
                print("- At least one lowercase letter")
            if not has_upper:
                print("- At least one uppercase letter")
            if not has_digit:
                print("- At least one digit")
            if not has_special:
                print("- At least one special character")


p = input("Enter your password: ")
validator = PasswordValidator(p)
validator.validate_pass()