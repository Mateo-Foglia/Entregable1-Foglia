# Entrega1-Foglia

1. Si estás viendo esto, ya estás en GitHub, puntualmente en mi proyecto. Lo siguiente es copiar el link en la opción desplegable que dice "Code".

2. Abrir una carpeta vacía en tu computadora, seleccionar la ruta y escribir "cmd" donde dicha ruta se encontraría. Una vez abierta la terminal escribir "git clone *link anteriormente copiado*".

3. Ahora hay que abrir VSC u otro entorno y abrir la carpeta en la que se clonó el repositorio de GitHub en el entorno.

4. Una vez abierta, abrimos la terminal usando la hotkey "ctrl+j" y allí escribimos (luego de chequear que estemos en la ubicación correcta) "python manage.py runserver".

5. Abrimos internet y escribimos el enlace "localhost:8000/AppPagEntreg" para ir a la página de inicio desde la cual podemos acceder al resto de funcionalidades de la página.

6. En caso de querer acceder al superusuario de Django, escribimos "localhost:8000/admin" y usamos como cuenta y contraseña la ya creada que es "admin" como cuenta, y "1234" como contraseña.

7. En caso de no poder usar ese superusuario por ser local (lo cual desconozco), debermos crear uno. Esto lo hacemos desde la terminal de VSC escribiendo "python manage.py createsuperuser" y siguiendo los pasos que ahí se nos indica.