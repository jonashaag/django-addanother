import pytest

from django.contrib.staticfiles.testing import StaticLiveServerTestCase


def test_empty_form(session_browser, live_server):
    def add_group(name):
        session_browser.find_by_id('add_id_groups').click()
        session_browser.windows.current = session_browser.windows[1]
        session_browser.fill_form({'name': name})
        session_browser.find_by_css('input[type=submit]').click()
        session_browser.windows.current = session_browser.windows[0]
        return session_browser.find_by_id('id_groups')[0]

    def get_value():
        return session_browser.evaluate_script('$("#id_groups").val()')

    def get_value_label(value):
        return session_browser.evaluate_script(
            '$("#id_groups option[value=%s]").html()' % value
        )

    session_browser.visit(live_server.url)
    session_browser.fill_form({'username': 'testuser'})

    select = add_group('bar')
    assert get_value() == ['1']
    assert get_value_label(1) == 'bar'

    session_browser.find_by_css('input[type=submit]').click()

    select = add_group('foo')
    assert get_value() == ['1', '2']
    assert get_value_label(2) == 'foo'
    session_browser.find_by_css('input[type=submit]').click()
