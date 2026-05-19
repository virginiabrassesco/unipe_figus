import random
from album_figus import (
    crear_figus_totales,
    mezclar_figus,
    crear_album_vacio,
    esta_completo_el_album,
    comprar_figus_hasta_completar_album,
    simular_completar_album,
    simular_muchas_personas_completar
)


class TestCrearFigusTotales:
    """Pruebas para la función crear_figus_totales"""

    def test_un_mazo_cinco_cartas(self):
        resultado = crear_figus_totales(1, 5)
        assert sorted(resultado) == sorted([1, 2, 3, 4, 5])

    def test_dos_mazos_cinco_cartas(self):
        resultado = crear_figus_totales(2, 5)
        assert sorted(resultado) == sorted([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])

    def test_tres_mazos_tres_cartas(self):
        resultado = crear_figus_totales(3, 3)
        assert sorted(resultado) == sorted([1, 2, 3, 1, 2, 3, 1, 2, 3])

    def test_un_mazo_una_carta(self):
        resultado = crear_figus_totales(1, 1)
        assert sorted(resultado) == [1]

    def test_cinco_mazos_dos_cartas(self):
        resultado = crear_figus_totales(5, 2)
        assert sorted(resultado) == sorted([1, 2] * 5)

    def test_cantidad_total_figus(self):
        mazos, total_cartas = 4, 20
        resultado = crear_figus_totales(mazos, total_cartas)
        assert len(resultado) == mazos * total_cartas


class TestMezclarFigus:
    """Pruebas para la función mezclar_figus"""

    def test_mezcla_mantiene_elementos(self):
        original = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        copia = original.copy()
        mezclar_figus(copia)
        # mismos elementos
        assert sorted(copia) == sorted(original)
        # misma longitud
        assert len(copia) == len(original)
        # al mezclar no deberían ser iguales
        assert copia != original

    def test_mezcla_modifica_lista(self):
        original = [1, 2, 3, 4, 5][::-1]
        copia = original.copy()
        mezclar_figus(copia)
        assert sorted(copia) == sorted(original)
        assert len(copia) == len(original)
        assert copia != original
        
    def test_mezcla_elementos_unicos(self):
        original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        copia = original.copy()
        mezclar_figus(copia)
        assert sorted(copia) == sorted(original)
        assert len(copia) == len(original)
        assert copia != original


class TestCrearAlbumVacio:
    """Pruebas para la función crear_album_vacio"""

    def test_tres_posiciones(self):
        album = crear_album_vacio(3)
        assert len(album) == 3
        # Debe ser todo False o todo 0
        assert all(elem is False or elem == 0 for elem in album)

    def test_una_posicion(self):
        album = crear_album_vacio(1)
        assert len(album) == 1
        assert album[0] is False or album[0] == 0

    def test_album_grande(self):
        album = crear_album_vacio(100)
        assert len(album) == 100
        assert all(elem is False or elem == 0 for elem in album)


class TestEstaCompletoElAlbum:
    """Pruebas para la función esta_completo_el_album"""

    def test_album_booleano_incompleto(self):
        album = crear_album_vacio(10)
        assert not esta_completo_el_album(album)

    def test_album_booleano_completo(self):
        album = crear_album_vacio(1)

        if isinstance(album[0], bool):
            album = [True] * 4
        else:
            album = [1] * 4

        assert esta_completo_el_album(album)

    def test_album_entero_incompleto_al_final(self):
        album = crear_album_vacio(1)

        if isinstance(album[0], bool):
            album = [True] * 4 + [False]
        else:
            album = [3] * 4 + [0]

        assert not esta_completo_el_album(album)

    def test_album_entero_incompleto_al_inicio(self):
        album = crear_album_vacio(1)

        if isinstance(album[0], bool):
            album = [False] + [True] * 4
        else:
            album = [0] + [3] * 4

        assert not esta_completo_el_album(album)


