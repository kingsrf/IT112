from flask import Flask

app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    app_name = "Flask App"
    return f"Welcome to my {app_name}!"

# About page
@app.route('/about')
def about():
    author = "King Sambonge"
    about_info = "A B.A.S in Application Development student, aspiring to be a skilled and impactful engineer."
    return author + ", <br>" + about_info
   
# Contact page
@app.route('/contacts')
def contact():
    contact_info = "Contacts: linkedin.com/in/kingsambonge"
    return contact_info


if __name__ == '__main__':
    app.run(debug=True)
