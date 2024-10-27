from flask import Flask, render_template, request
import recommendations  # Import the recommendation logic

app = Flask(__name__)

@app.route('/')
def index():
    """This corresponds to frame1.py"""
    return render_template('index.html')

@app.route('/menu')
def menu():
    """This corresponds to frame2.py"""
    return render_template('menu.html')

@app.route('/recommendation', methods=['GET', 'POST'])
def recommendation():
    """This corresponds to frame3.py"""
    if request.method == 'POST':
        family_members = request.form.get('family_members', 1)
        budget = request.form.get('budget', 8000)
        fuel_type = request.form.get('fuel_type', 'Petrol')

        # Log the inputs for debugging
        print(f"Input received - Family Members: {family_members}, Budget: {budget}, Fuel Type: {fuel_type}")

        # Call the recommend function from recommendations.py
        results = recommendations.recommend(family_members, budget, fuel_type)

        # Log the results for debugging
        print(f"Results: {results}")

        # Pass the results to the template
        return render_template('recommendation.html', results=results)
    return render_template('recommendation.html')

if __name__ == '__main__':
    app.run(debug=True)
