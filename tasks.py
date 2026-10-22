def agregar_tarea(tareas, titulo, categoria):
    titulo = titulo.strip()
    if not titulo:
        raise ValueError("El título es obligatorio")
    if categoria is None:
        raise ValueError("La categoría es obligatoria")
    categoria = categoria.strip()
    if not categoria:
        raise ValueError("La categoría es obligatoria")
    tarea = {
        "id": len(tareas) + 1,
        "titulo": titulo,
        "categoria": categoria,
        "completada": False,
    }
    tareas.append(tarea)
    return tarea

def completar_tarea(tareas, tarea_id):
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            tarea["completada"] = True
            return tarea
    raise ValueError("Tarea no encontrada")

def pendientes(tareas, categoria=None):
    tareas_pendientes = [t for t in tareas if not t["completada"]]
    if categoria is None:
        return tareas_pendientes

    categoria = categoria.strip().lower()
    if not categoria:
        return tareas_pendientes

    return [t for t in tareas_pendientes if t.get("categoria", "").lower() == categoria]
