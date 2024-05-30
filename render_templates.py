from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render_index():
    rendered_index = render_template('index.html')
    with open('docs/index.html', 'w') as file:
        file.write(rendered_index)
    return 'Index.html generated successfully!'

@app.route('/result')
def render_result():
    rendered_result = render_template('result.html')
    with open('docs/result.html', 'w') as file:
        file.write(rendered_result)
    return 'Result.html generated successfully!'

if __name__ == '__main__':
    app.run(debug=True)
