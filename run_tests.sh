#!/bin/bash
# Script para ejecutar las pruebas en el autograder

echo "Ejecutando pruebas del TP de Album de Figus"
echo "============================================"

# Verificar que existe el archivo del estudiante
if [ ! -f "album_figus.py" ]; then
    echo "ERROR: No se encuentra el archivo album_figus.py"
    exit 1
fi

# Ejecutar pruebas
python3 -m pytest tests/test_album_figus.py -v
# En windows quizá es python (sin el 3)

# Guardar el código de salida
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo ""
    echo "✅ TODAS LAS PRUEBAS PASARON EXITOSAMENTE"
else
    echo ""
    echo "❌ ALGUNAS PRUEBAS FALLARON"
fi

exit $EXIT_CODE
