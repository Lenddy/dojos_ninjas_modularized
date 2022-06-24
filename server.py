from flask_app.__init__ import app
from flask_app.controllers import dojo_controller,ninja_controller


#=============================
#=============================
#import your controllers
#==============================
#=============================

if __name__ == "__main__":
    app.run(debug=True)
