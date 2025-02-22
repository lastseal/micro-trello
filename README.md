# Micro Trello
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Obtener api_key (clave de API):

Para obtener las credenciales de conexión con un espacio de trabajo en Trello, se deben seguir los siguientes pasos:

1. Crear nueva integración en https://trello.com/power-ups/admin/new
2. En el menú Api Key obtener el código.
3. Genera manualmente un token
4. Obtener el board id desde la URL del tablero.

## Configuración

```bash
TRELLO_API_KEY=
TRELLO_API_TOKEN=
TRELLO_BOARD_ID=

# Variable para pruebas
PYTHONPATH=micro
```

## Uso Básico

```python
from micro import trello

data = trello.findMembers()
print(data)
```

```python
from micro import trello

data = trello.findMembers()
print(data)
```

## Referencias

[Primera llamada](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/#your-first-api-call)

[REST API](https://developer.atlassian.com/cloud/trello/rest/api-group-actions)
