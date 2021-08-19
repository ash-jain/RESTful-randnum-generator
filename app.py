import json
from random import random

from flask import Flask, request


app = Flask(__name__)

def rand_num_gen(lower: float = 0, upper: float = 1, count: int = 1) -> json:
    obj = {
        'status': "200 OK",
        'lower': lower,
        'upper': upper,
        'count': count,
        'result': None,
    }

    if lower >= upper:
        obj['status'] = "400 Bad Request"
        obj['message'] = "lower limit should be less than upper limit."
    elif count < 1:
        obj['status'] = "400 Bad Request"
        obj["message"] = "count should be greater than or equal to 1."
    else:
        if count > 256:
            count = 256

        obj['result'] = [(random() * (upper-lower)) + lower for _ in range(count)]

    return json.dumps(obj, indent=4, sort_keys=False)


@app.route("/")
def index():
    return app.send_static_file('index.html')


@app.route("/api")
def api():
    lower = request.args.get('lower', default=0.0, type=float)
    upper = request.args.get('upper', default=1.0, type=float)
    count = request.args.get('count', default=1.0, type=float)
    print(lower, upper, count)
    return rand_num_gen(lower, upper, round(count))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5500", debug=True)