# Big Data Dashboard

This project is a Streamlit application designed for the "Introduction to Cybernetics" course, focusing on the challenges and trends in Big Data. The application features an interactive dashboard that allows users to explore real-time data simulations, analyze data quality, and learn about serverless architectures.

## Project Structure

```
big-data-dashboard
├── src
│   ├── app.py               # Main application file for the Streamlit dashboard
│   ├── introduction.py      # Introduction page for student name input and redirection
│   └── database
│       └── data.db         # SQLite database for storing student names
├── requirements.txt         # List of dependencies required for the project
└── README.md                # Documentation for the project
```

## Features

- **Real-Time Data Simulation**: Simulates temperature readings from sensors in real-time.
- **Data Quality Analysis**: Provides insights into data quality and suggestions for handling missing values.
- **Serverless Architecture Overview**: Explains the concept and advantages of serverless computing.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd big-data-dashboard
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   streamlit run src/app.py
   ```

4. Access the application in your web browser at `http://localhost:8501`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.