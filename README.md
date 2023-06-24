# VegetableFruitClassifier-API

This repository contains the code for an API server that performs image classification using a pre-trained Vegetable and Fruit Classifier model. The API server is built using Python and Flask framework.

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Download the pre-trained model weights and place them in the project directory.

## Usage

1. Start the API server:
```bash
python app.py
```

2. The server will start running on http://localhost:5000.

3. Make a POST request to http://localhost:5000/classify endpoint with an image file as the payload. The server will return the classification result in the response.

## API Endpoint

1. POST /classify: Perform image classification on the provided image file.

a. Request Parameters:

    image: The image file to be classified.

b. Response:

    On success, the response will include the classification result in JSON format:
```json
{
  "classification": "apple"
}
```
    On failure, the response will include an error message:
```json
{
  "error": "No image found"
}
```

## Customize and Extend

1. You can modify the pre-processing steps in the classify function in app.py according to your requirements.

2. Update the class_labels list in app.py with the appropriate labels based on your classification classes.

## Contributing
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

Feel free to customize and modify the README according to your specific needs, including adding more sections such as Dependencies, Testing, Deployment, etc.

Let me know if you need any further assistance!
