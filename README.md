# Aplicación de Votación

## Credits
Based from repository [garden-io/web-app-example](https://github.com/garden-io/web-app-example)

Used for educational purposes to complete a workshop in university distributed systems course.

## Integrantes

Martin Perez Lopez y Luis Alfonso Murcia Quintero

Sistemas Distribuidos 2024-1

Universidad Icesi

## Resumen

Esta es una aplicación sencilla de votación que permite a los usuarios votar y realiza el cálculo de los votos. La aplicación sigue una arquitectura de tres capas:

- **API (Backend):** Maneja la lógica del negocio y las interacciones con la base de datos.
- **Web (Frontend):** Interfaz de usuario para que los usuarios puedan emitir sus votos.
- **Base de Datos (PostgreSQL):** Almacena los datos de los votos.

## *Características*

- **Votación en tiempo real:** Los usuarios pueden votar y ver los resultados en tiempo real.
- **Cálculo de votos:** La aplicación realiza el cálculo de los votos automáticamente.
- **Interfaz amigable:** Interfaz web intuitiva y fácil de usar.

## Tecnologías Utilizadas

- **Backend:** Python con Flask
- **Frontend:** Node.js con Vue.js
- **Base de Datos:** PostgreSQL
- **Infraestructura:** Helm y Kubernetes
- **CI/CD:** Jenkins
- **Monitorización:** Grafana y Prometheus

## *Estrategia de Branch*

Se utiliza una estrategia de branch llamada "branch by environment". Esta estrategia implica tener ramas separadas para cada entorno (desarrollo, pruebas, producción, etc.). Los cambios se integran en estas ramas específicas antes de ser promovidos al siguiente entorno.

## *Instalación y Configuración*

### Requisitos

- Node.js
- Python
- PostgreSQL
- Kubernetes
- Helm
- Jenkins
- Grafana
- Prometheus

### *Pasos de Instalación para probar la aplicación localmente*

1. **Clonar el repositorio:**
    ```sh
    git clone https://github.com/tuusuario/nombre-del-repositorio.git
    ```

2. **Backend:**
    - Navegar al directorio del backend:
      ```sh
      cd backend
      ```
    - Crear un entorno virtual e instalar dependencias:
      ```sh
      python -m venv venv
      source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
      pip install -r requirements.txt
      ```
    - Configurar la base de datos:
        ```sh
      - Crear una base de datos en PostgreSQL.
      - Actualizar el archivo `config.py` con las credenciales de la base de datos.
        ```
    - Iniciar el servidor backend:
      ```sh
      flask run
      ```

3. **Frontend:**
    - Navegar al directorio del frontend:
      ```sh
      cd ../frontend
      ```
    - Instalar dependencias:
      ```sh
      npm install
      ```
    - Iniciar el servidor frontend:
      ```sh
      npm run serve
      ```

4. **Infraestructura:**
    - Configurar y desplegar con Helm:
      ```sh
      helm install nombre-del-chart ./path-to-chart
      ```

5. **CI/CD:**
    - Configurar Jenkins con un webhook trigger en GitHub para activar CI/CD al hacer pull request desde cualquier rama hacia `main`.

## *Uso*

1. Acceder a la aplicación web en tu navegador.
2. Emitir tu voto.
3. Ver los resultados de la votación en tiempo real.

## *Monitorización*

El clúster de Kubernetes está siendo monitorizado con Grafana y Prometheus. Estas herramientas permiten visualizar métricas y realizar un seguimiento del rendimiento del sistema.

## *Contribuir*

Las contribuciones son bienvenidas. Por favor, sigue los siguientes pasos para contribuir:

1. Realiza un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-característica`).
3. Realiza los cambios y haz commit (`git commit -am 'Añadir nueva característica'`).
4. Sube los cambios a tu repositorio (`git push origin feature/nueva-característica`).
5. Crea un Pull Request.
6. El pull request dispara directamente el CI/CD que al pasar las pruebas de test e integración, hará       directamente push al repositorio sin ningún problema.

## Datos Relevantes

- Para este tipo de proyectos es necesario introducir a Jenkins al clúster de kubernetes en el cual estamos corriendo nuestra aplicación, por lo que es pertinente seguir los siguientes pasos


- **Aplicar el archivo de configuración de Jenkins:**
  - `kubectl apply -f jenkins.yaml`
  - Este comando aplica la configuración especificada en el archivo `jenkins.yaml`, creando los recursos necesarios en Kubernetes.

- **Instalar o actualizar Jenkins con Helm:**
  - `helm upgrade --install jenkins --namespace jenkins --values values.yaml jenkins/jenkins`
  - Este comando instala o actualiza Jenkins usando Helm, con los valores especificados en `values.yaml`, dentro del espacio de nombres `jenkins`.

- **Crear un ClusterRoleBinding:**
  - `kubectl create clusterrolebinding permissive-binding --clusterrole=cluster-admin --user=admin --user=kubelet --group=system:serviceaccounts`
  - Este comando crea un `ClusterRoleBinding` que otorga permisos de administrador de clúster a los usuarios `admin` y `kubelet`, así como al grupo `system:serviceaccounts`.

- **Limpiar la pantalla:**
  - `clear`
  - Este comando limpia la terminal.

- **Esperar 60 segundos para que Jenkins se inicie:**
  - `sleep 60s`
  - Este comando pausa la ejecución del script durante 60 segundos para permitir que Jenkins se inicie completamente.

- **Obtener la contraseña de administrador de Jenkins:**
  - `kubectl exec --namespace jenkins -it svc/jenkins -c jenkins -- /bin/cat /run/secrets/additional/chart-admin-password && echo`
  - Este comando ejecuta un comando dentro del contenedor de Jenkins para obtener y mostrar la contraseña de administrador almacenada en `/run/secrets/additional/chart-admin-password`.

- **Obtener información del servicio de Jenkins:**
  - `kubectl get svc -n jenkins`
  - Este comando lista los servicios en el espacio de nombres `jenkins`, proporcionando información sobre cómo acceder a Jenkins.

- Si quieres hacer tu propio proyecto y necesitas ayuda con grafana y prometheus: https://github.com/icesi-ops/training_kubernetes/blob/master/09_monitoring/01_promethetus_grafana.md

- ¿Cómo conectar Prometheus con el clúster? https://grafana.com/grafana/dashboards/315-kubernetes-cluster-monitoring-via-prometheus/


