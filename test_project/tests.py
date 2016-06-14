import pytest



def test_empty_select_multiple(session_browser, live_server):
    def add_team(name):
        session_browser.find_by_id('add_id_previous_teams').click()
        session_browser.windows.current = session_browser.windows[1]
        session_browser.fill_form({'name': name})
        session_browser.find_by_css('input[type=submit]').click()
        session_browser.windows.current = session_browser.windows[0]

    def get_value():
        return session_browser.evaluate_script('$("#id_previous_teams").val()')

    def get_value_label(value):
        return session_browser.evaluate_script(
            '$("#id_previous_teams option[value=%s]").html()' % value
        )

    session_browser.visit(live_server.url)
    session_browser.fill_form({'name': 'testplayer'})

    add_team('bar')
    assert get_value_label(1) == 'bar'
    assert get_value() == ['1']

    add_team('foo')
    assert get_value_label(2) == 'foo'
    assert get_value() == ['1', '2']

    session_browser.find_by_css('input[type=submit]').click()
    
    
def test_empty_foreign_key(session_browser, live_server):

    def add_team(name):
        session_browser.find_by_id('add_id_future_team').click()
        session_browser.windows.current = session_browser.windows[1]
        session_browser.fill_form({'name': name})
        session_browser.find_by_css('input[type=submit]').click()
        session_browser.windows.current = session_browser.windows[0]

    def change_team(name):
        session_browser.find_by_id('change_id_future_team').click()
        session_browser.windows.current = session_browser.windows[1]
        session_browser.fill_form({'name': name})
        session_browser.find_by_css('input[type=submit]').click()
        session_browser.windows.current = session_browser.windows[0]

    def get_value():
        return session_browser.evaluate_script('$("#id_future_team").val()')

    def get_value_label(value):
        return session_browser.evaluate_script(
            '$("#id_future_team option[value=%s]").html()' % value
        )

    session_browser.visit(live_server.url)
    session_browser.fill_form({'name': 'testplayer'})

    # I don't know how to reset the database between tests, so ID is 3
    add_team('john')
    assert get_value_label(3) == 'john'
    assert get_value() == '3'

    change_team('doe')
    assert get_value_label(3) == 'doe'
    assert get_value() == '3'

    session_browser.find_by_css('input[type=submit]').click()
