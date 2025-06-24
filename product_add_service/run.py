import sys
import os


sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from __init__ import create_app, db
import os

app = create_app()
port = int(os.getenv("PORT", 5000))

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)
