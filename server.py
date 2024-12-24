from flask import Flask, render_template, request, redirect
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)

if __name__ == "__main__":
    app.run(port=5500, debug=True) 
    
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    # Dynamically render the correct template
    return render_template(f"{page_name}.html")

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')
        
def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
        
@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        return redirect("/thankyou")
    else:
        return 'you lost pilgram'


# @app.route("/submit_form", methods=['POST', 'GET'])
# def submit_form():
#    if request.method == 'POST':
#        data = request.form.to_dict()
#        print(data)
#        return'Form Submitted'
#    else:
#         return'Shits Fucked yo'
