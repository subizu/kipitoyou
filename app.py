from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method =='POST':
        link = request.form['link']
        #print(link)
        if link =='':
            return render_template('index.html', message='Please enter a link')
        return render_template('success.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
