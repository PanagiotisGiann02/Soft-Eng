# hiking_buddy/tests/test_create_group.py

import pytest
from domain.models.user import User
from application.use_cases.create_group import CreateGroup
from domain.models.group import Group
from core.repositories.group_repository import InMemoryGroupRepository


@pytest.fixture
def group_repo():
    return InMemoryGroupRepository()


@pytest.fixture
def normal_user():
    return User(
        id=100,
        username="john_doe",
        first_name="John",
        last_name="Doe",
        email="john@example.com",
        phone_number="1234567890",
        password_hash="hash",
    )


@pytest.fixture
def create_group_uc(group_repo):
    return CreateGroup(group_repo)


def test_create_group_unique_name(normal_user, create_group_uc, group_repo):
    group = create_group_uc.execute(
        creator=normal_user,
        name="HikersClub",
        description="A club for hikers",
        logo_uri="logo.png",
        visibility="public",
    )
    assert isinstance(group, Group)
    assert group.id == 1
    assert group.name == "HikersClub"
    assert group.description == "A club for hikers"
    assert group.logo_uri.endswith(".png")
    assert group.visibility == "public"
    # User becomes manager
    assert group.manager_id == normal_user.id


def test_create_group_name_taken(normal_user, create_group_uc, group_repo):
    # Pre-create a group with the same name
    existing = group_repo.get_next_id()
    group_repo.save(
        Group(
            id=existing,
            name="TrailBlazers",
            description="",
            logo_uri="l.png",
            visibility="public",
            manager_id=normal_user.id,
        )
    )
    with pytest.raises(ValueError) as exc:
        create_group_uc.execute(
            creator=normal_user,
            name="TrailBlazers",
            description="Dup",
            logo_uri="logo.png",
            visibility="public",
        )
    assert "Name already taken" in str(exc.value)


def test_create_group_missing_description(normal_user, create_group_uc):
    with pytest.raises(ValueError) as exc:
        create_group_uc.execute(
            creator=normal_user,
            name="NewClub",
            description="",
            logo_uri="logo.png",
            visibility="public",
        )
    assert "Missing description" in str(exc.value)


def test_create_group_invalid_logo_format(normal_user, create_group_uc):
    with pytest.raises(ValueError) as exc:
        create_group_uc.execute(
            creator=normal_user,
            name="LogoTest",
            description="Desc",
            logo_uri="logo.txt",
            visibility="public",
        )
    assert "Invalid image format" in str(exc.value)


def test_cancel_before_create(group_repo):
    # Alt Flow: user cancels, repository remains empty
    assert group_repo.list_all() == []  # No create_group_uc.execute call
