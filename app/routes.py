from app import app
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    print(User)
    return "Hello, World!"