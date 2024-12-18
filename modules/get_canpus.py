def get_campus(location):
    import re,json
    import os
    file_path = os.path.join(os.path.dirname(__file__), 'campus_mapping.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        campus_mapping = json.load(f)
    match = re.match(r'(\d+)号楼', location)
    if match:
            building_number = match.group(1)
    for campus, buildings in campus_mapping.items():
        if building_number in buildings:
            return campus
    return 'Unknown Campus'

