import csv

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def opeppers():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# def write_to_csv(data):
#     with open('database.csv', newline='\n', mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         csvfile = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         csvfile.writerow([email, subject, message])
#
#
# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     # return 'form submitted hurray.....'
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         write_to_csv(data)
#         return redirect('/thank_you.html')
#     else:
#         return 'something went wrong, try again!'
