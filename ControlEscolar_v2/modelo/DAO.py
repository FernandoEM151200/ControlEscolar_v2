from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Date
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


