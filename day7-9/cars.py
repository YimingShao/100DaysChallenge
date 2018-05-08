cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    """return a comma separated string of jeep models (original order)"""
    mystring = ', '.join(str(model) for model in cars['Jeep'])
    #mystring = mystring[:-2]
    return mystring


def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    mylist = [brand[0] for brand in cars.values()]

    return mylist


def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    mylist=[]
    for brand in cars:
        for model in cars[brand]:
            if grep.lower() in model.lower():
                mylist.append(model)
    return sorted(mylist)


def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    sortedcars = {brand:sorted(cars[brand]) for brand in cars}
    return sortedcars