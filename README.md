# Red de clínicas veterinarias

Práctica académica de Python, SQLite y SQLAlchemy ORM.

## Modelo
Clinica (1:N) Consultorio (1:N) Veterinario (1:N) HistoriaClinica.
Las claves foráneas son obligatorias. La ciudad se incluye en la dirección y el responsable se guarda como nombre, de acuerdo con el enunciado. La licencia profesional se define como única. Los datos de prueba son ficticios y no constituyen recomendaciones veterinarias.

## Ejecución local en Windows (PowerShell)
Desde la raíz del repositorio clonado:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install sqlalchemy
python crear_base_entidades.py
python poblar_base.py
python consulta_all.py
python consulta_filter.py
python consulta_order_by.py
python consulta_or.py
python consulta_and.py
```

La base `veterinarias.db` se crea en el directorio de trabajo. Ejecutar siempre desde la raíz. El poblador no agrega datos si ya existen clínicas. Se recomienda no versionar `.venv/` ni `__pycache__/`. 

## Resultados de ejemplo
- 3 clínicas, 5 consultorios, 6 veterinarios y 8 historias clínicas.
- `all`: Huellitas Loja (5), Patitas Cuenca (3), Amigos Quito (0).
- `filter`: C01 y C04.
- `order_by`: Luna, Mora, Ruiz, Ríos, Torres, Vega (orden SQLite por defecto).
- `or_`: C02, C03 y C05.
- `and_`: Toby y Coco.

Los mínimos de hijos por entidad (por ejemplo, al menos un veterinario por consultorio) se satisfacen en los datos de prueba; una clave foránea obligatoria garantiza el padre de cada hijo, no el mínimo de hijos del padre. No se implementa una aplicación de altas/bajas ni validación de ese mínimo en todas las transacciones, porque no se solicita.

## Referencias de aprendizaje
- https://github.com/taw-desarrollo-plataformas-web/ae1bim-oct26-feb27
- https://github.com/taw-desarrollo-plataformas-web/ejemplos3.5_1
- https://github.com/taw-desarrollo-plataformas-web/EjemploSqlAlchemy-05
- https://docs.sqlalchemy.org/
