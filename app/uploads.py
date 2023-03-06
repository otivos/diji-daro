from flask import Blueprint, redirect, render_template, request, url_for

bp = Blueprint('upload', __name__, url_prefix='/uploads')

@bp.route('upload-resource', methods=('GET', 'POST'))
def handleUploads():
    
    if request.method == 'POST':
        return redirect(url_for('handleUploads'))
    
    return render_template('uploads.html')