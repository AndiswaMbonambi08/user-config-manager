# ⚙️ User Settings Manager

A lightweight Python module for managing user preferences such as theme, language, and notifications.
This project demonstrates how to add, update, delete, and view settings stored in a dictionary. I've transformed that FreeCodeCamp lab code into a stunning, feature-rich web application! 


## 📂 Features

Modern UI Design

Dark theme with cyan/blue gradient accents
Smooth animations and hover effects
Professional, clean layout
Responsive design (works on mobile)


Core Functionality (From Original freecode camp lab Code)

✅ Add settings
✅ Update settings
✅ Delete settings
✅ View all settings


Advanced Features

📊 Real-time Dashboard with live stats
📝 Change History Tracking (logs all modifications)
📥 Export Settings (download as JSON)
🏷️ Categories (organize settings by type)
💾 Database Persistence (SQLAlchemy + SQLite)
🎯 Tabbed Interface (Settings & History tabs)
🔄 Live Statistics (auto-updates every 5 seconds)

## 📜 Code Overview
python
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
# View settings
print(view_settings(test_settings))
#Output:
#Current User Settings:
#Theme: light
#Language: english
#Notifications: enabled

# Add a new setting
print(add_setting(test_settings, ("privacy", "high")))
#Output: Setting 'privacy' added with value 'high' successfully!

# Update an existing setting
print(update_setting(test_settings, ("theme", "dark")))
#Output: Setting 'theme' updated to 'dark' successfully!

# Delete a setting
print(delete_setting(test_settings, "notifications"))
#Output: Setting 'notifications' deleted successfully!

# View updated settings
print(view_settings(test_settings))


## ⚡ Key Notes

Keys and values are normalized to lowercase for consistency.

Duplicate keys are not allowed when adding new settings.

User-friendly messages are returned for each operation.

The view_settings function capitalizes keys for readability.


## Screenshots

<img width="1713" height="1398" alt="Screenshot_26-5-2026_31952_127 0 0 1" src="https://github.com/user-attachments/assets/1599c87e-46a7-4f7d-a5ad-9aeb12b26625" />

<img width="1713" height="1398" alt="Screenshot_26-5-2026_32016_127 0 0 1" src="https://github.com/user-attachments/assets/d4ef1679-bab8-424c-8b6e-e06c99d8310e" />

