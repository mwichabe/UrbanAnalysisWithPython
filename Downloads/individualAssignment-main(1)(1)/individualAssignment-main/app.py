from flask import Flask, render_template

app = Flask(__name__)

def calculate_triangle_number(n):
    return n * (n + 1) // 2

@app.route("/")
def triangle_numbers():
    numbers_to_calculate = [1, 2, 3, 4, 5]
    triangle_data = {n: calculate_triangle_number(n) for n in numbers_to_calculate}
    return render_template('individual.html', triangle_data=triangle_data)

if __name__ == '__main__':
    app.run(debug=True)
