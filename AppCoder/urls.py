from django.urls import path
from AppCoder.views import *
urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos/', lista_cursos),
    path('', inicio, name='Inicio'),
    path('cursos/', cursos, name='Cursos'),
    path('profesores/', profesores, name='Profesores'),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('entregables/', entregables, name='Entregables'),
    path('curso-formulario/', curso_formulario, name='CursoFormulario'),
    path('busqueda-camada/', busqueda_camada, name='BusquedaCamada'),
    path('buscar/', buscar, name='BuscarCurso'),
    path('lista-profesores/', lista_profesores, name='ListaProfesores'),
    path('crea-profesor/', crea_profesor, name='CreaProfesor'),
    path('elimina-profesor/<int:id>', eliminar_profesor, name='EliminaProfesor'),
    path('edita-profesor/<int:id>', editar_profesor, name='EditaProfesor'),
    path('lista-curso/', CursoList.as_view(), name='ListaCursos'),
    path('detalle-curso/<pk>', CursoDetail.as_view(), name='DetalleCurso'),
    path('crea-curso/', CursoCreate.as_view(), name='CreaCurso'),
    path('actualiza-curso/<pk>', CursoUpdate.as_view(), name='ActualizaCurso'),
    path('elimina-curso/<pk>', CursoDelete.as_view(), name='EliminaCurso'),
]
