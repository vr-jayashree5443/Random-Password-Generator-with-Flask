from flask import Flask, render_template, request
import string
import secrets

app = Flask(__name__)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    secure_password = ''.join(secrets.choice(characters) for i in range(length))
    return secure_password

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            length = int(request.form['length'])
            if length <= 0:
                raise ValueError
        except (KeyError, ValueError):
            error_message = "Please enter a valid positive integer."
            return render_template('index.html', error_message=error_message)

        password = generate_password(length)
        return render_template('index.html', password=password)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
