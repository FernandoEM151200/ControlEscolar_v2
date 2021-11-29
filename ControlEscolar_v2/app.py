from flask import Flask, render_template, request, flash, redirect, abort, url_for
from flask_bootstrap import Bootstrap
from modelo.DAO import db, Carreras, Grupo,Periodo,Usuario
from flask_login import LoginManager, current_user,login_required,login_user,logout_user
app=Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://userControlEscolar:Hola.123@localhost/ControlEscolar'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='cl4v3'

#login yoo}
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'
@login_manager.user_loader
def load_user(id):
    return Usuario.query.get(int(id))
#-----------------------------------------------------------------------------------------------------------------------------#
#Sección para las rutas de login
#-----------------------------------------------------------------------------------------------------------------------------#
@app.route('/Comunes/login', methods=['post'])
def validarUsuario():
    user=Usuario()
    mail=request.form['email']
    contraseña = request.form['password']
    user=user.validar(mail,contraseña)
    if user!= None:
        login_user(user)
        return render_template('comunes/index.html')
    else:
        flash('Datos incorrectos')
        return render_template('Comunes/login.html')



@app.route('/')
def login():
    return render_template('Comunes/login.html')

#-----------------------------------------------------------------------------------------------------------------------------#
#Sección para las rutas de INDEX
#-----------------------------------------------------------------------------------------------------------------------------#

@app.route('/')
@login_required
def inicio():
    #return '<h1> Bienvenido a la tienda en línea SHOPITESZ </h1>'
    return render_template('comunes/index.html')

@app.route('/index')
def principal():
    #return '<h1> Bienvenido a la tienda en línea SHOPITESZ </h1>'
    return render_template('comunes/index.html')

#-----------------------------------------------------------------------------------------------------------------------------#
#Fin de sección
#-----------------------------------------------------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------------------------------------------------#
#Sección para las rutas de ALUMNOS
#-----------------------------------------------------------------------------------------------------------------------------#


@app.route('/Alumnos/Nuevo')
def AlumnosNuevo():
    return render_template('Alumnos/Nuevo.html')

@app.route('/Alumnos/Consulta')
def AlumnosConsulta():
    return render_template('Alumnos/Consulta.html')

#-----------------------------------------------------------------------------------------------------------------------------#
#Fin de sección
#-----------------------------------------------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------------------------------------------#
#Seccion para las rutas de CARRERAS
#-----------------------------------------------------------------------------------------------------------------------------#


@app.route('/Carreras')
def carreras():
    c=Carreras()
    carreras=c.consultaGeneral()
    return render_template('Carreras/Consulta.html', carreras=carreras)


@app.route('/carreras/nuevo')
@login_required
def nuevaCarrera():

    return render_template('Carreras/Nuevo.html')

@app.route('/carreras/agregar', methods=['post'])
def agregarCarrera():
    c=Carreras()
    c.nombre=request.form['nombre']
    c.siglas=request.form['siglas']
    c.especialidad=request.form['especialidad']
    c.creditos=request.form['creditos']
    c.insertar()
    flash('¡Carrera registrada con éxito!')
    return render_template('Carreras/Nuevo.html')

@app.route('/carreras/ver/<int:id>')
def consultarCarreras(id):
    c=Carreras()
    return render_template('Carreras/Modificar.html', carreras=c.consultaIndividual(id))

@app.route('/carreras/guardar', methods=['post'])
def modificarCarreras():
    c=Carreras()
    c.idCarrera = request.form['id']
    c.nombre = request.form['nombre']
    c.siglas = request.form['siglas']
    c.especialidad = request.form['especialidad']
    c.creditos = request.form['creditos']
    c.actualizar()
    flash('¡Carrera editada con éxito!')
    return render_template('Carreras/Modificar.html', carreras=c)

@app.route('/carreras/eliminar/<int:id>')
def eliminarCarreras(id):
    c=Carreras()
    c.eliminar(id)
    flash('¡Carrera eliminada con éxito!')
    return redirect(url_for('carreras'))
#-----------------------------------------------------------------------------------------------------------------------------#
#Fin de sección
#-----------------------------------------------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------------------------------------------#
#Sección para rutas GRUPOS
#-----------------------------------------------------------------------------------------------------------------------------#
#@app.route('/grupos/<int:id>')
#def listarGrupos(id):
    #g=Grupo()
    #g=g.consultaIndividual(id)
    #return g.descripcion+'     '+g.periodos.nombre+'      '+g.carreras.nombre

@app.route('/Grupos')
def grupos():
    g=Grupo()
    grupos=g.consultaGeneral()
    return render_template('Grupo/Consulta.html', grupos=grupos)



@app.route('/grupos/nuevo')
def nuevoGrupo():
    p = Periodo()
    c = Carreras()
    return render_template('Grupo/Nuevo.html', periodo=p.consultaGeneral(),carreras=c.consultaGeneral())

@app.route('/grupos/agregar', methods=['post'])
def agregarGrupo():
    g=Grupo()
    g.idPeriodo=request.form['periodo']
    g.idCarrera=request.form['carrera']
    g.descripcion=request.form['descripcion']
    g.semestre=request.form['semestre']
    g.grupo=request.form['grupo']
    g.insertar()
    flash('¡Grupo registrado con éxito!')
    return render_template('/Grupo/Nuevo.html')

@app.route('/grupos/ver/<int:id>')
def consultarGrupo(id):
    g = Grupo()
    p = Periodo()
    c = Carreras()
    return render_template('Grupo/Modificar.html', grupos=g.consultaIndividual(id), periodo=p.consultaGeneral(),carreras=c.consultaGeneral())



@app.route('/grupos/guardar', methods=['post'])
def editarGrupo():
    g=Grupo()
    g.idGrupo=request.form['id']
    g.idPeriodo=request.form['periodo']
    g.idCarrera=request.form['carrera']
    g.descripcion=request.form['descripcion']
    g.semestre=request.form['semestre']
    g.grupo=request.form['grupo']
    g.actualizar()
    flash('¡Grupo editado con éxito!')
    return render_template('/Grupo/Modificar.html', grupos=g)

@app.route('/grupos/eliminar/<int:id>')
def eliminarGrupos(id):
    g=Grupo()
    g.eliminar(id)
    flash('¡Grupo eliminado con éxito!')
    return  redirect(url_for('grupos'))






#-----------------------------------------------------------------------------------------------------------------------------#
#Fin de sección
#-----------------------------------------------------------------------------------------------------------------------------#


if __name__=='__main__':
    db.init_app(app)
    app.run(port=2000, debug=True,)

