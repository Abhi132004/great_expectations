from flask import Flask, render_template
import great_expectations as ge

#Flask init
app = Flask(__name__)

# Initialize the Great Expectations DataContext
context = ge.data_context.DataContext('/path/to/your/ge/project')

# Define a route to perform data quality checks
@app.route('/data_quality_checks')
def data_quality_checks():
    # Replacing data asset with the actual data asset name Great Expectations project
    data_asset = context.get_data_asset('your_data_asset')

    #data quality checks
    results = data_asset.validate()

    # Rendering the results on a web page
    return render_template('data_quality.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
