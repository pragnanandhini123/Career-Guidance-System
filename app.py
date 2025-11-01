from flask import Flask, render_template, request
import pickle
import mysql.connector

app = Flask(__name__)

# Load ML model
model = pickle.load(open('model/career_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    marks = float(request.form['marks'])
    skills = float(request.form['skills'])
    interest = float(request.form['interest'])

    prediction = model.predict([[marks, skills, interest]])[0]

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # leave empty if you don’t have password set
            database="career_db"
        )
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (marks, skills, interest, prediction) VALUES (%s,%s,%s,%s)",
            (marks, skills, interest, prediction)
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print("Database connection failed:", e)

    return render_template('result.html', result=prediction)

if __name__ == "__main__":
    app.run(debug=True)
