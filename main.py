# Import necessary libraries
from flask import Flask, render_template, request
import pandas as pd
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load dataset and model
df = pd.read_csv('final_dataset.csv')  # Ensure the path is correct
pipe = pickle.load(open("LinearRegressionModel.pkl", 'rb'))  # Ensure the path is correct

# Route for the home page
@app.route('/')
def index():
    # Sorting the features from the dataset for the dropdowns
    squareFeets = sorted(df['squareMeters'].unique())
    Bedrooms = sorted(df['numberOfRooms'].unique())
    furnished_floors = sorted(df['floors'].unique())
    Pincode = sorted(df['cityCode'].unique())
    Renders = sorted(df['numPrevOwners'].unique())
    Origin = sorted(df['made'].unique())
    newly_Build = sorted(df['isNewBuilt'].unique())
    base = sorted(df['basement'].unique())
    store_rooms = sorted(df['hasStorageRoom'].unique())
    guest_rooms = sorted(df['hasGuestRoom'].unique())
    
    # Render the HTML template and pass the dropdown options
    return render_template('index.html', squareFeets=squareFeets, Bedrooms=Bedrooms,
                           furnished_floors=furnished_floors, Pincode=Pincode, 
                           Renders=Renders, Origin=Origin, newly_Build=newly_Build, 
                           base=base, store_rooms=store_rooms, guest_rooms=guest_rooms)

# Route for handling predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve form data
    squareFeets = request.form.get('squareMeters')
    Bedrooms = request.form.get('numberOfRooms')
    furnished_floors = request.form.get('floors')
    Pincode = request.form.get('cityCode')
    Renders = request.form.get('numPrevOwners')
    Origin = request.form.get('made')
    newly_Build = request.form.get('isNewBuilt')
    base = request.form.get('basement')
    store_rooms = request.form.get('hasStorageRoom')
    guest_rooms = request.form.get('hasGuestRoom')
    
    # Create a DataFrame with the input data
    input_data = pd.DataFrame([[squareFeets, Bedrooms, furnished_floors, Pincode, Renders, Origin, 
                                newly_Build, base, store_rooms, guest_rooms]], 
                                columns=['squareMeters', 'numberOfRooms', 'floors', 'cityCode', 
                                         'numPrevOwners', 'made', 'isNewBuilt', 'basement', 
                                         'hasStorageRoom', 'hasGuestRoom'])

    # Handling unknown categories in input (optional)
    for column in input_data.columns:
        # If the input contains unknown categories, replace them with the mode of the corresponding column
        if input_data[column].iloc[0] not in df[column].unique():
            input_data[column] = df[column].mode()[0]

    # Predict the price
    prediction = pipe.predict(input_data)[0]

    # Return the predicted price as a string
    return str(prediction)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=5000)
