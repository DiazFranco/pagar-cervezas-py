# Proyecto Cometa 🪁 - Prueba Técnica Fullstack

Este proyecto es una implementación de una API en Django que gestiona la creación y el estado de órdenes para un bar que vende cerveza. El objetivo es procesar las órdenes de cervezas y devolver el estado actual del pedido, manteniendo la información en memoria (sin base de datos).

## Requisitos

- Python 3.8+
- Django 4.x
- PIP para gestionar las dependencias

## Instalación

### 1. Clonar el repositorio

Primero, clonar este repositorio en tu máquina local:

```bash
git clone https://github.com/tu-usuario/cometa-proyecto.git
cd cometa-proyecto
```

### 2. Crear un entorno virtual (opcional pero recomendado)

Es recomendable usar un entorno virtual para gestionar las dependencias del proyecto. Si usas `venv`, puedes crear un entorno virtual de la siguiente manera:

```bash
python3 -m venv env
source env/bin/activate  # En Linux/macOS
env\Scripts\activate     # En Windows
```

### 3. Instalar dependencias

Instala las dependencias del proyecto utilizando `pip`:

```bash
pip install -r requirements.txt
```

Si no tienes un archivo `requirements.txt`, puedes crear uno con las dependencias necesarias:

```bash
pip freeze > requirements.txt
```

Las dependencias mínimas para este proyecto son:

```
Django==4.0
```

### 4. Configurar el proyecto

En este momento, el proyecto debería estar listo para ejecutarse sin necesidad de configuración adicional, ya que no se usa base de datos.

### 5. Ejecutar el servidor de desarrollo

Para ejecutar el servidor de desarrollo de Django, utiliza el siguiente comando:

```bash
python manage.py runserver
```

Esto levantará el servidor en `http://127.0.0.1:8000/`.

### 6. Acceder a las rutas

Una vez que el servidor esté en ejecución, puedes hacer solicitudes a las siguientes rutas:

- **GET** `/orders/status/`:
    - Devuelve el estado actual de la orden en formato JSON.
    - Ejemplo de respuesta:
    ```json
    {
        "created": "20240910 120000",
        "paid": false,
        "subtotal": 0,
        "taxes": 0,
        "discounts": 0,
        "items": [],
        "rounds": []
    }
    ```

- **POST** `/orders/create/`:
    - Crea una nueva orden. Debes enviar un JSON con los elementos de la orden.
    - Ejemplo de cuerpo de solicitud:
    ```json
    {
        "items": [
            {"name": "Corona", "quantity": 2},
            {"name": "Club Colombia", "quantity": 1}
        ]
    }
    ```

    - Ejemplo de respuesta si todo es correcto:
    ```json
    {
        "created": "20240910 120000",
        "paid": false,
        "subtotal": 340,
        "taxes": 71.4,
        "discounts": 0,
        "items": [],
        "rounds": [
            {
                "created": "20240910 120030",
                "items": [
                    {"name": "Corona", "quantity": 2},
                    {"name": "Club Colombia", "quantity": 1}
                ]
            }
        ]
    }
    ```

    - Si hay algún problema con el stock, la respuesta será algo como:
    ```json
    {
        "error": "Lo sentimos, no tenemos disponibles las siguientes cervezas: Quilmes."
    }
    ```

### 7. Probar la API

Puedes probar las rutas usando herramientas como [Postman](https://www.postman.com/) o `curl`.

## Notas adicionales

- **No se está utilizando una base de datos**, toda la información se guarda en memoria.
- **El stock de cervezas es limitado**: Si intentas pedir más cervezas de las que hay disponibles, la respuesta indicará que no hay stock suficiente.



