from flask import Flask

app = Flask(__name__)

@app.route('/home')
def func_1():
    return "Jan"

# comment
if __name__ == "__main__":
    app.run(debug=True)

