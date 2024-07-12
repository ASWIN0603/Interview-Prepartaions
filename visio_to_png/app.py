from flask import Flask, request, jsonify, send_file
import aspose.diagram
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) 

@app.route('/convert-visio', methods=['POST'])
def convert_visio():
    file = request.files['file']
    # Get the directory of the current script
    base_dir = os.path.dirname(__file__)

    # Save the uploaded file to the same directory as app.py
    file_path = os.path.join(base_dir, file.filename)
    file.save(file_path)

    # Convert Visio to PNG
    diagram = aspose.diagram.Diagram(file_path)
    output_path = os.path.join(base_dir, 'sample' + '.png')
    
    # Save the first page of the Visio file as a PNG
    diagram.save(output_path, aspose.diagram.SaveFileFormat.PNG)
    
    os.remove(file_path)    

    # Return the URL of the PNG file
    return send_file(output_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)  
