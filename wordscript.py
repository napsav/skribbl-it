from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template("home.html")
@app.route("/result", methods=['POST', 'GET'])
def result():
	if request.method == 'POST':
		inputValue = request.form['hint']
		l = len(inputValue)
		f = open("lista.txt", encoding="utf8")
		parole = [line.rstrip("\n") for line in f]
		x = 0
		value = []
		stessaLunghezza = []
		final = []
		for char in inputValue:
			if char.isalpha():
				value.append(x)
			x += 1
		x = 0
		for candidato in parole:
			if len(candidato) == l:
				stessaLunghezza.append(candidato)
		for word in stessaLunghezza:
			for n in value:
				if word[n] == inputValue[n]:
					x += 1
				if x == len(value):
					final.append(word)
			x = 0
		return '<br>'.join(final)

