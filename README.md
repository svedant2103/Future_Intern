# Future_Intern
A real Estate House Price Prediction model 

# House Price Prediction

This repository contains the implementation of a machine learning project to predict house prices based on features such as square footage, number of bedrooms, and other relevant attributes. The project includes data preprocessing, model training, evaluation, and deployment as a Flask-based web application.

## Features

- **Data Preprocessing:** Handling missing values, scaling numerical features, and ensuring data quality.
- **Machine Learning Models:** Linear Regression and Decision Trees were used for training.
- **Evaluation Metrics:** Mean Squared Error (MSE) for performance evaluation.
- **Web Application:** A Flask-based web interface for real-time house price prediction.
- **Deployment:** Deployed on GitHub for version control and accessibility.

## Tech Stack

- **Programming Language:** Python
- **Libraries:** Scikit-learn, Pandas, NumPy, Matplotlib
- **Web Framework:** Flask
- **Deployment:** GitHub

## Dataset

The dataset used is `ParisHousing.csv`, which contains the following columns:
- **Area**
- **Number of Rooms**
- **Number of Bathrooms**
- **Price**
- **Number of Floors**
- **Has Pool**, etc.

An additional processed dataset, `final_dataset.csv`, is generated during the preprocessing stage.

---

## Project Structure

---

The project is organized as follows:

# .gitignore: Files to ignore in the Git repository
# LICENSE: Project license
# LinearRegressionModel.pkl: Serialized machine learning model
# ParisHousing.csv: Raw dataset
# README.md: Project documentation
# RealEstateHousePricePredictionUsingML_Project.ipynb: Jupyter Notebook with detailed analysis
# final_dataset.csv: Preprocessed dataset
# main.py: Main script for preprocessing, training, and prediction

---

## How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/house-price-prediction.git
cd house-price-prediction
```

### 2. Install Dependencies
Install the required Python libraries using pip:
```bash
pip install -r requirements.txt
```

### 3. Run the Flask Application
Navigate to the `app` directory and start the Flask server:
```bash
cd app
python app.py
```
Access the application at `http://127.0.0.1:5000/` in your browser.

## Exploratory Data Analysis (EDA)
EDA was conducted using Pandas and Matplotlib to uncover patterns and correlations in the dataset. Key insights include:
- Strong positive correlation between square footage and house prices.
- Distribution of house prices is positively skewed.

## Model Performance
- **Linear Regression:** Achieved a Mean Squared Error (MSE) of 2100 and an accuracy of 86%.
- **Decision Tree:** Achieved a Mean Squared Error (MSE) of 1800 and an accuracy of 85%.

## Deployment
The application was deployed on GitHub to ensure version control and accessibility. Flask was used to create a user-friendly interface for real-time predictions.

## Future Improvements
- Integrate advanced models such as Random Forest and Desicion Trees.
- Add more features to the dataset for better predictions.

## Results
The model achieves a satisfactory accuracy based on metrics such as Mean Squared Error (MSE) and R² score. The detailed evaluation can be found in the Jupyter Notebook.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements
Special thanks to Future Intern for their guidance and support during the development of this project.

