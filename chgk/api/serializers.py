import requests


def process_packages_data() -> list:
    url = 'http://www.db.chgk.info/packages?page=1&itemsPerPage=6000'
    packages = requests.get(url).json()['hydra:member']
    right_structure_packages = []
    for package in packages:
        right_package = {'id': package['id'], 'title': package['title']}
        right_structure_packages.append(right_package)
    return right_structure_packages


def process_package_data(package_id, tour_number=''):
    url = f'http://www.db.chgk.info/packages/{package_id}'
    tours = requests.get(url).json()['tours']
    right_tours_structure = []
    for tour in tours:
        tour = {'tourNumber': tour['number'], 'questions': tour['questions']}
        right_tours_structure.append(tour)
    if tour_number:
        for tour in right_tours_structure:
            if tour['tourNumber'] == int(tour_number):
                return tour
    return right_tours_structure
