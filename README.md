# Travelling-Salesman-Problem
Travelling Salesman Problem (TSP) Solver Using Hill Climb Algorithm:
        
        This project implements a solution to the Travelling Salesman Problem (TSP) using the Hill Climb Algorithm in Python. The solution is integrated with a Streamlit web application for interactive input, visualization, and result display. Additionally, a MySQL database is used for storing distance matrices and computed results.

Features:

1) User-friendly GUI: Built with Streamlit for easy interaction.

2) Hill Climb Algorithm: A heuristic approach to solving TSP.

3) Database Integration: Stores and retrieves distance matrices using MySQL.

4) Custom Background: Enhances UI aesthetics with a background image.

5) Input Validation: Ensures the user provides a valid distance matrix.

6) Optimized Route Calculation: Generates an optimal path for the travelling salesman problem.

Running the Application

1️⃣ Start MySQL Server

Ensure MySQL is running before executing the script.

2️⃣ Run Streamlit App

Execute the following command to launch the web app:

streamlit run app.py

How to Use:

1. Enter the number of cities and provide a distance matrix in the input fields.

2. Click Solve TSP to start the optimization process.

3. The algorithm will find an optimal route and display it.

4. Optionally, save the computed distance matrix for future use.

5. Retrieve and view stored matrices and results from the database.

