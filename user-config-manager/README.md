🛠️ User Settings Manager
A simple Python module to manage user settings such as theme, language, and notifications.
This project demonstrates how to add, update, delete, and view user configuration options using a dictionary.

📂 Features
Add new settings → Insert a new key-value pair into the settings dictionary.

Update existing settings → Modify the value of an existing setting.

Delete settings → Remove a setting by its key.

View settings → Display all current settings in a user-friendly format.

📜 Code Overview
python
# Dictionary to store user settings
test_settings = {
    "theme": "light",
    "language": "english",
    "notifications": "enabled"
}

def add_setting(settings: dict, pair: tuple) -> str:
    ...

def update_setting(settings: dict, pair: tuple) -> str:
    ...

def delete_setting(settings: dict, key: str) -> str:
    ...

def view_settings(settings: dict) -> str:
    ...
🚀 Usage Examples
python
# Initial settings
print(view_settings(test_settings))
# Output:
# Current User Settings:
# Theme: light
# Language: english
# Notifications: enabled

# Add a new setting
print(add_setting(test_settings, ("privacy", "high")))
# Output: Setting 'privacy' added with value 'high' successfully!

# Update an existing setting
print(update_setting(test_settings, ("theme", "dark")))
# Output: Setting 'theme' updated to 'dark' successfully!

# Delete a setting
print(delete_setting(test_settings, "notifications"))
# Output: Setting 'notifications' deleted successfully!

# View updated settings
print(view_settings(test_settings))
⚡ Key Notes
All keys and values are stored in lowercase for consistency.

Duplicate keys are not allowed when adding new settings.

User-friendly messages are returned for each operation.

The view_settings function capitalizes keys for readability.

📖 Learning Context
This project is inspired by exercises like User Configuration Manager from freeCodeCamp, focusing on practical Python dictionary manipulation and function design.
