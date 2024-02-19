from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Define route for economic impact section
@app.route('/economic')
def economic_impact():
    return render_template('economic_impact.html')

# Define route for social impact section
@app.route('/social')
def social_impact():
    return render_template('social_impact.html')

# Define route for environmental impact section
@app.route('/environmental')
def environmental_impact():
    return render_template('environmental_impact.html')


if __name__ == '__main__':
    app.run(debug=True)
