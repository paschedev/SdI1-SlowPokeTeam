# <center>TP grupal Sistema de Integracion 1</center>
### <center>SlowPoke Team</center>


## Pasos para Trabajar en Equipo sin Conflictos

Para asegurar una colaboración fluida y minimizar los conflictos al fusionar código, te pedimos seguir los siguientes pasos:

**1. Crear una rama (branch) personal:**

Cada integrante del equipo debe trabajar en una rama individual. Esto aísla los cambios y permite que cada uno trabaje sin interferir con el trabajo de los demás.

Para crear tu propia rama, utiliza el siguiente comando en tu terminal (asegúrate de estar en la raíz del repositorio local):

```bash
git checkout -b tu_nombre_de_rama
```

Reemplaza "tu_nombre_de_rama" con un nombre descriptivo para la rama, en este caso usaremos nuestros nombres. Ej: kary.

**2. Realizar cambios y commits en tu rama:**

Una vez que estés en tu rama, realiza los cambios necesarios en los archivos. Guarda los cambios localmente utilizando el siguiente comando:

```bash
git add .
git commit -m "Descripción clara de los cambios realizados"
```

**3. Mantener tu rama local actualizada con la rama principal (main):**

Antes de enviar tus cambios (push) y crear un Pull Request, es crucial asegurarse de que tu rama local esté actualizada con los últimos cambios de la rama principal (main). Esto ayuda a prevenir o resolver conflictos de manera temprana.

Sigue estos pasos para actualizar tu rama:

&nbsp;&nbsp;**a. Cambia a la rama principal:**
```bash
git checkout main
```
&nbsp;&nbsp;**b. Descarga los últimos cambios de la rama principal del repositorio remoto:**
```bash
git pull origin main
```
&nbsp;&nbsp;**c. Vuelve a tu rama personal:**
```bash
git checkout tu_nombre_de_rama
```
&nbsp;&nbsp;**d. Fusiona los cambios de la rama principal en tu rama personal:**
```bash
git merge main
```

Si hay conflictos, Git te informará. Deberás resolver los conflictos editando los archivos afectados y luego ejecutar:
```bash
git add .
git commit -m "Resolución de conflictos al fusionar con main"
```

**4. Enviar tus cambios al repositorio remoto (push):**
Una vez que tu rama local esté actualizada y hayas realizado tus commits, puedes enviar tus cambios al repositorio remoto:

```bash
git push origin tu_nombre_de_rama
```

**5. Crear un Pull Request (PR):**
Después de hacer push de tu rama al repositorio remoto, ve al repositorio del proyecto. Allí encontrarás la opción para crear un nuevo "Pull Request" (o "Solicitud de Fusión").

a. Selecciona la rama que quieres fusionar (tu rama personal) con la rama principal (main).
b. Escribe un título descriptivo para tu Pull Request.
c. Proporciona una descripción detallada de los cambios que estás proponiendo. Explica el propósito de tu trabajo, los cambios realizados y cualquier consideración importante.
d. Asigna revisores (otros miembros del equipo) para que revisen tu código.

**6. Revisión y Discusión:**

Los miembros del equipo revisarán tu código, podrán hacer comentarios y sugerencias. Participa activamente en la discusión y realiza los cambios necesarios en tu rama respondiendo a los comentarios.

**7. Fusionar el Pull Request:**

Una vez que tu Pull Request haya sido revisado y aprobado, uno de los miembros del equipo con permisos de fusión podrá integrar tus cambios a la rama principal (main).