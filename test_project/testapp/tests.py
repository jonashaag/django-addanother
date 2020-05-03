import functools
import pytest
from django_addanother.contrib import select2 as da_select2
from testapp.models import Team
from testapp.forms import PlayerForm


@pytest.mark.django_db
def test_widget_deepcopy():
    form1 = PlayerForm()
    form2 = PlayerForm()
    assert form1.fields['current_team'].widget.widget is not form2.fields['current_team'].widget.widget
    assert form1.fields['future_team'].widget.widget is not form2.fields['future_team'].widget.widget


@pytest.mark.django_db
def test_smoke_select2():
    """Some basic tests to verify the select2 integration works."""
    for widget_cls_name in da_select2.__all__:
        if 'Heavy' in widget_cls_name:
            # Need extra select2 specific arguments
            continue

        widget_cls = getattr(da_select2, widget_cls_name)
        if 'AddAnotherEditSelected' in widget_cls_name:
            widget_cls(add_related_url='x', edit_related_url='x', add_icon='x', edit_icon='x')
        elif 'AddAnother' in widget_cls_name:
            widget_cls(add_related_url='x', add_icon='x')
        else:
            widget_cls(edit_related_url='x', edit_icon='x')


@pytest.mark.django_db
def test_empty_select_multiple(session_browser, live_server):
    add_team = functools.partial(_add_team, session_browser, 'previous_teams')
    get_value = functools.partial(_get_value, session_browser, 'previous_teams')
    get_value_label = functools.partial(_get_value_label, session_browser, 'previous_teams')

    session_browser.visit(live_server.url)
    session_browser.fill_form({'name': 'testplayer'})

    add_team('bar')
    bar_pk = Team.objects.get(name='bar').pk
    assert get_value_label(bar_pk) == 'bar'
    assert get_value() == [str(bar_pk)]

    add_team('foo')
    foo_pk = Team.objects.get(name='foo').pk
    assert get_value_label(foo_pk) == 'foo'
    assert get_value() == [str(bar_pk), str(foo_pk)]

    session_browser.find_by_css('input[type=submit]').click()


@pytest.mark.django_db
def test_empty_foreign_key(session_browser, live_server):
    add_team = functools.partial(_add_team, session_browser, 'future_team')
    get_value = functools.partial(_get_value, session_browser, 'future_team')
    get_value_label = functools.partial(_get_value_label, session_browser, 'future_team')

    def edit_team(name):
        """Click the edit-related button to change a related Team object."""
        session_browser.find_by_id('change_id_future_team').click()
        session_browser.windows.current = session_browser.windows[1]
        session_browser.fill_form({'name': name})
        session_browser.find_by_css('input[type=submit]').click()
        session_browser.windows.current = session_browser.windows[0]

    session_browser.visit(live_server.url)
    session_browser.fill_form({'name': 'testplayer'})

    add_team('john')
    team_pk = Team.objects.get(name='john').pk
    assert get_value_label(team_pk) == 'john'
    assert get_value() == str(team_pk)

    edit_team('doe')
    assert get_value_label(team_pk) == 'doe'
    assert get_value() == str(team_pk)

    session_browser.find_by_css('input[type=submit]').click()


def _add_team(session_browser, field, team_name):
    """Click the add-another button to add a new related Team object."""
    session_browser.find_by_id('add_id_%s' % field).click()
    session_browser.windows.current = session_browser.windows[1]
    session_browser.fill_form({'name': team_name})
    session_browser.find_by_css('input[type=submit]').click()
    session_browser.windows.current = session_browser.windows[0]

def _get_value(session_browser, field):
    """Get an input field's value."""
    return session_browser.evaluate_script('$("#id_%s").val()' % field)

def _get_value_label(session_browser, field, value):
    """Get the label of an input field's value."""
    return session_browser.evaluate_script(
        '$("#id_%s option[value=%s]").html()' % (field, value)
    )
