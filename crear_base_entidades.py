from sqlalchemy import create_engine, event, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

# SQLite requiere habilitar las claves foráneas en cada conexión.
@event.listens_for(engine, 'connect')
def activar_claves_foraneas(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute('PRAGMA foreign_keys=ON')
    cursor.close()

Base = declarative_base()
Session = sessionmaker(bind=engine)


class Clinica(Base):
    __tablename__ = 'clinicas'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    direccion = Column(String(200), nullable=False)
    veterinario_responsable = Column(String(100), nullable=False)

    consultorios = relationship('Consultorio', back_populates='clinica')

    def __repr__(self):
        return f'Clínica: {self.nombre} | Dirección: {self.direccion} | Responsable: {self.veterinario_responsable}'


class Consultorio(Base):
    __tablename__ = 'consultorios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    especialidad = Column(String(100), nullable=False)
    clinica_id = Column(Integer, ForeignKey('clinicas.id'), nullable=False)

    clinica = relationship('Clinica', back_populates='consultorios')
    veterinarios = relationship('Veterinario', back_populates='consultorio')

    def __repr__(self):
        return f'Consultorio: {self.nombre} | Especialidad: {self.especialidad}'


class Veterinario(Base):
    __tablename__ = 'veterinarios'

    id = Column(Integer, primary_key=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(150), nullable=False)
    licencia_profesional = Column(String(50), nullable=False, unique=True)
    consultorio_id = Column(Integer, ForeignKey('consultorios.id'), nullable=False)

    consultorio = relationship('Consultorio', back_populates='veterinarios')
    historias_clinicas = relationship('HistoriaClinica', back_populates='veterinario')

    def __repr__(self):
        return f'Veterinario: {self.nombres} {self.apellidos} | Licencia: {self.licencia_profesional}'


class HistoriaClinica(Base):
    __tablename__ = 'historias_clinicas'

    id = Column(Integer, primary_key=True)
    fecha_atencion = Column(Date, nullable=False)
    diagnostico = Column(String(200), nullable=False)
    tratamiento = Column(String(300), nullable=False)
    nombre_mascota = Column(String(100), nullable=False)
    veterinario_id = Column(Integer, ForeignKey('veterinarios.id'), nullable=False)

    veterinario = relationship('Veterinario', back_populates='historias_clinicas')

    def __repr__(self):
        return f'Historia clínica: {self.nombre_mascota} | Fecha: {self.fecha_atencion} | Diagnóstico: {self.diagnostico} | Tratamiento: {self.tratamiento}'


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    print('Base de datos y tablas creadas correctamente.')
