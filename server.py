from flask import Flask, render_template, request, redirect
from friend import Friend

app = Flask(__name__)

@app.route("/")
def index():
    all_friends = Friend.get_all()
    return render_template("index.html", all_friends = all_friends)

@app.route('/friend/show/<int:friend_id>')
def show(friend_id):
    friend = Friend.get_one(friend_id)
    return render_template("show_friend.html", friend = friend)

@app.route("/create-friend", methods = ['POST'])
def create_friend():
    Friend.save(request.form)
    return redirect('/')

@app.route("/update-friend", methods = ['POST'])
def update_friend():
    Friend.update(request.form)
    return redirect('/')

@app.route("/delete-friend/<int:friend_id>")
def delete(friend_id):
    Friend.delete(friend_id)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True, port = 5001)