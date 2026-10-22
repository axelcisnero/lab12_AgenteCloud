import unittest
from tasks import agregar_tarea, completar_tarea, eliminar_tarea, pendientes

class TestTasks(unittest.TestCase):
    def test_agregar_tarea(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación", "Estudio")
        self.assertEqual(tarea["titulo"], "Leer documentación")
        self.assertEqual(tarea["categoria"], "Estudio")
        self.assertFalse(tarea["completada"])

    def test_completar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Practicar", "Laboratorio")
        completar_tarea(tareas, 1)
        self.assertEqual(pendientes(tareas), [])

    def test_agregar_tarea_categoria_vacia(self):
        tareas = []
        with self.assertRaises(ValueError):
            agregar_tarea(tareas, "Leer documentación", "   ")

    def test_agregar_tarea_categoria_none(self):
        tareas = []
        with self.assertRaisesRegex(ValueError, "La categoría es obligatoria"):
            agregar_tarea(tareas, "Titulo", None)

    def test_pendientes_filtrar_por_categoria(self):
        tareas = []
        agregar_tarea(tareas, "Leer documentación", "Estudio")
        agregar_tarea(tareas, "Preparar laboratorio", "Laboratorio")
        agregar_tarea(tareas, "Repasar apuntes", "estudio")
        completar_tarea(tareas, 1)

        filtradas = pendientes(tareas, "ESTUDIO")
        self.assertEqual(len(filtradas), 1)
        self.assertEqual(filtradas[0]["titulo"], "Repasar apuntes")

    def test_pendientes_categoria_inexistente(self):
        tareas = []
        agregar_tarea(tareas, "Leer documentación", "Estudio")
        agregar_tarea(tareas, "Preparar laboratorio", "Laboratorio")

        filtradas = pendientes(tareas, "Personal")
        self.assertEqual(filtradas, [])

    def test_pendientes_categoria_solo_espacios(self):
        tareas = []
        agregar_tarea(tareas, "Leer documentación", "Estudio")
        agregar_tarea(tareas, "Preparar laboratorio", "Laboratorio")
        completar_tarea(tareas, 2)

        todas = pendientes(tareas)
        filtradas = pendientes(tareas, "   ")
        self.assertEqual(filtradas, todas)

    def test_eliminar_tarea_existente(self):
        tareas = []
        agregar_tarea(tareas, "Leer documentación", "Estudio")
        agregar_tarea(tareas, "Preparar laboratorio", "Laboratorio")

        eliminada = eliminar_tarea(tareas, 1)
        self.assertEqual(eliminada["id"], 1)
        self.assertEqual(len(tareas), 1)
        self.assertEqual(tareas[0]["id"], 2)
        self.assertEqual(tareas[0]["titulo"], "Preparar laboratorio")

    def test_eliminar_tarea_inexistente(self):
        tareas = []
        agregar_tarea(tareas, "Leer documentación", "Estudio")

        with self.assertRaisesRegex(ValueError, "Tarea no encontrada"):
            eliminar_tarea(tareas, 99)

    def test_agregar_tarea_tras_eliminar_no_repite_id(self):
        tareas = []
        agregar_tarea(tareas, "Tarea 1", "Estudio")
        agregar_tarea(tareas, "Tarea 2", "Laboratorio")
        eliminar_tarea(tareas, 1)

        nueva = agregar_tarea(tareas, "Tarea 3", "Estudio")
        self.assertEqual(nueva["id"], 3)
        self.assertEqual([t["id"] for t in tareas], [2, 3])

if __name__ == "__main__":
    unittest.main()
