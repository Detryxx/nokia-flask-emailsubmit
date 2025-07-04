from flask import Flask, render_template, request, redirect

app = Flask(__name__)
contacts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        if name and email:
            contacts.append({'name': name, 'email': email})
        return redirect('/')
    return render_template('index.html', contacts=contacts)

if __name__ == '__main__':
    app.run(debug=True)
