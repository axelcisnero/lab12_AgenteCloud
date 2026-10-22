import unittest
from tasks import agregar_tarea, completar_tarea, pendientes

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

    def test_pendientes_filtrar_por_categoria(self):
        tareas = []
        agregar_tarea(tareas, "Leer documentación", "Estudio")
        agregar_tarea(tareas, "Preparar laboratorio", "Laboratorio")
        agregar_tarea(tareas, "Repasar apuntes", "estudio")
        completar_tarea(tareas, 1)

        filtradas = pendientes(tareas, "ESTUDIO")
        self.assertEqual(len(filtradas), 1)
        self.assertEqual(filtradas[0]["titulo"], "Repasar apuntes")

if __name__ == "__main__":
    unittest.main()
