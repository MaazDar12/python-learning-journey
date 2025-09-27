class BankAccount:
    def __init__(self, owner, balance=0, pin="1234"):
        self.owner = owner
        self.balance = balance
        self.pin = pin
        self.is_authenticated = False

    def authenticate(self, entered_pin):
        if entered_pin == self.pin:
            self.is_authenticated = True
            print("✅ Authentication successful! You can now access your account.")
        else:
            print("❌ Incorrect PIN! Access denied.")

    def deposit(self, amount):
        if self.is_authenticated:
            self.balance += amount
            print(f"{self.owner} deposited {amount} PKR. New balance: {self.balance} PKR.")
        else:
            print("⚠️ Please authenticate first!")

    def withdraw(self, amount):
        if self.is_authenticated:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{self.owner} withdrew {amount} PKR. Remaining balance: {self.balance} PKR.")
            else:
                print()