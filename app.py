from flask import Flask, render_template
import utils

app = Flask(__name__)

file_name = 'candidates.json' # Имя файла
candidates = utils.load_candidates_from_json(file_name) # Список кандидатов из файла

@app.route('/')
def page_list():  # Страница со списком кандидатов
    return render_template('list.html', candidates = candidates)

@app.route('/candidate/<int:id>')
def page_single(id): # Страница кандидата по его id
    candidate = utils.get_candidate(id, candidates)
    return render_template('single.html', candidate = candidate)

@app.route('/search/<candidate_name>')
def page_search(candidate_name): # Старница кандидатов по найденому имени
    candidates_name = utils.get_candidates_by_name(candidate_name, candidates)
    len_ = len(candidates_name)
    return render_template('search.html', candidates_name = candidates_name, len_ = len_)

@app.route('/skill/<skill_name>')
def page_skill(skill_name): # Страница кандидатов по найденому скилу
    candidates_skill = utils.get_candidates_by_skill(skill_name, candidates)
    len_ = len(candidates_skill)
    return render_template('skill.html', candidates_skill = candidates_skill, len_ = len_, skill_name = skill_name)

if __name__ == '__main__':
    app.run()
