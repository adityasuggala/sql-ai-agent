import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from schema_loader import load_schema
from query_generator import generate_sql
from query_runner import run_query

load_dotenv()
from flask import send_from_directory
app = Flask(__name__, static_folder="../static", static_url_path="/static")

@app.route("/api/query", methods=["POST"])
def query():
    data = request.json
    question = data.get("question")
    if not question:
        return jsonify({"error": "No question provided"}), 400
    sql = generate_sql(question)
    return jsonify({"sql": sql})

@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(debug=True)
