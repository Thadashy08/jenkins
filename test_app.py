from app import calcular_salario
import unittest
import time

class TestCalcularSalario(unittest.TestCase):

    def test_01_tipo_contrato_invalido(self):
        with self.assertRaises(ValueError):
            calcular_salario("invalido", 40, 0, 0, 0)

    def test_02_horas_trabajadas_cero(self):
        resultado = calcular_salario("docente_tc", 0, 0, 0, 0)
        self.assertEqual(resultado["Salario Neto"], 0)

    def test_03_solo_horas_diurnas(self):
        resultado = calcular_salario("docente_tc", 40, 0, 0, 0)
        self.assertEqual(resultado["Salario Bruto"], 40 * 50000)

    def test_04_solo_horas_nocturnas(self):
        resultado = calcular_salario("docente_tc", 0, 20, 0, 0)
        self.assertEqual(resultado["Salario Bruto"], 20 * 70000)

    def test_05_solo_horas_dominicales(self):
        resultado = calcular_salario("docente_tc", 0, 0, 10, 0)
        self.assertEqual(resultado["Salario Bruto"], 10 * 90000)

    def test_06_solo_horas_festivas(self):
        resultado = calcular_salario("docente_tc", 0, 0, 0, 8)
        self.assertEqual(resultado["Salario Bruto"], 8 * 100000)

    def test_07_combinacion_tipos_horas(self):
        resultado = calcular_salario("docente_tc", 30, 10, 5, 5)
        esperado = (30 * 50000) + (10 * 70000) + (5 * 90000) + (5 * 100000)
        self.assertEqual(resultado["Salario Bruto"], esperado)

    def test_08_descuento_parafiscales_correcto(self):
        resultado = calcular_salario("docente_tc", 40, 0, 0, 0)
        esperado = (40 * 50000) * 0.09
        self.assertAlmostEqual(resultado["Descuento Parafiscales"], esperado)

    def test_09_horas_negativas(self):
        with self.assertRaises(ValueError):
            calcular_salario("docente_tc", -5, 0, 0, 0)

    def test_10_limite_maximo_horas(self):
        with self.assertRaises(ValueError):
            calcular_salario("docente_tc", 169, 0, 0, 0)

    def test_11_validacion_calculo_manual(self):
        resultado = calcular_salario("docente_tc", 10, 10, 10, 10)
        esperado_bruto = (10 * 50000) + (10 * 70000) + (10 * 90000) + (10 * 100000)
        self.assertEqual(resultado["Salario Bruto"], esperado_bruto)

    def test_12_descuento_aplicado_sobre_total(self):
        resultado = calcular_salario("docente_tc", 10, 10, 10, 10)
        salario_bruto = resultado["Salario Bruto"]
        self.assertEqual(resultado["Salario Neto"], salario_bruto - (salario_bruto * 0.09))

    def test_13_diferencia_entre_contratos(self):
        resultado_tc = calcular_salario("docente_tc", 20, 0, 0, 0)
        resultado_mc = calcular_salario("docente_mc", 20, 0, 0, 0)
        self.assertNotEqual(resultado_tc["Salario Neto"], resultado_mc["Salario Neto"])

    def test_14_no_tarifas_incorrectas(self):
        resultado = calcular_salario("docente_tc", 40, 0, 0, 0)
        self.assertEqual(resultado["Salario Bruto"], 40 * 50000)

    def test_15_consistencia_resultados(self):
        r1 = calcular_salario("docente_tc", 10, 10, 10, 10)
        r2 = calcular_salario("docente_tc", 10, 10, 10, 10)
        self.assertEqual(r1, r2)

    def test_16_valores_extremos(self):
        resultado = calcular_salario("docente_tc", 60, 40, 30, 38)  # total = 168 horas
        self.assertIsInstance(resultado["Salario Neto"], (int, float))

    def test_17_limite_cambio_tarifa(self):
        resultado_39 = calcular_salario("docente_tc", 39, 0, 0, 0)
        resultado_40 = calcular_salario("docente_tc", 40, 0, 0, 0)
        self.assertNotEqual(resultado_39["Salario Bruto"], resultado_40["Salario Bruto"])

    def test_18_entrada_caracteres_invalidos(self):
        with self.assertRaises(TypeError):
            calcular_salario("docente_tc", "cuarenta", 0, 0, 0)

    def test_19_estructura_salida(self):
        resultado = calcular_salario("docente_tc", 10, 10, 10, 10)
        self.assertIn("Salario Bruto", resultado)
        self.assertIn("Descuento Parafiscales", resultado)
        self.assertIn("Salario Neto", resultado)

    def test_20_rendimiento(self):
        inicio = time.time()
        for _ in range(1000):
            calcular_salario("docente_tc", 10, 10, 10, 10)
        fin = time.time()
        duracion = fin - inicio
        self.assertLess(duracion, 2.0)

if __name__ == '__main__':
    unittest.main()
