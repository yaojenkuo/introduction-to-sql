def extract_test_queries(qid):
    test_queries = {
        '0101': """SELECT type, name FROM sqlite_master;""",
        '0102': """PRAGMA TABLE_INFO(presidential2020);""",
        '0103': """SELECT * FROM presidential2020;""",
        '0104': """SELECT county, town, village FROM presidential2020;""",
        '0105': """SELECT DISTINCT candidates FROM presidential2020;""",
        '0106': """SELECT DISTINCT candidates FROM presidential2016;""",
        '0107': """SELECT * FROM presidential2020 LIMIT 10;""",
        '0108': """SELECT DISTINCT county AS distinct_counties FROM presidential2020;"""
    }
    return test_queries[qid]