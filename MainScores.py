import os
from flask import Flask

file_path = "/app/Scores.txt"

app = Flask(__name__)

@app.route('/')

def index():
    score = 0
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            score = int(file.read().strip())
            html = generate_html(score)
            return html

def generate_html(score):
    if score is not None:
        html = f"""<html>
<head>
<title>Scores Game</title>
</head>
<body>
<h1>The score is <div id="score">{score}</div></h1>
</body>
</html>"""
    else:
        html = """<html>
<head>
<title>Scores Game</title>
</head>
<body>
<h1><div id="score" style="color:red">ERROR</div></h1>
</body>
</html>"""

    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)