from flask import Flask, render_template
app = Flask(__name__)





@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/user/')
@app.route('/user/<username>')
def show_user_profile(username = None):
    # show the user profile for that user
    # return 'User {}'.format(username)
    return render_template("user.html", username=username)
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post {}'.format(post_id)



if __name__ == '__main__':
    app.run()
