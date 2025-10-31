# address book, function to create list with info from only people in certain cities

betsy_info = {'Name': 'Betsy Foobar',
              'Phone': 'x8012',
              'Street': '1600 Grand Avenue',
              'City': 'Saint Paul',
              'State': 'MN',
              'Email': 'bfoobar@macalester.edu'}

tom_info = {'Name': 'Tom Riddle',
            'Phone': 'x8512',
            'Street': '1600 Grand Avenue',
            'City': 'Saint Paul',
            'State': 'MN',
            'Email': 'triddle@macalester.edu'}

annabelle_info = {'Name': 'Annabelle Adachi',
                  'Phone': 'x3850',
                  'Street': '20 Gregory Drive',
                  'City': 'Fairfax',
                  'State': 'CA',
                  'Email': 'aadachi@macalester.edu'}

dolly_info = {'Name': 'Dolly Parton',
            'Phone': 'x2848',
            'Street': '2700 Dollywood Parks Blvd',
            'City': 'Pigeon Forge',
            'State': 'TN',
            'Email': 'dparton@macalester.edu'}

address_book = [ betsy_info, tom_info, annabelle_info, dolly_info,
                {'Name': 'Susan Fox',
                 'Phone': 'x6553',
                 'Street': '1600 Grand Avenue',
                 'City': 'Saint Paul',
                 'State': 'MN',
                 'Email': 'fox@macalester.edu'} ]

def filter_by_city(cityName, address_book):
    new_list = []
    for name in address_book:
        if name['City'] == cityName:
            new_list.append(name)
    return new_list

print(filter_by_city("Saint Paul", address_book))