from curses import flash
import os
from flask import Blueprint, abort, current_app, redirect, render_template, request, url_for

bp = Blueprint('upload', __name__, url_prefix='/uploads')

@bp.route('upload-resource', methods=('GET', 'POST'))
def handleUploads():

    if request.method == 'POST':
        uploaded_resource = request.files['file']
        if uploaded_resource.filename != '':
            file_ext = os.path.splitext(uploaded_resource.filename)[1]
            if file_ext not in current_app.config['UPLOAD_EXTENSIONS']:
                abort(400)
            if os.path.getsize(uploaded_resource.filename) > current_app.config['MAX_CONTENT_LENGTH']:
                abort(413)
            uploaded_resource.save(os.path.join(current_app.config['UPLOADS_FOLDER'], uploaded_resource.filename))
        return redirect(url_for('upload.handleUploads'))
    
    return render_template('uploads.html')