from flask import Flask, render_template, request, flash, redirect, abort, url_for
from flask_bootstrap import Bootstrap
from modelo.DAO import db, Carreras, Grupo, Periodo, Usuarios, Alumnos, Docentes, Coordinador
app=Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://userControlEscolar:Hola.123@localhost/ControlEscolar'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='cl4v3'

########################################################################################################################
#Sección INDEX


@app.route('/')
def inicio():
    return render_template('comunes/index.html')

@app.route('/index')
def principal():
    return render_template('comunes/index.html')


#Fin
########################################################################################################################
########################################################################################################################
#Sección ALUMNOS



@app.route('/Alumnos/NuevoUsers')
def AlumnosNuevoUsers():
    return render_template('Alumnos/NuevosUsers.html')

@app.route('/Alumnos/Consulta')
def AlumnosConsulta():
    a=Alumnos()
    alumnos=a.consultaGeneral()
    return render_template('Alumnos/Consulta.html', alumnos=alumnos)


@app.route('/Alumnos/agregar', methods=['post'])
def alumnosAgregar():
    a=Alumnos()
    a.idUsuario=request.form['usuario']
    a.idCarrera=request.form['carrera']
    a.anioIngreso=request.form['anioIngreso']
    a.insertar()
    flash('¡Registro Completo!')
    return redirect(url_for('AlumnosNuevoUsers'))


@app.route('/Alumnos/Nuevo')
def AlumnosNuevo():
    u = Usuarios()
    c = Carreras()
    return render_template('Alumnos/Nuevo.html', usuarios=u.consultaGeneral(), carreras=c.consultaGeneral())


@app.route('/Alumnos/ver/<int:id>')
def consultarAlumno(id):
    a= Alumnos()
    c= Carreras()
    u= Usuarios()
    return render_template('/Alumnos/Modificar.html', alumnos=a.consultaIndividual(id),carreras=c.consultaGeneral(), usuarios=u.consultaIndividual(id))

@app.route('/Alumnos/guardar' ,methods=['post'])
def modificarAlumno():
    a=Alumnos()
    u=Usuarios()

    u.idUsuario= request.form['usuario']
    u.nombre = request.form['nombre']
    u.sexo = request.form['sexo']
    u.telefono = request.form['telefono']
    u.email = request.form['email']
    u.contraseña = request.form['contraseña']
    u.tipo = request.form['tipo']
    estatus= request.values.get('estatus', False)

    if estatus =="True":
        u.estatus=True
    else:
        u.estatus=False

    u.actualizar()


    a.noControl=request.form['noControl']
    a.idUsuario=request.form['usuario']
    a.idCarrera=request.form['carrera']
    a.anioIngreso=request.form['anioIngreso']
    a.actualizar()


    flash('¡Alumno actualizado con éxtio!')

    return redirect(url_for('AlumnosConsulta'))

@app.route('/Alumnos/eliminar/ <int:id>')
def eliminarAlumnos(id):
    u=Usuarios()
    a=Alumnos()
    a.eliminar(id)
    u.eliminar(id)
    flash('¡Alumno eliminado con éxto!')
    return redirect(url_for('AlumnosConsulta'))


#Fin
########################################################################################################################
########################################################################################################################
#SECCIÓN DOCENTES

@app.route('/Docente/Consulta')
def docentesConsulta():
    d=Docentes()
    docentes=d.consultaGeneral()
    return render_template('Docentes/Consulta.html', docentes=docentes)

@app.route('/Docentes/NuevoUsers')
def DocentesNuevoUsers():
    return render_template('Docentes/NuevosUsers.html')

@app.route ('/Docentes/Nuevo')
def docentesNuevo():
    u = Usuarios()
    c = Carreras()
    return render_template('Docentes/Nuevo.html', usuarios=u.consultaGeneral(), carreras=c.consultaGeneral())

@app.route('/Docentes/agregar', methods=['post'])
def docentesAgregar():
    d=Docentes()
    d.idUsuario=request.form['usuario']
    d.idCarrera=request.form['carrera']
    d.anioIngreso=request.form['anioIngreso']
    d.escolaridad=request.form['escolaridad']
    d.especialidad=request.form['especialidad']
    d.cedula=request.form['cedula']
    d.insertar()
    flash('¡Registro Completo!')
    return redirect(url_for('DocentesNuevoUsers'))

@app.route('/Docentes/ver/<int:id>')
def consultarDocente(id):
    d= Docentes()
    c= Carreras()
    u= Usuarios()
    return render_template('/Docentes/Modificar.html', docentes=d.consultaIndividual(id),carreras=c.consultaGeneral(), usuarios=u.consultaIndividual(id))

@app.route('/Docentes/guardar' ,methods=['post'])
def modificarDocente():
    d=Docentes()
    u=Usuarios()

    u.idUsuario= request.form['usuario']
    u.nombre = request.form['nombre']
    u.sexo = request.form['sexo']
    u.telefono = request.form['telefono']
    u.email = request.form['email']
    u.contraseña = request.form['contraseña']
    u.tipo = request.form['tipo']
    estatus= request.values.get('estatus', False)

    if estatus =="True":
        u.estatus=True
    else:
        u.estatus=False

    u.actualizar()


    d.noDocente=request.form['noDocente']
    d.idUsuario=request.form['usuario']
    d.idCarrera=request.form['carrera']
    d.anioIngreso=request.form['anioIngreso']
    d.escolaridad=request.form['escolaridad']
    d.especialidad= request.form['especialidad']
    d.cedula=request.form['cedula']
    d.actualizar()


    flash('¡Docente actualizado con éxtio!')

    return redirect(url_for('docentesConsulta'))

