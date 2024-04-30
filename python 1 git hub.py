class BloodHarmonySystem:
    def __init__(self):
        self.user_database = {}
        self.appointment_schedule = {}
        self.blood_tracking_system = {}

    def user_registration(self, username, password, personal_details):
        # Validation
        if not self.is_valid_input(username, password):
            return "Invalid input. Please provide a strong password."

        # Check uniqueness of username
        if self.is_username_unique(username):
            # Create a new user profile
            user_profile = {"username": username, "password": password, "personal_details": personal_details}
            # Store user profile in the database
            self.user_database[username] = user_profile
            return "Registration successful. Welcome to Blood Harmony!"
        else:
            return "Username already exists. Please choose a different username."

    def schedule_appointment(self, username, date, time):
        # Check if the user is registered
        if username in self.user_database:
            # Check appointment availability
            if self.is_appointment_available(date, time):
                # Create a new appointment
                appointment = {"user": username, "date": date, "time": time}
                # Store appointment details
                self.appointment_schedule[(date, time)] = appointment
                return "Appointment scheduled successfully."
            else:
                return "Appointment slot not available. Please choose another date or time."
        else:
            return "User not registered. Please register before scheduling an appointment."

    def track_blood_unit(self, blood_unit_id):
        # Check if the blood unit ID is valid
        if blood_unit_id in self.blood_tracking_system:
            # Retrieve tracking information
            tracking_info = self.blood_tracking_system[blood_unit_id]
            return f"Blood unit {blood_unit_id} is currently {tracking_info}."
        else:
            return "Invalid blood unit ID. Please provide a valid ID for tracking."

    def is_valid_input(self, username, password):
        # Placeholder for input validation (e.g., password strength)
        return len(password) >= 8

    def is_username_unique(self, username):
        # Check if the username is unique
        return username not in self.user_database

    def is_appointment_available(self, date, time):
        # Placeholder for appointment availability check
        return (date, time) not in self.appointment_schedule


# Example Usage
blood_harmony = BloodHarmonySystem()

# User Registration
print(blood_harmony.user_registration("john_doe", "secure_password", {"name": "John Doe", "blood_type": "O+"}))

# Schedule Appointment
print(blood_harmony.schedule_appointment("john_doe", "2024-01-10", "15:30"))

# Track Blood Unit
print(blood_harmony.track_blood_unit(123456))
