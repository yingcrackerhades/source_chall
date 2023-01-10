from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input = request.form['input']
        input = input.replace(' ', '')
        if "cat" in input or "head" in input or "tail" in input or "nano" in input or "vi" in input or "vim" in input or "more" in input:
            return '''
            <html>
            <head>
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
            </head>
            <body class="d-flex align-items-center justify-content-center">
                <form action="/" method="get" class="p-5 border border-secondary rounded">
                <h3 class="text-center mb-4">Command : {}</h3>
                <p>Not Allowed</p>
                <a href="/" class="btn btn-primary btn-block">Back</a>
                </form>
            </body>
        </html>
        '''.format(input)
        try:
            output = subprocess.check_output(input, shell=True).decode()
        except subprocess.CalledProcessError as e:
            output = f"Invalid command: {input}"
        return '''
        <html>
            <head>
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
            </head>
            <body class="d-flex align-items-center justify-content-center">
                <form action="/" method="get" class="p-5 border border-secondary rounded">
                <h3 class="text-center mb-4">Command : {}</h3>
                <div class="form-group">
                    <textarea class="form-control" rows="20" readonly>{}</textarea>
                </div>
                <a href="/" class="btn btn-primary btn-block">Back</a>
                </form>
            </body>
        </html>
        '''.format(input, output)
    else:
        return '''
        <html>
            <head>
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
            </head>
            <body class="d-flex align-items-center justify-content-center">
                <form action="/" method="post" class="p-5 border border-secondary rounded">
                <h3 class="text-center mb-4">Enter a command:</h3>
                <div class="form-group">
                    <input type="text" id="input" name="input" placeholder="command" class="form-control">
                </div>
                <button type="submit" class="btn btn-primary btn-block">Submit</button>
                </form> 
            </body>
        </html>
       '''


if __name__ == "__main__":
  app.run(host='0.0.0.0')