from flask import Blueprint, jsonify
from datetime import datetime

status_routes = Blueprint('general', __name__)

date_format = '%d/%m/%Y'

gameweek_mapper = {

    1: ['16/08/2024', '24/08/2024'],
    2: ['24/08/2024', '31/08/2024'],
    3: ['31/08/2024', '14/09/2024'],
    4: ['14/09/2024', '21/09/2024'],
    5: ['21/09/2024', '28/09/2024'],
    6: ["28/09/2024", "05/10/2024"],
    7: ["05/10/2024", "19/10/2024"],
    8: ["19/10/2024", "25/10/2024"],
    9: ["25/10/2024", "02/11/2024"],
    10: ["02/11/2024", "09/11/2024"],
    11: ["09/11/2024", "23/11/2024"],
    12: ["23/11/2024", "29/11/2024"],
    13: ["29/11/2024", "03/12/2024"],
    14: ["03/12/2024", "07/12/2024"],
    15: ["07/12/2024", "14/12/2024"],
    16: ["14/12/2024", "21/12/2024"],
    17: ["21/12/2024", "26/12/2024"],
    18: ["26/12/2024", "29/12/2024"],
    19: ["29/12/2024", "04/01/2025"],
    20: ["04/01/2025", "14/01/2025"],
    21: ["14/01/2025", "18/01/2025"],
    22: ["18/01/2025", "25/01/2025"],
    23: ["25/01/2025", "01/02/2025"],
    24: ["01/02/2025", "14/02/2025"],
    25: ["14/02/2025", "21/02/2025"],
    26: ["21/02/2025", "25/02/2025"],
    27: ["25/02/2025", "08/03/2025"],
    28: ["08/03/2025", "15/03/2025"],
    29: ["15/03/2025", "01/04/2025"],
    30: ["01/04/2025", "05/04/2025"],
    31: ["05/04/2025", "12/04/2025"],
    32: ["12/04/2025", "19/04/2025"],
    33: ["19/04/2025", "26/04/2025"],
    34: ["26/04/2025", "03/05/2025"],
    35: ["03/05/2025", "10/05/2025"],
    36: ["10/05/2025", "18/05/2025"],
    37: ["18/05/2025", "25/05/2025"],
    38: ["25/05/2025", "25/05/2025"]

}

def set_gameweek_status() -> tuple[int, int]:
    today_date = datetime.now().date()

    current_gameweek = 0
    next_gameweek = 0

    for key, value in gameweek_mapper.items():
        start_date = datetime.strptime(value[0], date_format).date()
        end_date = datetime.strptime(value[1], date_format).date()

        if start_date <= today_date < end_date:
            current_gameweek = key
            next_gameweek = current_gameweek + 1

            if next_gameweek > 38:
                next_gameweek = current_gameweek
    
    return current_gameweek, next_gameweek

@status_routes.route('/api/status/gameweek', methods=['GET', 'POST'])
def get_gameweek_status():
    result = {
        'Current': set_gameweek_status()[0],
        'Next': set_gameweek_status()[1]
    }

    return jsonify(result), 200