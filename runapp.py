from flask import Flask, render_template, make_response, redirect, url_for

from database import question_dict, answer_dict
from clubs import all_clubs

app = Flask(__name__, template_folder="./templates", static_folder='./static')




# def get_question(id):

def process_answers(dictionary):
    answers = []
    for key in dictionary.keys():
        answers.append([key, dictionary[key]])
    return answers

def process_questions(dictionary):
    questions = []
    for key in dictionary.keys():
        questions.append([dictionary[key], key])
    return questions

def get_question_answers(qid): 
    qid = int(qid)
    question = question_dict[qid]
    answers = answer_dict[qid]
    return(question, answers)


#get next qid
def get_next_qid(qid, answer):
    if(qid == 1 or qid == 2):
        return answer_dict[qid][answer]
    elif(3 <= qid <= 6):
        return 2
    else: return -1 

class Responses:
    def __init__(self):
        self.club_names = []
    
    def add_club(self, clubname):
        self.club_names.append(clubname)

    def add_clubs(self, clubs:list):
        for club in clubs:
            self.add_club(club)
    
    def get_clubs(self):
        return self.club_names
    
    def reset_clubs(self):
        self.club_names = []


responses = Responses()

@app.route('/')
def index():
    responses.reset_clubs()
    html = render_template(
        'index.html'
    )
    result = make_response(html)
    return result



@app.route('/question/<num>')
def question(num):
    details = get_question_answers(num)
    question = [details[0], num]
    answers = process_answers(details[1])

    print(answers)
    print(type(question), type(answers))
    html = render_template("question.html",
                           question=question,
                           answers = answers
                           )
    response = make_response(html)
    return response

@app.route('/response/<qid>/<id>')
def response(qid, id):
    qid = int(qid)
    # if question id is 1 or 2, redirect to the corresponding question
    if qid == 1 or qid == 2:
        return redirect(f"/question/{id}")
    elif qid > 2 and qid <= 6:
        res = all_clubs[int(id)]
        responses.add_clubs(res)
        return redirect("/question/2")
    elif qid > 6:
        res = all_clubs[int(id)]
        responses.add_clubs(res)
        return redirect(url_for("results"))
    

@app.route('/results')
def results():
    results = responses.get_clubs()
    html = render_template("results.html", results=results)
    result = make_response(html)
    return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5100, debug=True)

