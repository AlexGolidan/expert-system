from flask import Flask, request, render_template, redirect, url_for
from experta import *
import sys
import os

sys.path.append(os.path.dirname(__file__))
from pest_disease_expert_system import Diagnosis, Crop, Symptom

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        crop = request.form['crop']
        return redirect(url_for('questions', crop=crop))
    return render_template('index.html')

@app.route('/questions', methods=['GET', 'POST'])
def questions():
    crop = request.args.get('crop')
    engine = Diagnosis()
    
    if request.method == 'GET':
        questions = engine.generate_questions(crop)
        return render_template('questions.html', crop=crop, questions=questions, yes_answers=[])
    
    if request.method == 'POST':
        yes_answers = set()
        for key, value in request.form.items():
            if value == 'yes':
                yes_answers.add(key)
        
        engine.yes_answers = yes_answers
        engine.reset()
        engine.declare(Crop(crop=crop))
        for symptom in yes_answers:
            engine.declare(Symptom(symptom=symptom))
        engine.run()
        
        probabilities = engine.calculate_probabilities(crop, yes_answers)
        filtered_probabilities = {disease: prob for disease, prob in probabilities.items() if prob > 0}
        result = engine.result or "Диагноз не определён. Проверьте, соответствуют ли симптомы одному из правил."
        return render_template('result.html', result=result, crop=crop, symptoms=list(yes_answers), probabilities=filtered_probabilities)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)