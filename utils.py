import json

def load_candidates_from_json(path):
    """Функция чтения данных с json файла"""
    with open(path, 'r', encoding='utf-8') as file_read:
        data = json.load(file_read)
    return data

def get_candidate(candidate_id, candidates):
    """Функция получения кандидата по id"""
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate
    return None

def get_candidates_by_name(candidate_name, candidates):
    """Функция получения списка кандидатов по имени"""
    candidates_name = []
    for candidate in candidates:
        if candidate_name.lower() in candidate['name'].lower().split():
            candidates_name.append(candidate)
    return candidates_name

def get_candidates_by_skill(skill_name, candidates):
    """Функция получения списка кандидатов по скиллам"""
    candidates_skill = []
    for candidate in candidates:
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            candidates_skill.append(candidate)
    return candidates_skill

