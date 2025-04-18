from flask import Flask, request, url_for

app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    app_name = "Flask App"
    return f"""
            <head>
                <link rel="stylesheet" href="{url_for('static', filename='style.css')}">
            </head>
            <h1>Welcome to my {app_name}!</h1>
            <br><br><nav>
                <a href='/about' class="button-link">About</a>
                <a href='/contacts' class="button-link">Contacts</a>
                <a href='/fortune' class="button-link">Fortune Teller Game</a>
            </nav>
            """

# About page
@app.route('/about')
def about():
    author = "King Sambonge"
    about_info = "A B.A.S in Application Development student, aspiring to be a skilled and impactful engineer."
    home_link = "<a href='/' style='text-decoration: none;'>&#x1F3E0; Home</a>"
    return f"""
        <head>
            <link rel="stylesheet" href="{url_for('static', filename='style.css')}">
        </head>
        <h1>{author}</h1>
        <em>{about_info}</em>
        <br><br>
        {home_link}
        """

# Contact page
@app.route('/contacts')
def contact():
    linkedIn = "<a class='button-link' href='https://linkedin.com/in/kingsambonge' target='_blank'>LinkedIn</a>"
    github = "<a class='button-link' href='https://github.com/kingsrf' target='_blank'>GitHub</a>"
    home_link = "<a href='/' style='text-decoration: none;'>&#x1F3E0; Home</a>"
    return f"""
            <head>
                <link rel="stylesheet" href="{url_for('static', filename='style.css')}">
            </head>
            <h1>Contacts</h1>
            {linkedIn}
            {github}
            <br><br>
            {home_link}
            """

# Fortune page
@app.route('/fortune', methods=['GET', 'POST'])
def fortune():
    home_link = "<a href='/' style='text-decoration: none;'>&#x1F3E0; Home</a>"
    if request.method == 'POST':
        user = request.form.get('user')
        color = request.form.get('color')
        number = request.form.get('number')
    
        
        fortunes = {
            'red': "You will have a great day!",
            'yellow': "Happiness and good news are on the way!",
            'blue': "Stay calm, a solution to a problem will appear!",
            'green': "Growth and success are in your future!",
            'purple': "A surprise is waiting for you!",
            'orange': "Adventure is on the horizon!",
            'pink': "Love is in the air!",
        }
        lucky_msg = fortunes.get(color, "No fortune available for this color.")
       
        return f"""
            <head>
                <link rel="stylesheet" href="{url_for('static', filename='style.css')}">
            </head>
          
            <h1>Hi {user.title()}!</h1>
            <p>Your lucky number is {number}: <em>{lucky_msg}</em></p>
            <br>
            <a href='/fortune' class="button-link">&#x1F3B2; Play Again</a>
            <br><br>
            {home_link}
        """

    return f""" 
                <head>
                    <link rel="stylesheet" href="{url_for('static', filename='style.css')}">
                </head>
                <form method="POST" action="/fortune">
                    <label for="user">Enter your name:</label>
                    <input type="text" name="user" required><br>

                    <label for="color">Choose a color:</label>
                    <select name="color" required>
                        <option value="red">Red</option>
                        <option value="yellow">Yellow</option>
                        <option value="blue">Blue</option>
                        <option value="green">Green</option>
                        <option value="purple">Purple</option>
                    </select><br>
                    
                    <label for="number">Enter a lucky number:</label>
                    <select name="number" required>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                    </select><br>
                    
                    <button type="submit" class="button-link">Submit</button>
                    <br><br>
                    {home_link}
                </form> 
            """


if __name__ == '__main__':
    app.run(debug=True)
