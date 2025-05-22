from flask import Blueprint, jsonify
from app import mongo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify({"message": "Welcome to the Flask API!"})