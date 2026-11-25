from crear_base_entidades import Clinica, Session

# Presentar todas las clínicas y la cantidad de historias clínicas asociadas.
with Session() as session:
    clinicas = session.query(Clinica).all()

    print('CLÍNICAS Y NÚMERO DE HISTORIAS CLÍNICAS')
    for clinica in clinicas:
        total_historias = 0
        for consultorio in clinica.consultorios:
            for veterinario in consultorio.veterinarios:
                total_historias += len(veterinario.historias_clinicas)

        print(f'Clínica: {clinica.nombre}')
        print(f'Número de historias clínicas: {total_historias}')
        print('---------')
