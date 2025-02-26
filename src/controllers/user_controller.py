from flask import Blueprint, jsonify, request

# Déclaration du Blueprint
user_bp = Blueprint("user", __name__)


@user_bp.route("/", methods=["GET"])
def get_users():
    return "COUCOU"
