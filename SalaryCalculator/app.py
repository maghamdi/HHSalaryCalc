from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    net_salary = float(request.form['net_salary'])

    base_salary = net_salary / 1.228125
    housing_allowance = 0.25 * base_salary
    transportation_allowance = 0.10 * base_salary
    social_security_deduction = 0.0975 * (base_salary + housing_allowance)
    total_salary = base_salary + housing_allowance + transportation_allowance

    result = {
        'base_salary': round(base_salary, 2),
        'housing_allowance': round(housing_allowance, 2),
        'transportation_allowance': round(transportation_allowance, 2),
        'social_security_deduction': round(social_security_deduction, 2),
        'total_salary': round(total_salary, 2),
        'net_salary': round(net_salary, 2)
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
