from flask import Blueprint
from ..controllers.formulario_controller import (
    condicional, 
    procesar_form, 
    crear_tabla1_view, 
    obtener_tabla1_view,
    actualizar_tabla1_view,
    eliminar_tabla1_view
)

form_bp = Blueprint('form_bp', __name__)

@form_bp.route('/condicionales')
def condicional_view():
    return condicional()

@form_bp.route('/procesar_formulario', methods=['POST'])
def procesar_form_view():
    return procesar_form()

# CRUD Routes
@form_bp.route('/tabla1/crear', methods=['POST'])
def crear_tabla1_route():
    return crear_tabla1_view()

@form_bp.route('/tabla1', methods=['GET'])
def obtener_tabla1_route():
    return obtener_tabla1_view()

@form_bp.route('/tabla1/actualizar/<int:id>', methods=['PUT'])
def actualizar_tabla1_route(id):
    return actualizar_tabla1_view(id)

@form_bp.route('/tabla1/eliminar/<int:id>', methods=['POST'])
def eliminar_tabla1_route(id):
    return eliminar_tabla1_view(id)

