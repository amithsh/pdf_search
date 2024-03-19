from flask import request,jsonify, current_app as app
import os
import uuid
from .utils import process_pdf


@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    if 'pdf' not in  request.files:
        return jsonify({"error": "No file part"}), 400
    
    pdf_file = request.files['pdf']
    filename = str(uuid.uuid4())+ '.pdf'
    filepath = os.path.join(app.config['UPLOAD_FOLDER'],filename)



    try:
        pdf_file.save(filepath)
    except Exception as e:
        return jsonify({"error":str(e)}),500
    

    return jsonify({"message":"pdf uploaded successfully","filename":filename}),200

@app.route("/search-pdf/<filename>",methods=["POST"])
def search_pdf(filename):
    keyword = request.json.get('keyword','')

    if not keyword:
        return  jsonify({"error":"no keyword provided"}),400
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'],filename)
    if  not os.path.exists(filepath):
        return jsonify({"error":"File doesnot exists"}),404
        
    pages_found = process_pdf(filepath,keyword)
    

    return jsonify({'keyword':keyword,"pages_found":pages_found})