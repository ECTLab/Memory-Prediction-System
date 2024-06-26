from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class VM(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(100), unique=True, nullable=False)
    x_value = db.Column(db.Float, nullable=False)

def init_db():
    db.create_all()

@app.before_request
def before_request():
    init_db()

@app.route('/')
def index():
    vms = VM.query.all()
    return render_template('index.html', vms=vms)

@app.route('/add_vm', methods=['POST'])
def add_vm():
    data = request.get_json()
    new_vm = VM(ip=data['ip'], x_value=data['x_value'])
    db.session.add(new_vm)
    db.session.commit()
    return jsonify({'message': 'VM added successfully'})

@app.route('/update_vm', methods=['POST'])
def update_vm():
    data = request.get_json()
    vm = VM.query.filter_by(ip=data['ip']).first()
    if vm:
        try:
            response = requests.post(
                f'http://{vm.ip}:9000/update-default-x',
                json={'value': data['x_value']},
                timeout=2
            )
            if response.status_code == 200:
                vm.x_value = data['x_value']
                db.session.commit()
                return jsonify({'message': 'VM updated successfully'}), 200
            else:
                return jsonify({'message': 'Failed to update VM'}), 500
        except requests.exceptions.RequestException:
            return jsonify({'message': 'VM does not respond'}), 500
    else:
        return jsonify({'message': 'VM not found'}), 404

@app.route('/delete_vm', methods=['POST'])
def delete_vm():
    data = request.get_json()
    vm = VM.query.filter_by(ip=data['ip']).first()
    if vm:
        db.session.delete(vm)
        db.session.commit()
        return jsonify({'message': 'VM deleted successfully'}), 200
    else:
        return jsonify({'message': 'VM not found'}), 404

@app.route('/update_multiple_vms', methods=['POST'])
def update_multiple_vms():
    data = request.get_json()
    ips = data['ips']
    x_value = data['x_value']
    messages = []
    for ip in ips:
        vm = VM.query.filter_by(ip=ip).first()
        if vm:
            try:
                response = requests.post(
                    f'http://{vm.ip}:9000/update-default-x',
                    json={'value': x_value},
                    timeout=2
                )
                if response.status_code == 200:
                    vm.x_value = x_value
                    db.session.commit()
                    messages.append({'ip': ip, 'message': 'VM updated successfully'})
                else:
                    messages.append({'ip': ip, 'message': 'Failed to update VM'})
            except requests.exceptions.RequestException:
                messages.append({'ip': ip, 'message': 'VM does not respond'})
        else:
            messages.append({'ip': ip, 'message': 'VM not found'})
    return jsonify(messages), 200

if __name__ == '__main__':
    app.run(debug=True)
