from db import DB_Handler
from flask import Flask, request, jsonify

backend = Flask("message_board")
db = DB_Handler()


@backend.route("/create", methods=["POST"])
def create_message():
    try:
        message = request.form.get("message", default="")
        username = request.form.get("username", default="Anon")

        if not message:
            return jsonify({"success": False, "message": "Message is required"}), 400

        message_id = db.add_message(message, username)
        return jsonify({"success": True, "message_id": message_id}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@backend.route("/update", methods=["POST"])
def update_message():
    try:
        message = request.form.get("message", default="")
        message_id = request.form.get("message_id", default=0, type=int)

        if not message or not message_id:
            return jsonify({"success": False, "message": "Message and message ID are required"}), 400

        success = db.modify_message(message_id, message)
        return jsonify({"success": success}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@backend.route("/delete", methods=["POST"])
def delete_message():
    try:
        message_id = request.form.get("message_id", default=0, type=int)

        if not message_id:
            return jsonify({"success": False, "message": "Message ID is required"}), 400

        success = db.delete_message(message_id)
        return jsonify({"success": success}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
