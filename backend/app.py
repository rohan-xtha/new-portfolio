from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Enable CORS for all routes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    details_link = db.Column(db.String(200))
    live_demo_link = db.Column(db.String(200))
    github_link = db.Column(db.String(200))
    image_url = db.Column(db.String(200), default='https://via.placeholder.com/355x200?text=Project+Image')

    def __repr__(self):
        return f'<Project {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'details_link': self.details_link,
            'live_demo_link': self.live_demo_link,
            'github_link': self.github_link,
            'image_url': self.image_url
        }

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<ContactMessage {self.name} - {self.email}>'

@app.route('/')
def hello_world():
    return 'Hello, Flask Backend!'

@app.route('/projects')
def get_projects():
    projects = Project.query.all()
    return jsonify([project.to_dict() for project in projects])

@app.route('/contact', methods=['POST'])
def submit_contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not name or not email or not message:
        return jsonify({'error': 'All fields are required.'}), 400

    new_message = ContactMessage(name=name, email=email, message=message)
    db.session.add(new_message)
    db.session.commit()

    return jsonify({'message': 'Message received successfully!'}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not Project.query.first(): # Add initial data only if table is empty
            project1 = Project(title='2025 Recap', description='Interactive website with GSAP animations and video effects.', details_link='2025-recap-project.html', live_demo_link='https://rohan-xtha.github.io/new-year/', github_link='https://rohan-xtha.github.io/new-year')
            project2 = Project(title='Portfolio Website', description='My personal portfolio showcasing my projects and skills.', details_link='#', live_demo_link='https://rohan-xtha.github.io/portfolio/', github_link='https://github.com/rohan-xtha/portfolio')
            project3 = Project(title='StoryVerse', description='An epic adventure set in a mystical land.', details_link='storyverse-project.html', live_demo_link='https://rohan-xtha.github.io/story/', github_link='https://github.com/rohan-xtha/story')
            db.session.add_all([project1, project2, project3])
            db.session.commit()
    app.run(debug=True)