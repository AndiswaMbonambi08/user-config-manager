from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_settings.db'
app.config['SECRET_KEY'] = 'settings-manager-secret-key'

db = SQLAlchemy(app)

class UserSetting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), unique=True, nullable=False)
    value = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(50), default='general')
    setting_type = db.Column(db.String(50), default='text')
    description = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class SettingsHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    setting_key = db.Column(db.String(100))
    old_value = db.Column(db.String(500))
    new_value = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

def add_setting(key: str, value: str, category: str = "general", setting_type: str = "text", description: str = "") -> dict:
    key = key.lower()
    if UserSetting.query.filter_by(key=key).first():
        return {"success": False, "message": f"Setting '{key}' already exists! Cannot add a new setting with this name."}
    new_setting = UserSetting(key=key, value=value.lower(), category=category, setting_type=setting_type, description=description)
    db.session.add(new_setting)
    db.session.commit()
    return {"success": True, "message": f"Setting '{key}' added with value '{value}' successfully!"}

def update_setting(key: str, value: str) -> dict:
    key = key.lower()
    setting = UserSetting.query.filter_by(key=key).first()
    if not setting:
        return {"success": False, "message": f"Setting '{key}' does not exist! Cannot update a non-existing setting."}
    history = SettingsHistory(setting_key=key, old_value=setting.value, new_value=value.lower())
    setting.value = value.lower()
    setting.updated_at = datetime.utcnow()
    db.session.add(history)
    db.session.commit()
    return {"success": True, "message": f"Setting '{key}' updated to '{value}' successfully!"}

def delete_setting(key: str) -> dict:
    key = key.lower()
    setting = UserSetting.query.filter_by(key=key).first()
    if not setting:
        return {"success": False, "message": "Setting not found!"}
    db.session.delete(setting)
    db.session.commit()
    return {"success": True, "message": f"Setting '{key}' deleted successfully!"}

def get_all_settings() -> list:
    settings = UserSetting.query.all()
    grouped = {}
    for setting in settings:
        if setting.category not in grouped:
            grouped[setting.category] = []
        grouped[setting.category].append({"id": setting.id, "key": setting.key, "value": setting.value, "type": setting.setting_type, "description": setting.description, "created_at": setting.created_at.isoformat(), "updated_at": setting.updated_at.isoformat()})
    return grouped

def get_settings_summary() -> str:
    settings = UserSetting.query.all()
    if not settings:
        return "No settings available."
    result = "Current User Settings:\n"
    for setting in settings:
        result += f"{setting.key.capitalize()}: {setting.value}\n"
    return result

def get_history(key: str = None, limit: int = 10) -> list:
    if key:
        history = SettingsHistory.query.filter_by(setting_key=key).order_by(SettingsHistory.timestamp.desc()).limit(limit).all()
    else:
        history = SettingsHistory.query.order_by(SettingsHistory.timestamp.desc()).limit(limit).all()
    return [{"setting_key": h.setting_key, "old_value": h.old_value, "new_value": h.new_value, "timestamp": h.timestamp.isoformat()} for h in history]

@app.route('/')
def index():
    return render_template('settings_dashboard.html')

@app.route('/api/settings', methods=['GET'])
def get_settings():
    return jsonify(get_all_settings())

@app.route('/api/settings/summary', methods=['GET'])
def get_summary():
    return jsonify({"summary": get_settings_summary()})

@app.route('/api/settings', methods=['POST'])
def create_setting():
    data = request.json
    result = add_setting(key=data.get('key'), value=data.get('value'), category=data.get('category', 'general'), setting_type=data.get('type', 'text'), description=data.get('description', ''))
    return jsonify(result), 201 if result['success'] else 400

@app.route('/api/settings/<key>', methods=['PUT'])
def update_setting_api(key):
    data = request.json
    result = update_setting(key, data.get('value'))
    return jsonify(result), 200 if result['success'] else 400

@app.route('/api/settings/<key>', methods=['DELETE'])
def delete_setting_api(key):
    result = delete_setting(key)
    return jsonify(result), 200 if result['success'] else 404

@app.route('/api/history', methods=['GET'])
def get_history_api():
    key = request.args.get('key')
    limit = request.args.get('limit', 20, type=int)
    history = get_history(key, limit)
    return jsonify({"history": history})

@app.route('/api/stats', methods=['GET'])
def get_stats():
    total_settings = UserSetting.query.count()
    categories = db.session.query(UserSetting.category).distinct().count()
    total_changes = SettingsHistory.query.count()
    return jsonify({"total_settings": total_settings, "total_categories": categories, "total_changes": total_changes})

@app.route('/api/export', methods=['GET'])
def export_settings():
    settings = UserSetting.query.all()
    export_data = {s.key: {"value": s.value, "category": s.category, "type": s.setting_type, "description": s.description} for s in settings}
    return jsonify(export_data)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5001)
