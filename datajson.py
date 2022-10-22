# Download the course.json from this link https://github.com/xaviruvpadhiyar98/JSON-CRUD/blob/main/json/course.json

import json

# Load the File
def load_data():
    with open('./material.json', 'r') as f:
        ## importamos la base de datos json
        data = json.load(f)
        return data

def create_data_table():
    data = load_data()
    dataLen = len(data)


    ## creamos la lista que se converitan en nuestra columnas
    material  = []
    tipo      = []
    densidad  = []
    esfuerzo  = []
    modulo    = []
    for i in range(dataLen):
        materialList = data[i]
        material.append(materialList.get("name"))
        tipo.append(materialList.get("tipo"))
        densidad.append("{:.3e}".format(materialList.get("desidad")))
        esfuerzo.append("{:.3e}".format(materialList.get("esfuerzo")))
        modulo.append("{:.3e}".format(materialList.get("modulo")))

    ## cramos el diccionario para crear la tabla
    materialDict = {
        'material'  : material,
        'tipo'      : tipo,
        'densidad'  : densidad,
        'esfuerzo'  : esfuerzo,
        'modulo'    : modulo
    }

    return materialDict

# inlcude data to database
def include_data(data):
    json_data = load_data()
    json_data.append(data)
    save_data(json_data)

# Save the file with new data
def save_data(json_data):
    with open('./material.json', 'w') as f:
        json.dump(json_data, f, indent=4)

# Read an Item from file
def get_one_item_from_json(name):
    json_data = load_data()
    for x in json_data:
        if x['name'] == name:
            return x

# Delete One Item from Json
def delete_one_item_from_json(id):
    json_data = load_data()
    del json_data[id]
    save_data(json_data)

# Update One Item from JSON
def update_one_item_in_json(id, data):
    json_data[id] = data
    save_data(json_data)

if __name__ == '__main__':
    #print(load_data())

    sol = get_one_item_from_json("A1020")

    print(sol)
