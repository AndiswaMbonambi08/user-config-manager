# ⚙️ User Settings Manager
A lightweight Python module for managing user preferences such as theme, language, and notifications.  
This project demonstrates how to **add, update, delete, and view** settings stored in a dictionary.

## 📂 Features
- **Add new settings** → Insert a new key-value pair.  
- **Update existing settings** → Modify the value of an existing setting.  
- **Delete settings** → Remove a setting by its key.  
- **View settings** → Display all current settings in a user-friendly format.  

## 📜 Code Overview
```python
# Dictionary to store user settings
test_settings = {
    "theme": "light",
    "language": "english",
    "notifications": "enabled"
}

def add_setting(settings: dict, pair: tuple) -> str: ...
def update_setting(settings: dict, pair: tuple) -> str: ...
def delete_setting(settings: dict, key: str) -> str: ...
def view_settings(settings: dict) -> str: ...

## 🚀 Usage Examples

python
 View settings
print(view_settings(test_settings))

 Add a new setting
print(add_setting(test_settings, ("privacy", "high")))

 Update an existing setting
print(update_setting(test_settings, ("theme", "dark")))

 Delete a setting
print(delete_setting(test_settings, "notifications"))

View updated settings
print(view_settings(test_settings))

## ⚡ Key Notes

Keys and values are normalized to lowercase for consistency.

Duplicate keys are not allowed when adding new settings.

User-friendly messages are returned for each operation.

The view_settings function capitalizes keys for readability.

## 📖 Extensions
This module can be extended to:

Save/load settings from a JSON file for persistence.

Integrate with a GUI or CLI for interactive configuration.

Add validation rules (e.g., only allow certain values for theme).
