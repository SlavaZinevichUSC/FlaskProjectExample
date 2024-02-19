# Custom Docker Instance for Python Server with Image Classification

## Overview
This project demonstrates the deployment of a custom Docker instance hosting a Python server capable of running a machine learning classification algorithm on images. The server utilizes a pre-trained ResNet for image classification tasks.

## Features
- Dockerized environment for easy deployment and scalability.
- Python server for handling image classification requests.
- Integration of a machine learning model for image classification tasks.
- RESTful API endpoints for interacting with the server.

## Requirements
- Docker installed on the host machine.

## Installation and Usage
1. Clone this repository to your local machine.
   ```
   git clone https://github.com/SlavaZinevichUSC/FlaskProjectExample
   ```

2. Navigate to the project directory.
   ```
   cd your_repository
   ```

3. Build the Docker image.
   ```
   docker build -t image_classification_server .
   ```

4. Run the Docker container.
   ```
   docker run -d -p 5000:5000 image_classification_server
   ```

5. Once the container is running, you can send image classification requests to the server at `http://localhost:5000/classify`.

## API Endpoints
- `/classify`: POST request to classify an image. Send a multipart form-data request with an image file attached.

## Example Usage
```python
import requests

url = 'http://localhost:5000/binary'
files = {'image': open('path_to_your_image.jpg', 'rb')}
response = requests.post(url, files=files)
print(response.json())
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs, feature requests, or questions.

## License
This project is licensed under the [MIT License](LICENSE).
