from app import db, create_app
from app.main.models import Users, Discussions, Comments, Follows, Likes
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
