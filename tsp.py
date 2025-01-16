import random
import time
import streamlit as st
import numpy as np

def calculate_route_length(route, distance_matrix):
    length = 0
    for i in range(len(route) - 1):
        length += distance_matrix[route[i]][route[i + 1]]
    length += distance_matrix[route[-1]][route[0]]
    return length

def find_best_neighbour(current_route, distance_matrix):
    best_route = current_route[:]
    best_length = calculate_route_length(best_route, distance_matrix)
    for i in range(len(current_route)):
        for j in range(i + 1, len(current_route)):
            neighbor = current_route[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbor_length = calculate_route_length(neighbor, distance_matrix)

            if neighbor_length < best_length:
                best_route = neighbor
                best_length = neighbor_length

    return best_route, best_length

def hill_climb_tsp(distance_matrix):
    num_cities = len(distance_matrix)
    current_route = list(range(num_cities))
    random.shuffle(current_route)
    current_length = calculate_route_length(current_route, distance_matrix)

    start_time = time.time()
    while True:
        best_route, best_length = find_best_neighbour(current_route, distance_matrix)

        if best_length < current_length:
            current_route, current_length = best_route, best_length
        else:
            break

    end_time = time.time()
    time_taken = end_time - start_time

    return current_route, current_length, time_taken



def main():
    st.title("Travelling Salesman Problem Solver - Hill Climb Algorithm")

    num_cities = st.number_input("Enter the number of cities:", min_value=2, max_value=20, step=1)

    if num_cities:
        st.write("Enter the distance matrix row by row:")
        distance_matrix = []
        for i in range(num_cities):
            row = st.text_input(f"Row {i + 1} (space-separated distances):", key=f"row_{i}")
            if row:
                try:
                    distance_matrix.append(list(map(int, row.split())))
                except ValueError:
                    st.error(f"Invalid input in Row {i + 1}. Please enter space-separated integers.")

        if len(distance_matrix) == num_cities:
            if st.button("Solve TSP"):
                with st.spinner("Finding the shortest path..."):
                    best_route, shortest_path_length, time_taken = hill_climb_tsp(distance_matrix)

                st.success("Results:")
                st.write("Best Route:", " -> ".join(map(str, [city + 1 for city in best_route])))
                st.write("Shortest Path Length:", shortest_path_length)
                st.write(f"Time Taken: {time_taken:.4f} seconds")


               

if __name__ == "__main__":
    main()

import streamlit as st

def add_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

background_image_url = "data:image/jpeg;base64,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"
add_background(background_image_url)

import mysql.connector
from mysql.connector import errorcode

def setup_database(host="localhost", user="root", password="", database="tsp_db"):
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        cursor = conn.cursor()

        # Create the database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")

        # Connect to the specified database
        conn.database = database

        # Create tables
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS DistanceMatrix (
                id INT AUTO_INCREMENT PRIMARY KEY,
                city_count INT,
                distances TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Results (
                id INT AUTO_INCREMENT PRIMARY KEY,
                best_route TEXT,
                shortest_path_length INT,
                time_taken FLOAT
            )
        """)

        conn.commit()
        print(f"Database '{database}' setup complete.")
        return conn

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Incorrect username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(f"Error: Database '{database}' does not exist and could not be created.")
        else:
            print(err)

# Usage example
if __name__ == "__main__":
    connection = setup_database(host="localhost", user="your_username", password="your_password", database="tsp_db")

def save_distance_matrix(conn, city_count, distance_matrix):
    cursor = conn.cursor()

    distances = ",".join(map(str, [item for sublist in distance_matrix for item in sublist]))
    cursor.execute("INSERT INTO DistanceMatrix (city_count, distances) VALUES (?, ?)", (city_count, distances))
    conn.commit()
    print("Distance matrix saved successfully.")

def fetch_distance_matrix(conn, matrix_id):
    cursor = conn.cursor()
    cursor.execute("SELECT city_count, distances FROM DistanceMatrix WHERE id = ?", (matrix_id,))
    row = cursor.fetchone()
    if row:
        city_count, distances = row

        distance_matrix = [
            list(map(int, distances.split(",")))[i * city_count:(i + 1) * city_count]
            for i in range(city_count)
        ]
        print(f"Retrieved distance matrix with ID {matrix_id}:")
        for row in distance_matrix:
            print(row)
        return distance_matrix
    else:
        raise ValueError("No distance matrix found with the given ID.")

def save_results(conn, best_route, shortest_path_length, time_taken):
    cursor = conn.cursor()

    route_str = ",".join(map(str, best_route))
    cursor.execute(
        "INSERT INTO Results (best_route, shortest_path_length, time_taken) VALUES (?, ?, ?)",
        (route_str, shortest_path_length, time_taken)
    )
    conn.commit()
    print("TSP results saved successfully.")

def fetch_all_results(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, best_route, shortest_path_length, time_taken FROM Results")
    rows = cursor.fetchall()
    if rows:
        print("TSP Results:")
        for row in rows:
            print(f"ID: {row[0]}, Best Route: {row[1]}, Shortest Path Length: {row[2]}, Time Taken: {row[3]:.4f} seconds")
    else:
        print("No results found.")


if __name__ == "__main__":
    conn = setup_database()

import streamlit as st
import mysql.connector

# Database configuration
db_config = {
    'host': '127.0.0.1',  # e.g., '127.0.0.1' or a remote IP
    'user': 'root',
    'password': 'carolyn',
    'database': 'tsp_database'
}

# Connect to MySQL
def connect_to_mysql():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as e:
        st.error(f"Error: {e}")
        return None

# Function to insert user input into the database
def insert_data(city1, city2, distance):
    connection = connect_to_mysql()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO tsp_data (city1, city2, distance) VALUES (%s, %s, %s)"
        cursor.execute(query, (city1, city2, distance))
        connection.commit()
        cursor.close()
        connection.close()
        st.success("Data successfully inserted into the database.")

def main():
    st.title("TSP Problem Data Entry")

    # User input for city1, city2, and distance
    city1 = st.number_input("Enter City 1 ID:", min_value=1)
    city2 = st.number_input("Enter City 2 ID:", min_value=1)
    distance = st.number_input("Enter Distance Between City 1 and City 2:", min_value=0.0, step=0.1)

    if st.button("Insert Data"):
        insert_data(city1, city2, distance)

if __name__ == "__main__":
    main()
