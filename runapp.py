from flask import Flask, render_template, make_response

app = Flask(__name__, template_folder="./templates", static_folder='./static')




# def get_question(id):



@app.route('/')
def index():
    html = render_template(
        'index.html'
    )
    result = make_response(html)
    return result

@app.route('/question/<num>')
def question(num):
    to_render = f"question{num}.html"
    html = render_template(to_render)
    result = make_response(html)
    return result

@app.route('/results')
def results():
    html = render_template("results.html")
    result = make_response(html)
    return result


# @app.route('/game')
# def game_page():
#     html = render_template('game.html')
#     result = make_response(html)
#     return result 

# @app.route('/help')
# def help_page():
#     html = render_template('help.html')
#     result = make_response(html)
#     return result 

# @app.route('/exit')
# def exit_page():
#     html = render_template('exit.html')
#     result = make_response(html)
#     return result

# @app.route('/win')
# def win_page():
#     html = render_template('win.html')
#     result = make_response(html)
#     return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5100, debug=True)


# from time import strftime, localtime
# from flask import Flask, render_template, request, make_response


# app = Flask(__name__, template_folder=".")


# @app.route('/', methods=['GET'])
# @app.route('/index', methods=['GET'])
# def index():
#     # html = render_template("index.html")
#     # response = make_response(html)

#     # return response
#     print("rendering template")
#     return render_template("index.html")