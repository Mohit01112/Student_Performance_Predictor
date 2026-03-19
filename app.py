from flask import Flask, request, render_template, jsonify
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
import pandas as pd
from ai_tutor import study_assistant

application = Flask(__name__)
app = application

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/api/tutor', methods=['POST'])
def tutor_api():
    try:
        data = request.get_json(silent=True) or {}
        message = (data.get('message') or '').strip()
        if not message:
            return jsonify({"error": "Message is required"}), 400

        answer = study_assistant(message)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('predict.html')

    if request.method == 'POST':
        try:
            # Get form data
            gender = request.form.get('gender')
            race_ethnicity = request.form.get('race_ethnicity')
            parental_education = request.form.get('parental_education')
            lunch = request.form.get('lunch')
            test_prep = request.form.get('test_prep')
            reading_score = int(request.form.get('reading_score'))
            writing_score = int(request.form.get('writing_score'))

            # Create CustomData object
            custom_data = CustomData(
                gender=gender,
                race_ethnicity=race_ethnicity,
                parental_level_of_education=parental_education,
                lunch=lunch,
                test_preparation_course=test_prep,
                reading_score=reading_score,
                writing_score=writing_score
            )

            # Get DataFrame
            pred_df = custom_data.get_data_as_data_frame()

            # Make prediction
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            predicted_score = round(results[0], 2)

            # Determine performance level
            if predicted_score >= 80:
                performance = "Excellent"
                emoji = "🌟"
                message = "The student is predicted to excel in mathematics!"
            elif predicted_score >= 60:
                performance = "Good"
                emoji = "👍"
                message = "The student is predicted to perform well in mathematics."
            elif predicted_score >= 40:
                performance = "Needs Support"
                emoji = "📚"
                message = "The student may need additional support in mathematics."
            else:
                performance = "Needs Significant Help"
                emoji = "⚠️"
                message = "The student is predicted to struggle with mathematics and may need significant help."

            return render_template('result.html',
                                 predicted_score=predicted_score,
                                 performance=performance,
                                 emoji=emoji,
                                 message=message,
                                 student_data={
                                     'gender': gender,
                                     'race_ethnicity': race_ethnicity,
                                     'parental_education': parental_education,
                                     'lunch': lunch,
                                     'test_prep': test_prep,
                                     'reading_score': reading_score,
                                     'writing_score': writing_score
                                 })

        except Exception as e:
            return render_template('error.html', error=str(e))

if __name__ == "__main__":
    print("\n" + "="*50)
    print("Starting Student Performance Predictor App...")
    print("Server will run on: http://127.0.0.1:5000")
    print("="*50 + "\n")
    app.run(host="0.0.0.0", port=5000, debug=True)