from flask import Flask, render_template, url_for, request, redirect # for serving html
import csv

app = Flask(__name__)

@app.route("/")
def home(): 
    return render_template('index.html')  # html file must be in the templates folder

@app.route("/<string:page_name>") #grab address from browser
def html_page(page_name):
    return render_template(page_name) 

# @app.route("/works.html")
# def works():
#     return render_template('works.html')  

# @app.route("/contact.html")
# def works():
#     return render_template('contact.html')

# def write_to_file(data): # to txt 
#     with open ('database.txt', mode='a') as db:
#         #data is in a dictinary format
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = db.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('data.csv', mode="a") as database:
       email = data['email']
       subject = data['subject']
       message = data['message'] 
       csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
       csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
   if request.method == 'POST':
       try:
            data = request.form.to_dict() 
            write_to_csv(data)
            return redirect('/thankyou.html')
       except:
           return 'did not save to DB'
   else:
       return 'smth went wrong!'


