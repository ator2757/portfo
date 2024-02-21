import csv
from flask import Flask, render_template, send_from_directory,request,redirect

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

#this functions write to a text file (database.txt)
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject},{message}')

#this functions write to a csv file (database.csv)
def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'


# @app.route("/works.html")
# def works():
#     return render_template('works.html')
#
# @app.route("/about.html")
# def about():
#     return render_template('about.html')
#
# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')


