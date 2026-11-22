from flask import Blueprint, request, jsonify

bp = Blueprint('main', __name__)

@bp.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

@bp.route('/api/chat', methods=['POST'])
def chat():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    data = request.get_json()
    message = data.get('message')
    
    if message is None:
        return jsonify({"error": "Missing 'message' field"}), 400
    if not isinstance(message, str):
        return jsonify({"error": "Message must be a string"}), 400
    if len(message.strip()) == 0:
        return jsonify({"error": "Message cannot be empty"}), 400
    if len(message) > 500:
        return jsonify({"error": "Message too long (max 500 chars)"}), 400
    
    response_text = "You can start by tracking your income and expenses."
    return jsonify({"response": response_text})