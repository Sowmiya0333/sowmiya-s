from flask import Flask, render_template, request, redirect ,flash,url_for
import gspread
from google.oauth2.service_account import Credentials
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Google Sheets API setup
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)

# Open the Google Sheet (replace `YOUR_SHEET_ID` with the ID of your sheet)
sheet = client.open_by_key("1TE29cDRptxhP6GN7OhPHyoNoBnGTsbb1L0bFwvtLuHE")
worksheet = sheet.sheet1  # Select the first sheet in the Google Spreadsheet

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process form data
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        # Handle the data (e.g., store it, send an email, etc.)
        worksheet.append_row([name, email, subject, message])
        
        # Flash the success message
        flash("Thank you for contacting Me! Have a great dayyy", "success")
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
