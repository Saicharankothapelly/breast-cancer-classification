# breast-cancer-classification

# software and tools requirements 

1.[Github Account](https://github.com)
2.[VS code IDE](https://code.visualstudio.com/)
3.[GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)
4.[HerokuAccount](https://heroku.com)

A web application that classifies breast cancer using machine learning. Users can input tumor features, and the model predicts whether it's benign or malignant.

## Features  
Breast cancer classification using different ML algorithms 
Exploratory Data Analysis (EDA)
Data Cleaning
Web-based UI for easy predictions  

## 📂 Dataset  
We used the **Wisconsin Breast Cancer Dataset (WBCD)** from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)).

Target Classes:
  -B (Benign) → 1
  - M (Malignant) → 0 
- Features:
  - Mean radius, texture, perimeter, area, smoothness, etc.  
  - 30 numerical attributes  

## Installation

1.Clone the repo:

2.Install dependencies:

pip install -r requirements.txt

3.Run thr Flask app

python app.py

4. Open `http://127.0.0.1:5000` in a browser.


## Usage
- Enter tumor features in the form.
- Click "Classify" to get predictions.


## Technologies Used
- Python
- Flask
- HTML/CSS
- Scikit-learn


## Contributing
Pull requests are welcome! Open an issue first to discuss changes.


## License
This project is licensed under the Apache License.