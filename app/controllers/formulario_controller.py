from http import HTTPStatus
from flask import redirect, render_template, request, url_for, jsonify
from ..services.formulario_services import(procesar_formulario, crear_tabla1, obtener_tabla1_por_id, obtener_todos_tabla1,eliminar_tabla1) 

def procesar_form():
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    detalle = request.form['detalle']

    procesar_formulario(nombre,descripcion,detalle)

    return redirect(url_for('form_bp.condicional_view'))

def condicional():
    registros = obtener_todos_tabla1()
    # Desempaquetar registros
    registros_desempaquetados = [(r[0], r[1].descripcion, r[2].detalle) for r in registros]
    return render_template("condicional.html", registros=registros_desempaquetados)



# Crear
def crear_tabla1_view():
    data = request.json
    nombre = data.get('nombre')
    tabla2_id = data.get('tabla2_id')
    tabla1 = crear_tabla1(nombre, tabla2_id)
    return jsonify({"id": tabla1.id, "nombre": tabla1.nombre}), 201

# Leer
def obtener_tabla1_view():
    tabla1_id = request.args.get('id')
    if tabla1_id:
        tabla1 = obtener_tabla1_por_id(tabla1_id)
        if tabla1:
            return jsonify({"id": tabla1.id, "nombre": tabla1.nombre})
        return jsonify({"error": "No encontrado"}), 404
    else:
        tabla1s = obtener_todos_tabla1()
        return jsonify([{"id": t.id, "nombre": t.nombre} for t in tabla1s])

# Actualizar
def actualizar_tabla1_view():
    data = request.json
    tabla1_id = data.get('id')
    nombre = data.get('nombre')
    tabla2_id = data.get('tabla2_id')
    tabla1 = actualizar_tabla1(tabla1_id, nombre, tabla2_id)
    if tabla1:
        return jsonify({"id": tabla1.id, "nombre": tabla1.nombre})
    return jsonify({"error": "No encontrado"}), 404

# Eliminar
def eliminar_tabla1_view(tabla1_id):
    tabla1 = eliminar_tabla1(tabla1_id)
    if tabla1:
        return jsonify({"mensaje": "Eliminado exitosamente"})
    return jsonify({"error": "No encontrado"}), 404