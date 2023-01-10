from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["PUT", "GET"])
def home():
  if request.method == "PUT":
    # jika request method adalah PUT, tampilkan flag
    return "pwn0{ndasmu_c0k}"
  else:
    # jika request method bukan PUT, tampilkan halaman biografi
    return """
      <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
            <style>
              body {
                background-color: black;
              }
              @media (max-width: 768px) {
                .card {
                  width: 100%;
                  margin-top: 100px;
                  border-color: cyan;
                }
              }
              h5 {
                color: red;
                text-shadow: 1px 1px 3px white;
              }
              p {
                color: gray;
              }
            </style>
            <title>0xPwn0</title>
          </head>
          <body>
            <div class="card mx-auto" style="width: 18rem;">
              <img class="card-img-top" src="https://i.pinimg.com/736x/06/e2/f3/06e2f31262293a5ed6467badc62926e1.jpg">
              <div class="card-body d-flex flex-column align-items-center">
                <h5 class="card-title">0xPwn0</h5>
                <p class="card-text">Hacking is the art exploitation, not a crime</p>
              </div>
            </div>
          </body>
        </html>
    """

if __name__ == "__main__":
  app.run(host='0.0.0.0')
