<div align="center">
<table>
    <theader>
        <tr>
            <td style="width:25%;"><img src="https://github.com/rescobedoulasalle/iw-23b/blob/main/proyecto/logo_ulasalle_2017.png?raw=true" alt="ULASALLE" style="width:20%; height:auto"/></td>
            <td>
                <span style="font-weight:bold;">UNIVERSIDAD LA SALLE</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA</span><br />
                <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE MATEMÁTICAS E INGENIERÍAS</span><br />
                <span style="font-weight:bold;">CARRERA PROFESIONAL DE INGENIERÍA DE SOFTWARE</span>
            </td>            
        </tr>
    </theader>
    <tbody>
        <tr>
        <td colspan="2"><span style="font-weight:bold;">Proyecto web</span>: Desarrollo de una red social (Crazy Challenge)</td>
        </tr>
        <tr>
        <td colspan="2"><span style="font-weight:bold;">Fecha</span>:  07/12/2023</td>
        </tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">PROYECTO WEB</span><br />
</div>


<table>
<theader>
<tr><th>INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
    <tr>
        <td>ASIGNATURA:</td><td>Ingeniería Web</td>
    </tr>
    <tr>
        <td>SEMESTRE:</td><td>VIII</td>
    </tr>
    <tr>
        <td>FECHA INICIO:</td> <td>01-Agosto-2023</td> 
        <td>FECHA FIN:</td> <td>07-Dic-2023</td>
    </tr>
    <tr>
        <td colspan="13">DOCENTE:
        <ul>
        <li>Richart Smith Escobedo Quispe - r.escobedo@ulasalle.edu.pe</li>
        </ul>
        </td>
    </<tr>
    <tr>
        <td colspan="11">GRUPO:
        <ul>
          <li>Juliana Berrios Butron</li>
          <li>Jose Grados Chuquitaype</li>
          <li>Daria Lopez Franco</li>
          <li>Bradlhy Machado Medina</li>
          <li>Jean Mamani Mota</li>
        </ul>
        </td>
    </<tr>
</tdbody>
</table>

#   WebApp con Django

[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]

[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]

##  Tipo de Sistema
    La aplicación "Crazy Challenge" es un emocionante y vibrante plataforma diseñada para brindar a los usuarios una 
    experiencia única de desafío, diversión y creatividad. Este documento describe los módulos de la aplicación y sus 
    interacciones, estableciendo las bases para un entendimiento más profundo de su arquitectura y funcionamiento.

##  Requisitos del sistema
    El sistema debe satisfacer los siguientes requisitos funcionales y no funcionales:

    REQUISITOS FUNCIONALES (RQF)
    - RQF01 : Registro y Autenticación
      • Los usuarios deben poder registrarse en la plataforma utilizando la autenticación del sistema.
      
    - RQF02 : Perfil de Usuario
      • El usuario podrá completar y/o editar la biografía de su perfil además de su avatar, preferencias e información personal.
      
    - RQF03 : Recopilación de Preferencias en el Perfil de Usuario
      • Debe haber una sección de preferencias donde los usuarios puedan seleccionar categorías, temas o etiquetas. Los usuarios 
        al iniciar sesión deben especificar sus preferencias e intereses en su perfil (mínimo 3 preferencias).
    
    - RGF04 : Chat entre Usuarios
      • Los usuarios pueden chatear de forma privada con otros usuarios que siguen.
      
    - RQF04 : Publicación de Videos y Contenido de Retos
      • Los usuarios deben poder cargar videos y fotos para mostrar cómo completaron un reto asociándolo al reto correspondiente.
      
    - RQF05 : Interacción Social
      • Los usuarios pueden postear, subir videos o desafíos.
      • Los usuarios pueden seguir a otros usuarios y ser seguidos.
      • Los usuarios pueden reaccionar a los videos de los retos con una variedad de reacciones (por ejemplo, “Cumplió”, 
        “No cumplió”, “Incompleto” ).
      • Los usuarios pueden comentar en los videos de los retos.
      
    REQUISITOS NO FUNCIONALES (RQNF)
    - RQNF01
      •
      

