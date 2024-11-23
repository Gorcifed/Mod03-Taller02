from flask import jsonify, Blueprint, render_template, current_app
from models.huron import Huron
from models.perro import Perro
from models.gato import Gato
from models.boaConstrictor import BoaConstrictor

animales_blueprint = Blueprint('animales_bp', __name__, url_prefix="/animales")

@animales_blueprint.route('/<tipo>', methods=["GET"])
def obtener_animal(tipo):
    animal = None
    if tipo == "huron":
        animal = Huron("Pepe", 5, 5.2, "Zambia", 210.0)
    elif tipo == "boa":
        animal = BoaConstrictor("Margarita", 8, 4.2, "Brasil", 2500.0)
    elif tipo == "gato":
        animal = Gato("Felix", 3, 2.2)
    elif tipo == "perro":
        animal = Perro("Lazzie", 8, 14.5)

    if animal == None:
        return "Tipo incorrecto", 400

    animal.sonido = animal.hacer_sonido();
    data = {
        "data": animal.serializar()
    }

    return jsonify(data)

@animales_blueprint.route('/<tipo>/sonido', methods=["GET"])
def obtener_sonido_animal(tipo):
    animal = None
    if tipo == "huron":
        animal = Huron("Pepe", 5, 5.2, "Zambia", 210.0)
    elif tipo == "boa":
        animal = BoaConstrictor("Margarita", 8, 4.2, "Brasil", 2500.0)
    elif tipo == "gato":
        animal = Gato("Felix", 3, 2.2)
    elif tipo == "perro":
        animal = Perro("Lazzie", 8, 14.5)

    if animal == None:
        return "Tipo incorrecto", 400

    data = {
        "data" : animal.hacer_sonido()
    }

    return jsonify(data)