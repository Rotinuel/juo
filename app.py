from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'lagos, Nigeria',
    'salary': 'NGN 400,000'
    },
    {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'lagos, Nigeria',
    'salary': 'NGN 350,000'
    },
    {
    'id': 3,
    'title': 'Frontend Developer',
    'location': 'Remote',
    },
    {
    'id': 4,
    'title': 'Backend Developer',
    'location': 'Remote',
    'salary': 'NGN 200,000'
    },
]

@app.route("/")
def hello_imma():
    return render_template( 'home.html', 
                           jobs=JOBS,
                           company_name='Juo')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug= True)