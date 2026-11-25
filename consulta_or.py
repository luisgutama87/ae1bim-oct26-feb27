from sqlalchemy import or_
from crear_base_entidades import Consultorio, Session

# Consultorios de Cirugía o Dermatología.
with Session() as session:
    consultorios = session.query(Consultorio).filter(
        or_(Consultorio.especialidad == 'Cirugía',
            Consultorio.especialidad == 'Dermatología')
    ).all()

    print('CONSULTORIOS DE CIRUGÍA O DERMATOLOGÍA')
    for consultorio in consultorios:
        print(f'{consultorio} | Clínica: {consultorio.clinica.nombre}')
