# hiking_buddy/core/repositories/group_repository.py

from domain.models.group import Group


class GroupRepository:
    def get_next_id(self) -> int:
        raise NotImplementedError

    def save(self, group: Group) -> None:
        raise NotImplementedError

    def list_all(self):
        raise NotImplementedError


class InMemoryGroupRepository(GroupRepository):
    def __init__(self):
        self._groups = {}
        self._current_id = 1

    def get_next_id(self) -> int:
        nid = self._current_id
        self._current_id += 1
        return nid

    def save(self, group: Group) -> None:
        self._groups[group.id] = group
        print(f"[GroupRepository] Saved group {group.id} - {group.name}")

    def list_all(self):
        return list(self._groups.values())
