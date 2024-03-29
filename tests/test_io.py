import goals_from_team_statistic as dt


def test_read_json():
    path = "tests/data/data_file_262_2295.json"
    stats_team = dt.read_json(path)
    assert_read_a_query_of_teams_statistics(stats_team)


def assert_read_a_query_of_teams_statistics(stats_team):
    obtained_query = stats_team["get"]
    expected_query = "teams/statistics"
    assert obtained_query == expected_query
