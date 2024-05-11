from flask import Flask, render_template, request
import os
import emailjs

app = Flask(__name__)

# Initialize EmailJS
emailjs.init("RGfHRGMRqGPVIYC_W")  # Replace with your EmailJS user ID

# Ensure uploads folder exists
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# EmailJS configuration
FROM_EMAIL = 'shashwatsharma12304@gmail.com'
TO_EMAIL = 'shashwatsharma.dev@gmail.com'
EMAIL_SUBJECT = 'PDF Upload Notification'


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "No file part"
    file = request.files["file"]

    if file.filename == "":
        return "No selected file"
    
    if file:
        # Save the file to the uploads folder
        filename = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filename)

        # Send email using EmailJS
        send_email(filename)

        return "File uploaded successfully"


def send_email(filename):
    # Compose email message
    message = f"The PDF file {os.path.basename(filename)} has been uploaded successfully."

    # Send email using EmailJS
    emailjs.send('service_oclzt3i', 'template_2g15vgm', {
        "from_name": "Your Name",
        "to_name": "Uploader",
        "from_email": FROM_EMAIL,
        "to_email": TO_EMAIL,
        "message": message
    })


if __name__ == "__main__":
    app.run(debug=True)