##  Modelo de datos
    El modelo de datos esta conformado por las siguientes entidades.

    -   Curso : En esta entidad se almacena la información de los cursos o asignaturas que se imparten en una Escuela Profesional. Ejemplo: Programación Web 2, III semestre, 02 horas teóricas, 04 horas de laboratorio, etc..
    -   Profesor : En esta entidad se almacena los datos de los profesores que se responsabilizan del avance académico en la enseñanza de los temas planificados en cada curso. Ejemplo: Richart Escobedo, rescobedoq@unsa.edu.pe, Magister, etc.

    ...

##  Diccionario de datos

    En la construcción de software y en el diccionario de datos sobre todo se recomienda y se utilizará el idioma inglés para especificar objetos, atributos, etc.

| Course | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| code  | Numerico| No | Si | Ninguno | Código |
| name  | Cadena| No | No | Ninguno | Nombre |
...

| Teacher | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| code  | Numerico| No | Si | Ninguno | Código |
| name | Cadena| No | No | Ninguno | Nombres |
| email | Cadena| No | No | Ninguno | Correo electrónico |
| gender | Fecha| Si | No | NULL | Fecha de nacimiento |
...

##  Diagrama Entidad-Relación
    ...

##  Administración con Django
    Se muestran los pasos realizados para crear el Proyecto, la aplicación, creacion de modelos, migraciones y habilitación del panel de administración en Django.
    ...

##  Plantillas Bootstrap
    Se seleccionó la siguiente plantilla para el usuario final (No administrador).

    Demo online:
    URL: ...

    Se muestran las actividades realizadas para adecuación de plantillas, vistas, formularios en Django.
    ...

##  CRUD - Core Business - Clientes finales
    El núcleo de negocio del sistema de inscripciones tiene valor de aceptación para los cliente finales (alumnos) radica en realizar el proceso de inscripción propiamente, que empieza desde que:
    1. El alumno inicia sesión.
    2. El alumno selecciona el o los cursos donde desea realizar una inscripción.
    3. El alumno selecciona el grupo de laboatorio donde desea incribirse.
    4. El alumno puede tener la posibilidad de anular una incripción por varias razones: cambio de grupo, corregir error, etc.
    5. El alumno puede ver el consolidado de sus inscripciones.
    6. El alumno cierra sesión.

    Todas y cada una de estas pantallas debe funcionar en la plantilla bootstrap.
    A continuación se muestran las actividades realizadas para su construcción:
    ...

##  Servicios mediante una API RESTful
    Se ha creado una aplicación que pondra a disposición cierta información para ser consumida por otros clientes HTTP.
    1. GET : Con el método get se devolverá la lista de cursos, grupos y horarios establecidos para que el alumno sobre todo vea esta información en cualquier otro medio. En formato JSON. 
    2. POST : Con este método se enviara el código del alumno y se devolvera sus inscripciones. En formato JSON.
    
    Ejemplo: Prueba en Página web, aplicación móvil, PDF, etc.
    Se especifican los pasos para crear el servicio RestFul
    ...

##  Operaciones asíncronas AJAX
    Se propone el uso de AJAX para realizar la asignación de carga académica a los docentes que estan registrados. Esta operación la realizará el usuario operador encargado por el DAISI.
    Se muestran los pasos necesarios a realizar.
    ....

##  Investigación: Front-End.
    - Utilizar un framework para Front-End que consuma la API Django Rest-Framework.

Github del proyecto:

URL Proyecto:

URL Playlist YouTube.
Producción de un PlayList en Youtube explicando cada una de los requerimientos.
Video 01 - Sistema - Requisitos.
Video 02 - Modelo de datos - DD - DER.
etc…


## REFERENCIAS
-   

#

[license]: https://img.shields.io/github/license/rescobedoq/pw2?label=rescobedoq
[license-file]: https://github.com/rescobedoq/pw2/blob/main/LICENSE

[downloads]: https://img.shields.io/github/downloads/rescobedoq/pw2/total?label=Downloads
[releases]: https://github.com/rescobedoq/pw2/releases/

[last-commit]: https://img.shields.io/github/last-commit/rescobedoq/pw2?label=Last%20Commit

[Debian]: https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white
[debian-site]: https://www.debian.org/index.es.html

[Git]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[git-site]: https://git-scm.com/

[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[github-site]: https://github.com/

[Vim]: https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white
[vim-site]: https://www.vim.org/

[Java]: https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white
[java-site]: https://docs.oracle.com/javase/tutorial/


[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]


[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]
