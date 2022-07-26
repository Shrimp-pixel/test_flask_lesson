from test_flask_lesson import create_app, db
from test_flask_lesson.models import User

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
