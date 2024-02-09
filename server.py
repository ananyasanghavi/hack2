from flask import Flask, Response
from detection import start_detection

app = Flask(__name__)

@app.route('/start_detection')
def start_detection_route():
    start_detection()
    return Response(status=200)

if __name__ == '__main__':
    app.run()

# # backend/app.py
# from flask import Flask, jsonify
# from flask_cors import CORS
# from detection import start_detection, stop_detection

# app = Flask(__name__)
# CORS(app)  # Enable CORS for your frontend

# @app.route('/start_detection', methods=['POST'])
# def start():
#     start_detection()
#     return jsonify({'message': 'Detection started'}), 200

# @app.route('/stop_detection', methods=['POST'])
# def stop():
#     stop_detection()
#     return jsonify({'message': 'Detection stopped'}), 200

# if __name__ == '__main__':
#     app.run(debug=True)
