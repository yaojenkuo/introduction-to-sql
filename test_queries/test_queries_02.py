def extract_test_queries(qid):
    test_queries = {
        '0201': """SELECT DISTINCT county || town || village AS combined_key
        FROM presidential2020;""",
        '0202': """SELECT firstName,
       lastName,
       weightKilograms / (heightMeters*heightMeters) AS bmi
  FROM players
 ORDER BY bmi DESC;""",
        '0203': """SELECT *
  FROM presidential2020
 WHERE county='臺北市';""",
        '0204': """SELECT * 
  FROM presidential2020
 WHERE county IN ('臺北市', '新北市', '桃園市', '臺中市', '臺南市', '高雄市');""",
        '0205': """SELECT personId,
       ppg
  FROM careerSummaries
 WHERE ppg > 20;""",
        '0206': """SELECT personId,
       CAST(assists AS REAL) / CAST(turnovers AS REAL) AS ast_to_ratio
  FROM careerSummaries
 ORDER BY ast_to_ratio DESC
 LIMIT 10;"""
    }
    return test_queries[qid]