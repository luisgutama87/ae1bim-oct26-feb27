from datetime import date
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica, Session

# Todos los datos son ficticios y de uso académico.
with Session() as session:
    # Evita duplicar los datos de ejemplo si se vuelve a ejecutar el archivo.
    if session.query(Clinica).first() is not None:
        print('La base ya contiene clínicas. No se insertaron datos nuevos.')
    else:
        clinica1 = Clinica(nombre='Huellitas Loja', direccion='Av. Universitaria, Loja',
                           veterinario_responsable='Ana Torres')
        clinica2 = Clinica(nombre='Patitas Cuenca', direccion='Av. Solano, Cuenca',
                           veterinario_responsable='Carlos Mora')
        clinica3 = Clinica(nombre='Amigos Quito', direccion='Av. Amazonas, Quito',
                           veterinario_responsable='Elena Ruiz')

        consultorio1 = Consultorio(nombre='C01', especialidad='Medicina general', clinica=clinica1)
        consultorio2 = Consultorio(nombre='C02', especialidad='Cirugía', clinica=clinica1)
        consultorio3 = Consultorio(nombre='C03', especialidad='Dermatología', clinica=clinica2)
        consultorio4 = Consultorio(nombre='C04', especialidad='Medicina general', clinica=clinica2)
        consultorio5 = Consultorio(nombre='C05', especialidad='Cirugía', clinica=clinica3)

        veterinario1 = Veterinario(nombres='Ana', apellidos='Torres', correo='ana@example.com',
                                   licencia_profesional='VET-001', consultorio=consultorio1)
        veterinario2 = Veterinario(nombres='Luis', apellidos='Vega', correo='luis@example.com',
                                   licencia_profesional='VET-002', consultorio=consultorio1)
        veterinario3 = Veterinario(nombres='Sofía', apellidos='Luna', correo='sofia@example.com',
                                   licencia_profesional='VET-003', consultorio=consultorio2)
        veterinario4 = Veterinario(nombres='Carlos', apellidos='Mora', correo='carlos@example.com',
                                   licencia_profesional='VET-004', consultorio=consultorio3)
        veterinario5 = Veterinario(nombres='Paula', apellidos='Ríos', correo='paula@example.com',
                                   licencia_profesional='VET-005', consultorio=consultorio4)
        veterinario6 = Veterinario(nombres='Elena', apellidos='Ruiz', correo='elena@example.com',
                                   licencia_profesional='VET-006', consultorio=consultorio5)

        historia1 = HistoriaClinica(fecha_atencion=date(2026, 11, 1), diagnostico='Control general',
                                    tratamiento='Seguimiento clínico', nombre_mascota='Max', veterinario=veterinario1)
        historia2 = HistoriaClinica(fecha_atencion=date(2026, 11, 2), diagnostico='Control general',
                                    tratamiento='Seguimiento clínico', nombre_mascota='Luna', veterinario=veterinario1)
        historia3 = HistoriaClinica(fecha_atencion=date(2026, 11, 3), diagnostico='Gastritis',
                                    tratamiento='Plan veterinario registrado', nombre_mascota='Rocky', veterinario=veterinario2)
        historia4 = HistoriaClinica(fecha_atencion=date(2026, 11, 4), diagnostico='Revisión posoperatoria',
                                    tratamiento='Seguimiento clínico', nombre_mascota='Nala', veterinario=veterinario3)
        historia5 = HistoriaClinica(fecha_atencion=date(2026, 11, 5), diagnostico='Control general',
                                    tratamiento='Seguimiento clínico', nombre_mascota='Toby', veterinario=veterinario2)
        historia6 = HistoriaClinica(fecha_atencion=date(2026, 11, 6), diagnostico='Dermatitis',
                                    tratamiento='Plan veterinario registrado', nombre_mascota='Milo', veterinario=veterinario4)
        historia7 = HistoriaClinica(fecha_atencion=date(2026, 11, 7), diagnostico='Dermatitis',
                                    tratamiento='Seguimiento clínico', nombre_mascota='Bella', veterinario=veterinario4)
        historia8 = HistoriaClinica(fecha_atencion=date(2026, 11, 8), diagnostico='Control general',
                                    tratamiento='Seguimiento clínico', nombre_mascota='Coco', veterinario=veterinario5)

        # Las relaciones incorporan los objetos dependientes por cascada save-update.
        session.add_all([clinica1, clinica2, clinica3])
        session.commit()
        print('Datos de ejemplo almacenados correctamente.')
