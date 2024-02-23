import goals_from_team_statistic as gts

raw_data = {"response": {"team": {"name": "Cruz Azul"}, "goals": {"for": {"total": {"total": 49}}}}}


def test_obtain_name_team():
    expected_name_team = "Cruz Azul"
    obtained_name_team = gts.obtain_name_team(raw_data)
    assert obtained_name_team == expected_name_team
