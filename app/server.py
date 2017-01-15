from flask import Flask, render_template
from flask_sslify import SSLify

app = Flask(__name__)
ssify = SSLify(app)

@app.route('/')
def index():
  return render_template('pyrss2gen.xml'), 201, {'Content-Type': 'application/xml' }

if __name__ == '__main__':
  app.run(debug=True)
