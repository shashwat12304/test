from flask import Flask, render_template,jsonify
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Here you can handle the file upload process
    # For simplicity, let's just return a success message
    return jsonify({'message': 'File uploaded successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
