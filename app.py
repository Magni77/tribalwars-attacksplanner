from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def input_form():
    return render_template('attack-form.html')


@app.route('/', methods=['POST'])
def my_form_post():
    """
    input
    {
      "target": str,
      "attackers": [
        {
          "cords": str,
          "slowestUnit": str[axe, light], # TODO add all units
          "arriveTime": datetime
        }
      ]

    }
    :return:
    {
      "results":[
        {"cordX": str, "start": str, "duration": str, "arriveAt": str},
        {"cordX": str, "start": str, "duration": str, "arriveAt": str},
      ]
    }
    """
    text = request.form['text']
    processed_text = text.upper()
    return processed_text


if __name__ == '__main__':
    app.run(debug=True, )
