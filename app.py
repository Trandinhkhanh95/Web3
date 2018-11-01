from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/new_bike", methods=['GET','POST'])
def new_bike():
    if request.method == 'GET':
        return render_template("new_bike.html")
    elif request.method == 'POST':
        form = request.form
        model = form['model']
        daily_fee = form['daily_fee']
        image = form['image']
        year = form['year']
        print('*'*50)
        print()
        print("Model :", model,"||","Daily fee :", daily_fee,"||","Image :", image,"||","Year :", year)
        print()
        print('*'*50)
        return render_template("repost.html")

if __name__ == '__main__':
  app.run(debug=True)
