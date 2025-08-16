from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Data storage - you can modify these to add/update content
PORTFOLIO_DATA = {
    "personal_info": {
        "name": "Stavya Joshi",
        "title": "Banana Leclerc",
        "email": "joshistavya@gmail.com",
        "phone": "+91 9968 23315",
        "location": "Mumbai, India",
        "bio": "Motivated Computer Science Engineering student with hands-on experience in web development, machine learning, data analytics, and cloud computing. Passionate about creating real-world tech solutions and collaborating in fast-paced, innovation-driven environments.",
        "github": "https://github.com/Stavya98",
        "linkedin": "https://linkedin.com/in/stavyajoshi",
        "resume_url": "/static/resume.pdf"
    },
    
    "skills": [
        "Python","Data Science","Linux","Machine Learning","PowerBi","Tableau","CLoud Computing", "Java", "Web Development", "Flask", "Django", "MongoDB", "MySQL", "Git", "AWS",
    ],
    
    "projects": [
        {
            "id": 1,
            "title": "Indian Sign Language System",
            "description": " Developed an ML-powered translator using MediaPipe and BiLSTM to bridge communication gaps between deaf and hearing communities",
            "tech_stack": ["Machine Learning", "Flask", "Tensorflow","OpenCV", "MediPipe", "React"],
            "github_url": "https://github.com/Stavya98/ISL-Translation",
            "image_url": "/static/images/project1.jpg",
            "featured": True
        },
        {
            "id": 2,
            "title": "Cluster-Based Discount App",
            "description": "Designed a coupon-based app for retailers to give discount coupons to their loyal customers according to their purchases in their clusters based on location. ",
            "tech_stack": ["React", "Node.js", "ExpressJs", "MongoDB"],
            "github_url": "https://github.com/Stavya98",
            "live_url": "https://taskmanager.herokuapp.com",
            "image_url": "/static/images/project2.jpg",
            "featured": True
        },
        {
            "id": 3,
            "title": "AI-Based Desktop Assistant ",
            "description": "Created a voice-activated productivity desktop assistant integrating Python and Gemini API. ",
            "tech_stack": ["Python", "Gemini API"],
            "github_url": "https://github.com/Stavya98",
            "live_url": "https://weather-dashboard.netlify.app",
            "image_url": "/static/images/project3.jpg",
            "featured": False
        },
        {
            "id": 4,
            "title": "WhatsApp Customer Support Chatbot",
            "description": " Built a 24/7 AI chatbot using IBM Watson Assistant for automated query handling.  ",
            "tech_stack": ["Cloud Computing", "IBM Watson"],
            "github_url": "https://github.com/Stavya98",
            "live_url": "https://weather-dashboard.netlify.app",
            "image_url": "/static/images/project3.jpg",
            "featured": False
        },
        {
            "id": 5,
            "title": "Stock Price Prediction System",
            "description": " Built a time series stocks forecasting model using LSTM, applying trend analysis and feature engineering giving an accuracy of 96%  ",
            "tech_stack": ["Python", "LSTM", "Pandas", "NumPy","Streamlit"],
            "github_url": "https://github.com/Stavya98/Stock-prediction",
            "live_url": "https://weather-dashboard.netlify.app",
            "image_url": "/static/images/project3.jpg",
            "featured": False
        },
        {
            "id": 6,
            "title": "Real-Time Traffic Analysis & Congestion Control System",
            "description": " Built a computer vision-based traffic management system using YOLOv8 to dynamically adjust traffic signal timing based on vehicle density at intersections, reducing congestion and optimizing traffic flow. ",
            "tech_stack": ["Python", "OpenCV", "YoloV8", "NumPy","Pandas"],
            "github_url": "https://github.com/Stavya98",
            "live_url": "https://weather-dashboard.netlify.app",
            "image_url": "/static/images/project3.jpg",
            "featured": False
        },
        {
            "id": 7,
            "title": "Customer Purchase Behavior Analysis Dashboard:",
            "description": " Developed a Power BI dashboard using Power Query and DAX for business sales insights for an Electronic Retail Store. ",
            "tech_stack": ["Powerbi", "DAX", "Power Query"],
            "github_url": "https://github.com/Stavya98",
            "live_url": "https://weather-dashboard.netlify.app",
            "image_url": "/static/images/project3.jpg",
            "featured": False
        },
        {
            "id": 8,
            "title": "Formula 1 Race Winner Prediction",
            "description": " Built a machine learning model to predict race winners using historical Formula data. Applied feature engineering and exploratory data to prepare datasets. Trained multiple classification algorithms including Random Forest, Support Vector Machine (SVM), and K-Nearest Neighbors (KNN), achieving 90+ accuracy in predicting race outcomes.  ",
            "tech_stack": ["Python", "KNN Algorithm", "Random Forest","Support Vector Machine", "Pandas", "NumPy"],
            "github_url": "https://github.com/Stavya98/F1-Race-Prediction",
            "live_url": "https://weather-dashboard.netlify.app",
            "image_url": "/static/images/project3.jpg",
            "featured": False
        },
         {
            "id": 9,
            "title": "MERN Stack Music Streaming app",
            "description": "Developed a full-stack music platform with playlist creation, admin only content management, React Frontend, Firebase authentication and AWS S3 for storage. ",
            "tech_stack": ["React Js", "Node.js", "ExpressJs", "MongoDB", "AWS S3"],
            "github_url": "https://github.com/Stavya98/Music-App-Mern",
            "live_url": "https://weather-dashboard.netlify.app",
            "image_url": "/static/images/project3.jpg",
            "featured": False
        }
    ],
    
    "experience": [
        {
            "title": "Forensics Analyst Intern",
            "company": "DeepCytes Lab UK",
            "duration": "Jul 2025 - Present",
            "description": "Working as a Forensics Analyst Intern, I am responsible for analyzing digital evidence, conducting forensic investigations, and assisting in the development of cybersecurity protocols. My role involves using advanced forensic tools to recover and analyze data from various digital devices, ensuring compliance with legal standards and best practices in cybersecurity."
        },
        
    ],
    
    "education": [
        {
            "degree": "Bachelor of Technology",
            "field": "Computer Science Engineering",
            "institution": "Shah & Anchor Kutchhi Engineering College",
            "duration": "2022 - 2026",
            "grade": "CGPA: 8.42/10"
        }
    ],
    
    "extracurriculars": [
        {
            "title": "Group Leader",
            "organization": "Shart India Hackathon",
            "duration": "2023",
            "description": "Led a team of 5 in a national hackathon, developed an innovative solution for real life problems"
        },
        {
            "title": "Team Leader",
            "organization": "Dev With AI Hackathon",
            "duration": "2024",
            "description": "Lead a team of 4 in a hackathon focused on AI solutions, successfully developed a prototype for the given problem statement"
        }
    ],
    
    "certificates": [
        {
            "name": "AWS Cloud Practitioner",
            "issuer": "Amazon Web Services",
            "date": "March 2024",
            "url": "https://aws.amazon.com/verification",
            "image_url": "/static/images/aws-cert.jpg"
        },
        {
            "name": "Google Analytics Certified",
            "issuer": "Google",
            "date": "February 2024",
            "url": "https://analytics.google.com/analytics/academy/",
            "image_url": "/static/images/google-cert.jpg"
        },
        {
            "name": "React Developer Certificate",
            "issuer": "Meta",
            "date": "January 2024",
            "url": "https://coursera.org/verify/certificate",
            "image_url": "/static/images/meta-cert.jpg"
        }
    ]
}

@app.route('/')
def home():
    return render_template('index.html', data=PORTFOLIO_DATA)

@app.route('/api/data')
def get_data():
    return jsonify(PORTFOLIO_DATA)

@app.route('/api/projects')
def get_projects():
    return jsonify(PORTFOLIO_DATA['projects'])

@app.route('/api/projects/<int:project_id>')
def get_project(project_id):
    project = next((p for p in PORTFOLIO_DATA['projects'] if p['id'] == project_id), None)
    if project:
        return jsonify(project)
    return jsonify({'error': 'Project not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)