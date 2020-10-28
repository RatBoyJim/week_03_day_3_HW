from app import app

@app.route('/')
def index():
    return "Python is better than Ruby! (Probably)"

@app.route('/<name>')
def greet(name): 
    return f"Hello {name}!".upper()