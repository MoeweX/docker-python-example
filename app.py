from flask import Flask
import os
import socket

app = Flask(__name__)

filename = "/data/storage.txt"

@app.route("/")
def hello():

    visits = 0

    try:
        with open(filename, 'r+') as f:
            text = f.read()
            print("Read: " + text)
            visits = int(text)
    except IOError:
        print("No visits present yet, setting to 0")

    with open(filename, 'w+') as f:
        new_visits = visits + 1;
        f.seek(0)
        f.write(str(new_visits))
        f.truncate()

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {new_visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), new_visits=new_visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
