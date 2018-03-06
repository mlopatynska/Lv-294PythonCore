from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    #return "ESjlfsejlgfulasg"

@app.route('/hello')
def hello():
    return render_template("hello.html")

@app.route('/user/')
@app.route('/user/<username>')
def show_user_profile(username = None):
    return render_template("user.html", username = username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)




if __name__ == '__main__':
    app.run()
