from flask import Flask ,render_template,request,session,url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('layout.htm')

@app.route('/dashboard')
def home():
    return  render_template('dashboard.htm')


@app.route('/signup')
def signup():
    return  render_template('signup.htm')

@app.route('/recipes.htm')
def recipes():
    return  render_template('recipes.htm')


@app.route('/login')
def login():
    return  render_template('login.htm')





if __name__ == '__main__':
    app.run(debug=True)