class TestComprarFigusHastaCompletarAlbum:
    """Pruebas para la función comprar_figus_hasta_completar_album"""

    def test_completar_sin_repetidas(self):
        album = crear_album_vacio(3)
        figus = [1, 2, 3]
        resultado = comprar_figus_hasta_completar_album(figus, album)
        assert resultado == 3

    def test_completar_con_repetidas(self):
        album = crear_album_vacio(3)
        figus = [1, 2, 2, 3]
        resultado = comprar_figus_hasta_completar_album(figus, album)
        assert resultado == 4

    def test_completar_muchas_repetidas(self):
        album = crear_album_vacio(2)
        figus = [1, 1, 1, 1, 2, 1]
        resultado = comprar_figus_hasta_completar_album(figus, album)
        assert resultado == 5

    def test_completar_album_con_enteros(self):
        album = crear_album_vacio(3)
        figus = [3, 1, 3, 2]
        resultado = comprar_figus_hasta_completar_album(figus, album)
        assert resultado == 4

    def test_album_ya_completo(self):
        album = crear_album_vacio(1)

        if isinstance(album[0], bool):
            album = [True] * 3
        else:
            album = [1] * 3

        figus = [1, 2, 3]
        resultado = comprar_figus_hasta_completar_album(figus, album)
        assert resultado == 0  # No compra nada


class TestSimularCompletarAlbum:
    """Pruebas para la función simular_completar_album"""

    def test_resultado_mayor_a_total_cartas(self):
        # En el unico caso que es igual a la cantidad es cuando no están mezcladas, es poco probable
        mazos, total_cartas = 2, 10
        resultado = simular_completar_album(mazos, total_cartas)
        assert resultado > total_cartas

    def test_resultado_menor_o_igual_total_figus(self):
        mazos, total_cartas = 3, 5
        total_figus = mazos * total_cartas
        resultado = simular_completar_album(mazos, total_cartas)
        assert resultado <= total_figus

    def test_un_mazo_una_figu(self):
        resultado = simular_completar_album(1, 1)
        assert resultado == 1

    def test_un_mazo_con_todas_distintas(self):
        # Con un solo mazo, debe comprar todas las figus sí o sí
        mazos, total_cartas = 1, 8
        resultado = simular_completar_album(mazos, total_cartas)
        assert resultado == total_cartas

    def test_tipo_retorno(self):
        resultado = simular_completar_album(2, 5)
        assert isinstance(resultado, int)


class TestSimularMuchasPersonasCompletar:
    """Pruebas para la función simular_muchas_personas_completar"""

    def test_devuelve_promedio_flotante(self):
        promedio = simular_muchas_personas_completar(2, 5, 10)
        assert isinstance(promedio, float)

    def test_promedio_en_rango_esperado(self):
        mazos, total_cartas = 3, 10
        total_figus = mazos * total_cartas
        promedio = simular_muchas_personas_completar(mazos, total_cartas, 20)
        assert promedio >= total_cartas
        assert promedio <= total_figus

    def test_un_mazo_una_figu_promedio(self):
        promedio = simular_muchas_personas_completar(1, 1, 5)
        assert promedio == 1.0

    def test_un_mazo_promedio_igual_total(self):
        # Con un solo mazo, siempre se compran TODAS las figus
        mazos, total_cartas = 1, 6
        promedio = simular_muchas_personas_completar(mazos, total_cartas, 10)
        assert promedio == float(total_cartas)

    def test_tres_personas_album_pequeno(self):
        # Solo verifica que ejecuta sin errores y devuelve float
        promedio = simular_muchas_personas_completar(2, 3, 3)
        assert isinstance(promedio, float)
        assert promedio >= 3.0
        assert promedio <= 6.0


class TestIntegracion:
    """Pruebas de integración que combinan múltiples funciones"""

    def test_flujo_completo(self):
        # Crear figus
        figus = crear_figus_totales(2, 5)
        assert len(figus) == 10

        # Mezclar
        mezclar_figus(figus)
        # No podemos probar el orden, pero podemos probar que sigue teniendo 10 elementos

        # Crear album
        album = crear_album_vacio(5)
        assert len(album) == 5

        # Completar
        compradas = comprar_figus_hasta_completar_album(figus, album)
        assert compradas >= 5
        assert compradas <= 10

        # Verificar completo
        assert esta_completo_el_album(album)

    def test_simulacion_coherente(self):
        """Verifica que simular_completar_album y simular_muchas_personas_completar sean coherentes"""
        mazos, total_cartas = 2, 4
        una_persona = simular_completar_album(mazos, total_cartas)
        promedio = simular_muchas_personas_completar(mazos, total_cartas, 1)
        assert una_persona == int(promedio)

    def test_determinismo_semilla(self):
        # Si fijamos la semilla, los resultados deben ser reproducibles
        random.seed(42)
        resultado1 = simular_completar_album(3, 10)
        random.seed(42)
        resultado2 = simular_completar_album(3, 10)
        assert resultado1 == resultado2


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])