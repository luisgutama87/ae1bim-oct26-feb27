from crear_base_entidades import Veterinario, Session

# Ordenar veterinarios alfabéticamente por apellidos y nombres.
with Session() as session:
    veterinarios = session.query(Veterinario).order_by(
        Veterinario.apellidos.asc(), Veterinario.nombres.asc()
    ).all()

    print('VETERINARIOS ORDENADOS POR APELLIDOS')
    for veterinario in veterinarios:
        print(veterinario)
