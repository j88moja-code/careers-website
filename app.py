from flask import Flask, render_template, url_for, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Durban, South Africa',
        'salary': 'R 500, 000'
    },
    {
        'id': 2,
        'title': 'Software Engineer',
        'location': 'Cape Town, South Africa', 
    },
    {
        'id': 3,
        'title': 'Backend Engineer',
        'location': 'Alberton, South Africa',
        'salary': 'R 900, 000'
    },
    {
        'id': 4,
        'title': 'Frontend Developer',
        'location': 'Remote',
        'salary': 'R 600, 000'
    },

]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='Jobe')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)