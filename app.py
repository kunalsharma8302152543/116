# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Kunal Sharma" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():

    name = "Pramod Sharma" # write your name
    age = "43" # write your age

    return render_template('father.html' , name = name , age = age)

@app.route("/mother")
def mother():

    name = "Alka Sharma" # write your name
    age = "38" # write your age

    return render_template('mother.html' , name = name , age = age)

@app.route("/friend")
def friend():

    name = "Kundan" # write your name
    age = "15" # write your age

    return render_template('friend.html' , name = name , age = age)


# define the route to mother webpage


# define the route to friends webpage


# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
