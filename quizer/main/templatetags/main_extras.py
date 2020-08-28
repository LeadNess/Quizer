# pylint: disable=invalid-name
"""Custom template tags"""
import json
from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def deserialize_subjects(subjects):
    return json.dumps([{'name': subject.name, 'id': subject.id} for subject in subjects])


@register.simple_tag
def deserialize_lecturers(lecturers):
    return json.dumps([{'name': lecturer.username, 'id': lecturer.id} for lecturer in lecturers])


@register.simple_tag
def deserialize_tests(tests):
    return json.dumps([{'name': test.name, 'id': test.id} for test in tests])


@register.simple_tag
def static_url():
    """Return static path"""
    return settings.STATIC_URL


@register.simple_tag
def sort_icon():
    """Sort icon source"""
    return settings.STATIC_URL + 'main/images/sort.svg'


@register.simple_tag
def team_icon():
    """Team icon source"""
    return settings.STATIC_URL + 'main/images/team.svg'


@register.simple_tag
def clock_icon():
    """Clock icon source"""
    return settings.STATIC_URL + 'main/images/clock.svg'


@register.simple_tag
def task_icon():
    """Task icon source"""
    return settings.STATIC_URL + 'main/images/task.svg'


@register.simple_tag
def person_icon():
    """Person icon source"""
    return settings.STATIC_URL + 'main/images/person.svg'


@register.simple_tag
def logout_icon():
    """Logout icon source"""
    return settings.STATIC_URL + 'main/images/logout.svg'


@register.simple_tag
def wait_icon():
    """Wait icon source"""
    return settings.STATIC_URL + 'main/images/wait.svg'


@register.simple_tag
def research_icon():
    """Research icon source"""
    return settings.STATIC_URL + 'main/images/research.svg'


@register.simple_tag
def add_test_icon():
    """Add test icon source"""
    return settings.STATIC_URL + 'main/images/add-test.svg'


@register.simple_tag
def edit_icon():
    """Edit test icon source"""
    return settings.STATIC_URL + 'main/images/edit.svg'


@register.simple_tag
def user_icon():
    """User icon source"""
    return settings.STATIC_URL + 'main/images/user.svg'


@register.simple_tag
def subject_icon():
    """Subject icon source"""
    return settings.STATIC_URL + 'main/images/white_subject.svg'


@register.simple_tag
def delete_icon():
    """Delete icon source"""
    return settings.STATIC_URL + 'main/images/delete.svg'


@register.simple_tag
def add_icon():
    """Add icon source"""
    return settings.STATIC_URL + 'main/images/add.svg'


@register.simple_tag
def cancel_icon():
    """Cancel icon source"""
    return settings.STATIC_URL + 'main/images/cancel.svg'


@register.simple_tag
def download_icon():
    """Download icon source"""
    return settings.STATIC_URL + 'main/images/download.svg'


@register.simple_tag
def play_icon():
    """Play icon source"""
    return settings.STATIC_URL + 'main/images/play.svg'


@register.simple_tag
def finish_icon():
    """Finish icon source"""
    return settings.STATIC_URL + 'main/images/finish.svg'


@register.simple_tag
def search_icon():
    """Search icon source"""
    return settings.STATIC_URL + 'main/images/loupe.svg'


@register.simple_tag
def close_icon():
    """Close icon source"""
    return settings.STATIC_URL + 'main/images/close.svg'


@register.simple_tag
def database_icon():
    """Database icon source"""
    return settings.STATIC_URL + 'main/images/database.svg'
