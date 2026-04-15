from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Welcome to this Flask course</h1>"

@app.route("/index")
def index():
    return render_template('index1.html')

@app.route('/about')
def about():
    return render_template('about.html')


# ✅ Single submit route (fixed)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science + maths + c + data_science) / 4

        if total_score >= 50:
            return redirect(url_for('successres', score=int(total_score)))
        else:
            return redirect(url_for('fail', score=int(total_score)))

    return render_template('form.html')


# ✅ PASS / FAIL handled here
@app.route('/successres/<int:score>')
def successres(score):
    res = "PASS" if score >= 50 else "FAIL"
    exp = {'score': score, 'res': res}
    return render_template('result1.html', results=exp)


# ✅ FAIL route
@app.route('/fail/<int:score>')
def fail(score):
    exp = {'score': score, 'res': 'FAIL'}
    return render_template('result1.html', results=exp)


# ✅ Jinja IF example
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result_if.html', score=score)


if __name__ == "__main__":
    app.run(debug=True)