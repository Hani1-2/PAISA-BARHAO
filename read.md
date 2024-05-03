# Project Name: SmartInvest.AI

## Project Deployment
1. Project is deployed at following URL `https://samrtinvestai.netlify.app/`.

## Project Architecture
![SmartInvest.AI](architecture.png)


## Description
SmartInvest.AI will provide accessible insights into various investment options, including stocks, commodities, and mutual funds, tailored to the Pakistani market. Through the app, users can gain valuable information and comparisons to make informed investment decisions, promoting financial literacy and inclusion.

## Technologies Used
- Python
- Flask
- FAISS
- LangChain 
- Docker

## Installation
1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Set up your database configurations in `config.py`.
5. Run the application using `python main.py`.

## Usage
1. Build Image using `docker build -t flask_app .`.
2. Run the server using command `docker run -p 5000:5000 flask_app `
2. Make API requests to endpoints for data processing and model predictions.

## Using Docker
1. Ensure the backend server is running.
2. Make API requests to endpoints for data processing and model predictions.

## Endpoints
- `/api/ask_question`: Endpoint for retrieval of questions answers.
- `/api/create_vector_db`: Endpoint for refresh and update vector DB.

## Contributing
Feel free to contribute to this project by submitting pull requests or reporting issues.
