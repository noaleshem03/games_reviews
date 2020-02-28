# The data for your website
#

data = {
    # Example of a collection
    "games": [
        {
            "id": '0',
            "name": 'Tekken',
            "category": 'Fighting',
            "platform": 'PlayStation',
            "rating": '9.6',
            'imageUrl': '/shared/images/Tekken.jpg'
        },
        {
            "id": '1',
            "name": 'God of War',
            "category": 'Action',
            "platform": 'PlayStation',
            "rating": '9.3',
            'imageUrl': '/shared/images/God_of_war.jpg'
        },
        {
            "id": '2',
            "name": 'Need for Speed',
            "category": 'Racing',
            "platform": 'PC',
            "rating": '8.0',
            'imageUrl': '/shared/images/Need_for_speed.jpg'
        },
        {
            "id": '3',
            "name": 'Pro Evolution Soccer',
            "category": 'Sports',
            "platform": 'PlayStation',
            "rating": '7.8',
            'imageUrl': '/shared/images/Pro_evolution.jpg'
        },
        {
            "id": '4',
            "name": 'The Last of Us',
            "category": 'Adventure',
            "platform": 'PlayStation',
            "rating": '9.1',
            'imageUrl': '/shared/images/The_last_of_us.jpg'
        },
        {
            "id": '5',
            "name": 'Fortnite',
            "category": 'Action',
            "platform": 'PC',
            "rating": '8.4',
            'imageUrl': '/shared/images/Fortnite.jpg'
        },
        {
            "id": '6',
            "name": 'Crash Bandicoot',
            "category": 'Adventure',
            "platform": 'PlayStation',
            "rating": '7.5',
            'imageUrl': '/shared/images/Crash_bandicoot.jpg'
        },
        {
            "id": '7',
            "name": 'Call of Duty',
            "category": 'Action',
            "platform": 'PlayStation',
            "rating": '8.6',
            'imageUrl': '/shared/images/Call_of_duty.jpg'
        },
        {
            "id": '8',
            "name": 'Grand Theft Auto',
            "category": 'Adventure',
            "platform": 'PlayStation',
            "rating": '9.7',
            'imageUrl': '/shared/images/GTA.jpg'
        },
        {
            "id": '9',
            "name": 'Devil May Cry',
            "category": 'Action',
            "platform": 'PC',
            "rating": '8.9',
            'imageUrl': '/shared/images/Devil_may_cry.jpg'
        },
        {
            "id": '10',
            "name": 'FIFA',
            "category": 'Sports',
            "platform": 'PlayStation',
            "rating": '9.0',
            'imageUrl': '/shared/images/FIFA.jpg'
        },
        {
            "id": '11',
            "name": 'Crysis',
            "category": 'Action',
            "platform": 'PC',
            "rating": '7.1',
            'imageUrl': '/shared/images/Crysis.jpg'
        },
    ]
}


def get_data(params):
    index = int(params.pop('_index', 0))
    length = int(params.pop('_length', 0))
    collection = params.pop('_collection')

    filtered_data = list(filter(lambda element: set(params.items()).issubset(set(element.items())),
                                data[collection]))

    return filtered_data[index:index + length] if length > 0 else filtered_data[index:]
