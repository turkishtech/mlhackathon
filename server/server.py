from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    """Main Page"""
    global results
    global data
    global start
    print(data)
    return render_template('index.html', data=results, start=start, input=data)

@app.route('/categorize', methods=['POST'])
def categorize():
    global results
    global start
    global data
    start = "False"
    data = request.form['text_to_categorize']
    method = request.form['method']
    results = get_results(data, method)
    return redirect("/")


def get_results(input_data, method):
    results = ['Results for Task %s:' % method]
    if method == "1a":
        # do calculations
        output = None
        pass

    elif method == "1b":
        # do calculations
        output = None
        pass

    elif method == "2":
        # do calculations
        output = None
        pass

    # first index in array is used for task identification
    results[1:] = ["Prediction 1", "Prediction 2", "..."]
    return results


if __name__ == "__main__":
    results = []
    data = ""
    start = "True"
    app.run(host="localhost", port=8008, debug=False)
