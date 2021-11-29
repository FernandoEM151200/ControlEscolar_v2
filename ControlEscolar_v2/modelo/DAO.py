from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from flask_login import UserMixin

db=SQLAlchemy()

#Bloque Carreras
class Carreras(db.Model):
    __tablename__='Carreras'
    idCarrera=Column(Integer, primary_key=True)
    nombre=Column(String(50), unique=True)
    siglas=Column(String(5), unique=True)
    especialidad= Column(String(100), nullable=False)
    creditos= Column(Integer, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self,id):
        return self.query.get(id)

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
            objeto=self.consultaIndividual(id)
            db.session.delete(objeto)
            db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

#Fin

#Bloque Grupos
class Grupo(db.Model):
    __tablename__='Grupo'
    idGrupo=Column(Integer,primary_key=True)
    idPeriodo=Column(Integer, ForeignKey('Periodo.idPeriodo'))
    idCarrera= Column(Integer, ForeignKey('Carreras.idCarrera'))
    descripcion=Column(String(50), nullable=False)
    semestre=Column(Integer, nullable=False)
    grupo=Column(String(1), nullable=False)

    periodos = relationship('Periodo', backref='periodos', lazy='select')
    carreras = relationship('Carreras', backref='carreras', lazy='select')

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self,id):
        return self.query.get(id)

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
            objeto=self.consultaIndividual(id)
            db.session.delete(objeto)
            db.session.commit()

    def consultaGeneral(self):
        return self.query.all()



#Fin


#Bloque Periodos
class Periodo(db.Model):
  __tablename__='Periodo'
  idPeriodo=Column(Integer , primary_key=True)
  nombre=Column(String(100), nullable=False)
  fechaInicio=Column(Date, nullable=False)
  fechaFin=Column(Date, nullable=False)

  def insertar(self):
      db.session.add(self)
      db.session.commit()

  def consultaIndividual(self, id):
      return self.query.get(id)

  def actualizar(self):
      db.session.merge(self)
      db.session.commit()

  def eliminar(self, id):
      objeto = self.consultaIndividual(id)
      db.session.delete(objeto)
      db.session.commit()

  def consultaGeneral(self):
      return self.query.all()

#Fin
#Usuarios-login
class Usuario(UserMixin, db.Model):
    __tablename__='usuarios'
    idUsuario=Column(Integer,primary_key=True)
    nombre=Column(String(100),nullable=False)
    sexo=Column(String(1))
    telefono = Column(String(12) )
    email = Column(String(100) )
    contraseña = Column(String(20) )
    tipo = Column(String(15) )
    estatus=Column(Integer,default=1)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        objeto = self.consultaIndividual(id)
        db.session.delete(objeto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def validar(self,mail,contraseña):
        usuario=None
        usuario=self.query.filter(Usuario.email==mail,Usuario.contraseña==contraseña).first()
        return usuario
    #Metodos Perfilamiento
    def is_authenticated(self):
        return True
    def is_active(self):
        return  self.estatus
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.idUsuario
    def is_admin(self):
        if self.tipo=="administrador":
            return True
        else:
            return False
    def is_docente(self):
        if self.tipo=="docente":
            return True
        else:
            return False
    def is_coordinador(self):
        if self.tipo=="coordinador":
            return True
        else:
            return False
    def is_alumno(self):
        if self.tipo=="alumno":
            return True
        else:
            return False


#Bloque Usuarios
class Usuarios(db.Model):
    __tablename__='Usuarios'
    idUsuario= Column(Integer, primary_key=True)
    nombre= Column(String(100), nullable=False)
    sexo= Column(String(1), nullable=False)
    telefono= Column(String(12),nullable=False)
    email=Column(String(100), unique=True)
    contraseña=Column(String(20), nullable=False)
    tipo=Column(String(15), nullable=False)
    estatus=Column(Boolean,default=True)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        objeto = self.consultaIndividual(id)
        db.session.delete(objeto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()


#Fin

#Bloque Alumnos
class Alumnos (db.Model):
    __tablename__='Alumnos'
    noControl=Column(Integer, primary_key=True)
    idUsuario=Column(Integer,ForeignKey('Usuarios.idUsuario'))
    idCarrera=Column(Integer,ForeignKey('Carreras.idCarrera'))
    anioIngreso=Column(Integer, nullable=False)

    usuarios = relationship('Usuarios', lazy='select')
    carreras = relationship('Carreras',  lazy='select')

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        objeto = self.consultaIndividual(id)
        db.session.delete(objeto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()
#Fin

#Bloque Docentes
class Docentes (db.Model):
    __tablename__='Docentes'
    noDocente=Column(Integer, primary_key=True)
    idUsuario=Column(Integer, ForeignKey('Usuarios.idUsuario'))
    idCarrera=Column(Integer, ForeignKey(Carreras.idCarrera))
    anioIngreso=Column(Integer,nullable=False)
    escolaridad=Column(String(20),nullable=False)
    especialidad=Column(String(100), nullable=False)
    cedula=Column(String(10) , unique=True)

    usuarios = relationship('Usuarios', lazy='select')
    carreras = relationship('Carreras',  lazy='select')

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        objeto = self.consultaIndividual(id)
        db.session.delete(objeto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()
# Fin

#Bloque Coordinador
class Coordinador(db.Model):
    __tablename__='Coordinador'
    idCoordinador= Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey('Usuarios.idUsuario'))
    idCarrera = Column(Integer, ForeignKey(Carreras.idCarrera))
    fechaInicio=Column(Date, nullable=False)
    fechaFin= Column(Date, nullable=False)

    usuarios = relationship('Usuarios', lazy='select')
    carreras = relationship('Carreras',  lazy='select')

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        objeto = self.consultaIndividual(id)
        db.session.delete(objeto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()
#Fin