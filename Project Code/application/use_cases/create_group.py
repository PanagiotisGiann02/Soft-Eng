# hiking_buddy/application/use_cases/create_group.py

from domain.models.group import Group
from domain.models.user import User


class CreateGroup:
    def __init__(self, group_repository):
        self.group_repository = group_repository

    def execute(
        self, creator: User, name: str, description: str, logo_uri: str, visibility: str
    ):
        # Ensure user is logged in
        if creator is None or not isinstance(creator, User):
            raise PermissionError("User must be logged in to create groups")
        # Validate unique name
        existing = [g for g in self.group_repository.list_all() if g.name == name]
        if existing:
            raise ValueError("Name already taken")
        # Validate description
        if not description or not description.strip():
            raise ValueError("Missing description")
        # Validate logo format
        if not (
            logo_uri.lower().endswith(".png")
            or logo_uri.lower().endswith(".jpg")
            or logo_uri.lower().endswith(".jpeg")
        ):
            raise ValueError("Invalid image format")
        # Create group
        group_id = self.group_repository.get_next_id()
        group = Group(
            id=group_id,
            name=name,
            description=description,
            logo_uri=logo_uri,
            visibility=visibility,
            manager_id=creator.id,
        )
        self.group_repository.save(group)
        return group
