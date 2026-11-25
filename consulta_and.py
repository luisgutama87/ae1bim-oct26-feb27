from datetime import date
from sqlalchemy import and_
from crear_base_entidades import HistoriaClinica, Session

# Historias con diagnóstico Control general Y fecha desde el 5 de noviembre.
with Session() as session:
    historias = session.query(HistoriaClinica).filter(
        and_(HistoriaClinica.diagnostico == 'Control general',
             HistoriaClinica.fecha_atencion >= date(2026, 11, 5))
    ).all()

    print('HISTORIAS DE CONTROL GENERAL DESDE EL 05/11/2026')
    for historia in historias:
        print(historia)
