from crear_base_entidades import Consultorio, Session

# Consultar los consultorios de Medicina general.
with Session() as session:
    consultorios = session.query(Consultorio).filter(
        Consultorio.especialidad == 'Medicina general'
    ).all()

    print('CONSULTORIOS DE MEDICINA GENERAL')
    for consultorio in consultorios:
        print(f'{consultorio} | Clínica: {consultorio.clinica.nombre}')
