def get_campus(location):
    import re
    from tkinter import filedialog
    match = re.match(r'(\d+)号楼', location)
    if match:
            building_number = match.group(1)
            if building_number in ['1', '2', '3', '4', '5', '6', '7', '8']:
                return '西校区'
            elif building_number in ['9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19','20','21']:
                return '中校区'
            elif building_number in ['22', '23', '24', '25', '26', '27', '28', '29', '30', '31','32',"33"]:
                return '东校区'
            else:
                return 'Unknown Campus'