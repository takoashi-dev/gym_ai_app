from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

data = []
affinity = 0

comments = [
    "いい感じだね！",
    "その調子で続けよう",
    "確実に強くなってる",
    "ナイスワーク！",
    "成長してるね"
]

html = """
<h1>🏋️ 筋トレ育成ゲーム</h1>

<p>好感度: {{affinity}}</p>

<form method="POST">
  種目: <input name="exercise" required>
  回数: <input name="reps" required>
  <button type="submit">記録</button>
</form>

{% if message %}
<p><b>{{message}}</b></p>
{% endif %}

<h2>履歴</h2>
<ul>
{% for d in data %}
  <li>{{d['exercise']}} - {{d['reps']}}回</li>
{% endfor %}
</ul>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    global affinity
    message = None

    if request.method == "POST":
        exercise = request.form["exercise"]
        reps = request.form["reps"]

        data.append({"exercise": exercise, "reps": reps})
        affinity += int(reps) // 10 + 1

        message = random.choice(comments)

    return render_template_string(html, data=data, message=message, affinity=affinity)

if __name__ == "__main__":
    app.run(debug=True) 
