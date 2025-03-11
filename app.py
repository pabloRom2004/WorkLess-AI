from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# Configure API keys
# openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analyze_project', methods=['POST'])
def analyze_project():
    data = request.json
    project_description = data.get('description', '')
    
    # Call AI service to analyze the project
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a task planning assistant."},
            {"role": "user", "content": f"Break down this project into manageable tasks: {project_description}"}
        ]
    )
    
    # Process the response
    tasks = response.choices[0].message.content
    
    return jsonify({"tasks": tasks})

if __name__ == '__main__':
    app.run(debug=True)