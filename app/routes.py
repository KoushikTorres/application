from flask import Blueprint, send_from_directory

bp = Blueprint('main', __name__)

@bp.route('/video/<path:filename>')
def stream_video(filename):
    return send_from_directory('static/videos', filename)
