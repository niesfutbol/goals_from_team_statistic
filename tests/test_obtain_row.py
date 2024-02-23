import goals_from_team_statistic as gts

raw_data = {"response": {"team": {"name": "Cruz Azul"}, "goals": {"for": {"total": {"total": 49}}}}}


def test_obtain_name_team():
    expected_name_team = "Cruz Azul"
    obtained_name_team = gts.obtain_name_team(raw_data)
    assert obtained_name_team == expected_name_team
    assert_a_real_example_from_json_file()


def assert_a_real_example_from_json_file():
    expected_name_team = "Cruz Azul"
    real_example = gts.read_json("tests/data/data_file_262_2295.json")
    obtained_name_team = gts.obtain_name_team(real_example)
    assert obtained_name_team == expected_name_team
