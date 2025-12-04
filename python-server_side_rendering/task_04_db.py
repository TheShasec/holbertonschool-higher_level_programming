from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# -----------------------------
# Helper: Load JSON data
# -----------------------------
def load_json_data():
    try:
        with open("products.json") as json_file:
            return json.load(json_file)
    except Exception as e:
        return {"error": f"JSON loading error: {str(e)}"}

# -----------------------------
# Helper: Load CSV data
# -----------------------------
def load_csv_data():
    try:
        products = []
        with open("products.csv") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                row["price"] = float(row["price"])   # Convert to numeric
                products.append(row)
        return products
    except Exception as e:
        return {"error": f"CSV loading error: {str(e)}"}

# -----------------------------
# Helper: Load SQLite data
# -----------------------------
def load_sql_data():
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        conn.close()

        # Convert rows into list of dictionaries
        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        return products

    except Exception as e:
        return {"error": f"Database error: {str(e)}"}


# -----------------------------
# Main Route
# -----------------------------
@app.route("/products")
def display_products():
    source = request.args.get("source", "").lower()

    if source == "json":
        products = load_json_data()

    elif source == "csv":
        products = load_csv_data()

    elif source == "sql":
        products = load_sql_data()

    else:
        return render_template("product_display.html",
                               error="Wrong source",
                               products=None)

    # Handle errors inside data loading
    if isinstance(products, dict) and "error" in products:
        return render_template("product_display.html",
                               error=products["error"],
                               products=None)

    return render_template("product_display.html",
                           error=None,
                           products=products)


if __name__ == "__main__":
    app.run(debug=True)

