# Venutto Admin

Panel de administración para **Venutto**, desarrollado con Django. Permite gestionar el catálogo de productos organizado por categorías, con su precio, descripción y disponibilidad, y muestra el menú de productos disponibles.

## Funcionalidades

- Categorías de productos, con control de disponibilidad.
- Productos con nombre, precio, descripción y disponibilidad. Cada producto pertenece a una categoría.
- Vista de menú con los productos disponibles.
- Panel de administración de Django para cargar y editar el catálogo.

## Estructura

| App | Función |
| --- | --- |
| `productos` | Categorías, productos y vista del menú |
| `usuarios` | Reservada para la gestión de usuarios |
| `config` | Configuración del proyecto y URLs |

## Instalación local

```bash
git clone https://github.com/jatoledo-max/venutto-admin.git
cd venutto-admin
python -m venv venv
venv\Scripts\activate            # Windows  (Linux/macOS: source venv/bin/activate)
pip install -r requierements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Luego abre `http://127.0.0.1:8000/admin/` para cargar categorías y productos, y `http://127.0.0.1:8000/` para ver el menú.

## Tecnologías

Python · Django 6.0
