record_collection = { 
    2548: { 
        'albumTitle': 'Slippery When Wet', 
        'artist': 'Bon Jovi', 
        'tracks': ['Let It Rock', 'You Give Love a Bad Name'] 
    }, 
    2468: { 
        'albumTitle': '1999', 
        'artist': 'Prince', 
        'tracks': ['1999', 'Little Red Corvette'] 
    }, 
    1245: { 
        'artist': 'Robert Palmer', 
        'tracks': [] 
    }, 
    5439: { 
        'albumTitle': 'ABBA Gold' 
    }
}

def update_records(dictionary_record, id_tag, property_tag, value_tag):
    if property_tag != 'tracks':
        if value_tag != '':
            dictionary_record[id_tag][property_tag] = value_tag
        else:
            if property_tag in dictionary_record[id_tag]:
                del dictionary_record[id_tag][property_tag]
    else:
        if value_tag != '':
            if 'tracks' not in dictionary_record[id_tag]:
                dictionary_record[id_tag][property_tag] = [value_tag]
            else:
                dictionary_record[id_tag][property_tag].append(value_tag)
        else:
            del dictionary_record[id_tag][property_tag]
    return dictionary_record

    # if property_tag != 'tracks' and value_tag != '':
    #     dictionary_record[id_tag][property_tag] = value_tag
    # if property_tag != 'tracks' and value_tag == '':
    #     dictionary_record[id_tag][property_tag] = []
    # if property_tag == 'tracks' and value_tag != '':
    #     dictionary_record[id_tag][property_tag].append(value_tag)
    # if property_tag == 'tracks' and value_tag == '':
    #     dictionary_record[id_tag][property_tag] = []
    # if property_tag == 'tracks' and not 'track' in dictionary_record[id_tag]:
    #     dictionary_record[id_tag][property_tag] = [value_tag] if value_tag != '' else []
    # return dictionary_record
    
id_tag = int(input("input id: "))
property_tag = input("input property: ")
value_tag = input("input value: ")
record_collection = update_records(record_collection, id_tag, property_tag, value_tag)
print(record_collection)