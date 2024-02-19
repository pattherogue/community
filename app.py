from flask import Flask, render_template
import data_collection
import data_analysis
import data_visualization

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for data collection
@app.route('/collect-data')
def collect_data():
    file_path = "data/CRE2022.CRE-Data.csv"
    df = data_collection.load_data(file_path)
    return 'Data collected successfully'

# Route for data analysis
@app.route('/analyze-data')
def analyze_data():
    df = data_collection.load_data("data/CRE2022.CRE-Data.csv")
    data_analysis.analyze_data(df)
    return 'Data analyzed successfully'

# Route for data visualization
@app.route('/visualize-data')
def visualize_data():
    df = data_collection.load_data("data/CRE2022.CRE-Data.csv")
    data_visualization.visualize_data(df)
    return 'Data visualized successfully'

if __name__ == '__main__':
    app.run(debug=True)
