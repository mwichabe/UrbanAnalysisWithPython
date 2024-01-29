from flask import Flask, render_template

app = Flask(__name__)

def sum_of_squares_count(n):
    count = 0
    for x in range(int(n**0.5) + 1):
        y_squared = n - x**2
        y = int(y_squared**0.5)
        if x**2 + y**2 == n:
            count += 1
    return count

def analyze_remainder_patterns():
    remainder_patterns = {}
    for remainder in range(4):
        pattern_counts = {}
        for n in range(1, 101): 
            if n % 4 == remainder:
                count = sum_of_squares_count(n)
                pattern_counts[n] = count
        remainder_patterns[remainder] = pattern_counts
    return remainder_patterns
#  sums of triangular numbers
def triangular_number_count(n):
    count = 0
    for x in range(n + 1):
        for y in range(n + 1):
            for z in range(n + 1):
                if x + y + z == n:
                    count += 1
    return count

# Test the function
for n in range(1, 11):
    ways = triangular_number_count(n)
    print(f"Number {n}: {ways} ways to write as a sum of three triangular numbers")


@app.route('/')
def index():
    # Use your functions to get data
    sums_of_squares_data = {number: sum_of_squares_count(number) for number in [3, 4, 5, 6]}
    remainder_patterns_data = analyze_remainder_patterns()
    triangular_numbers_data = {n: triangular_number_count(n) for n in range(1, 11)}

    # Render the HTML template with data
    return render_template('individual.html',
                           sums_of_squares_data=sums_of_squares_data,
                           remainder_patterns_data=remainder_patterns_data,
                           triangular_numbers_data=triangular_numbers_data)

if __name__ == '__main__':
    app.run(debug=True)