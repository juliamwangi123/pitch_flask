from app import app

@app.route('/')
@app.route('/pitch')
def index():
    return 'hi'