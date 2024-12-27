from flask import Flask, render_template, request
from dotenv import load_dotenv
from flask_mail import Mail, Message
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.yourmailserver.com'  # Use your SMTP server (e.g., smtp.gmail.com for Gmail)
app.config['MAIL_PORT'] = 587  # Port for TLS
app.config['MAIL_USE_TLS'] = True  # Use TLS encryption
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  # Your email username
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # Your email password
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')  # Default sender (use your email address)

# Initialize Flask-Mail
mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission
        pass
    return render_template('contact.html')

@app.route('/quote', methods=['GET', 'POST'])
def quote():
    if request.method == 'POST':
        # Extract form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        details = request.form['details']
        request_owner = 'request_owner' in request.form  # Checkbox logic

        # Process the data (e.g., save it, send an email, etc.)
        message = f"Thank you for your quote request, {name}. We will get back to you soon!"
        
        # Optionally, log the data or send an email
        print(f"Name: {name}, Email: {email}, Phone: {phone}, Job Details: {details}, Request Owner: {request_owner}")

        # Send an email notification (uncomment this part if you want to send emails)
        msg = Message('New Quote Request', recipients=[os.getenv('ADMIN_EMAIL')])
        msg.body = f"""
        New quote request received:

        Name: {name}
        Email: {email}
        Phone: {phone}
        Job Details: {details}
        Request Owner: {request_owner}
        """
        mail.send(msg)

        return render_template('quote.html', message=message)
    
    return render_template('quote.html')


@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

if __name__ == "__main__":
    app.run(debug=True)
