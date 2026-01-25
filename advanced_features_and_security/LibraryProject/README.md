# Permissions and Groups Setup

This module demonstrates role-based access control in Django.

## Custom Permissions
Defined in `Article` model:
- `can_view`
- `can_create`
- `can_edit`
- `can_delete`

## Groups
- **Viewers** → can_view
- **Editors** → can_view, can_create, can_edit
- **Admins** → can_view, can_create, can_edit, can_delete

## Usage
- Permissions enforced in `views.py` using `@permission_required`.
- Run `python manage.py setup_groups` to initialize groups and permissions.
- Assign users to groups via Django Admin.