#Fin
########################################################################################################################
########################################################################################################################
#Sección Coordinador

@app.route('/Coordinador/NuevoUsers')
def CoordinadorNuevoUsers():
    return render_template('Coordinador/NuevosUsers.html')

@app.route('/Coordinador/Consulta')
def CoordinadorConsulta():
    coor = Coordinador()
    coordinador = coor.consultaGeneral()
    return render_template('Coordinador/Consulta.html', coordinador=coordinador)


@app.route ('/Coordinador/Nuevo')
def coordinadorNuevo():
    u = Usuarios()
    c = Carreras()
    return render_template('Coordinador/Nuevo.html', usuarios=u.consultaGeneral(), carreras=c.consultaGeneral())

@app.route('/Coordinador/agregar', methods=['post'])
def CoordinadorAgregar():
    co=Coordinador()
    co.idUsuario=request.form['usuario']
    co.idCarrera=request.form['carrera']
    co.fechaInicio=request.form['inicio']
    co.fechaFin=request.form['fin']
    co.insertar()
    flash('¡Registro Completo!')
    return redirect(url_for('CoordinadorNuevoUsers'))

@app.route('/Coordinador/ver/<int:id>')
def consultarCoordinador(id):
    co= Coordinador()
    c= Carreras()
    u= Usuarios()
    return render_template('/Coordinador/Modificar.html', coordinador=co.consultaIndividual(id),carreras=c.consultaGeneral(), usuarios=u.consultaIndividual(id))


@app.route('/Coordinador/guardar' ,methods=['post'])
def modificarCoordinador():
    co=Coordinador()
    u=Usuarios()

    u.idUsuario= request.form['usuario']
    u.nombre = request.form['nombre']
    u.sexo = request.form['sexo']
    u.telefono = request.form['telefono']
    u.email = request.form['email']
    u.contraseña = request.form['contraseña']
    u.tipo = request.form['tipo']
    estatus= request.values.get('estatus', False)

    if estatus =="True":
        u.estatus=True
    else:
        u.estatus=False

    u.actualizar()


    co.idCoordinador=request.form['idCoordinador']
    co.idUsuario=request.form['usuario']
    co.idCarrera=request.form['carrera']
    co.fechaInicio=request.form['inicio']
    co.fechaFin=request.form['fin']
    co.actualizar()


    flash('¡Docente actualizado con éxtio!')

    return redirect(url_for('CoordinadorConsulta'))

#Fin
########################################################################################################################
#SECCIÓN CARRERAS

@app.route('/Carreras')
def carreras():
    c=Carreras()
    carreras=c.consultaGeneral()
    return render_template('Carreras/Consulta.html', carreras=carreras)


@app.route('/carreras/nuevo')
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
    return redirect(url_for('carreras'))

@app.route('/carreras/eliminar/<int:id>')
def eliminarCarreras(id):
    c=Carreras()
    c.eliminar(id)
    flash('¡Carrera eliminada con éxito!')
    return redirect(url_for('carreras'))

#Fin
########################################################################################################################


########################################################################################################################
#Sección GRUPOS

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
    return redirect(url_for('grupos'))

@app.route('/grupos/eliminar/<int:id>')
def eliminarGrupos(id):
    g=Grupo()
    g.eliminar(id)
    flash('¡Grupo eliminado con éxito!')
    return  redirect(url_for('grupos') )


#Fin
##############################################################################################



##############################################################################################
#Sección USUARIOS


@app.route('/usuarios/agregarAos', methods=['post'])
def agregarUsuarios():
    u=Usuarios()
    u.nombre=request.form['nombre']
    u.sexo=request.form['sexo']
    u.telefono=request.form['telefono']
    u.email=request.form['email']
    u.contraseña=request.form['contraseña']
    u.tipo=request.form['tipo']
    u.insertar()
    flash('¡Datos personales registrados con éxito')
    return redirect(url_for('AlumnosNuevo'))

@app.route('/usuarios/agregarDoc', methods=['post'])
def agregarUsuariosDoc():
    u=Usuarios()
    u.nombre=request.form['nombre']
    u.sexo=request.form['sexo']
    u.telefono=request.form['telefono']
    u.email=request.form['email']
    u.contraseña=request.form['contraseña']
    u.tipo=request.form['tipo']
    u.insertar()
    flash('¡Datos personales registrados con éxito')
    return redirect(url_for('docentesNuevo'))


@app.route('/usuarios/agregarCoor', methods=['post'])
def agregarUsuariosCoor():
    u=Usuarios()
    u.nombre=request.form['nombre']
    u.sexo=request.form['sexo']
    u.telefono=request.form['telefono']
    u.email=request.form['email']
    u.contraseña=request.form['contraseña']
    u.tipo=request.form['tipo']
    u.insertar()
    flash('¡Datos personales registrados con éxito')
    return redirect(url_for('coordinadorNuevo'))


#Fin
########################################################################################################################


if __name__=='__main__':
    db.init_app(app)
    app.run(port=1000, debug=True,)

