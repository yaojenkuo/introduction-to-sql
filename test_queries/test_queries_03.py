def extract_test_queries(qid):
    test_queries = {
        '0301': """SELECT COUNT(*) AS n_teams
  FROM teams
 WHERE confName = 'East';""",
        '0302': """SELECT COUNT(*) AS n_teams
  FROM teams
 WHERE confName = 'West';""",
        '0303': """SELECT COUNT(*) AS n_obs
  FROM presidential2020;""",
        '0304': """SELECT COUNT(*) AS n_cols
  FROM PRAGMA_TABLE_INFO('presidential2020');""",
        '0305': """SELECT COUNT(*) AS n_players
  FROM careerSummaries
 WHERE ppg > 20;""",
        '0306': """SELECT SUM(votes) AS total_votes
  FROM presidential2020;""",
        '0307': """SELECT number,
       candidates,
       SUM(votes) AS total_votes
  FROM presidential2020
 GROUP BY number;""",
        '0308': """SELECT town,
       SUM(votes) AS total_votes
  FROM presidential2020
 WHERE county = '臺北市'
 GROUP BY town
HAVING total_votes > 100000
ORDER BY total_votes DESC;""",
        '0309': """SELECT CASE WHEN county IN ('臺北市', '新北市', '桃園市', '臺中市', '臺南市', '高雄市') THEN '六都'
       ELSE '非六都'
       END AS county_type,
       SUM(votes) AS total_votes
  FROM presidential2020
 GROUP BY county_type;""",
        '0310': """SELECT number,
       candidates,
       CASE WHEN county IN ('臺北市', '新北市', '桃園市', '臺中市', '臺南市', '高雄市') THEN '六都'
       ELSE '非六都'
       END AS county_type,
       SUM(votes) AS total_votes
  FROM presidential2020
 GROUP BY number, county_type;""",
        '0311': """SELECT firstName,
       lastName
  FROM players
 WHERE personId = (
           SELECT personId
             FROM careerSummaries
            WHERE assists = (
                SELECT MAX(assists)
                  FROM careerSummaries
            )
       );""",
        '0312': """SELECT firstName,
       lastName
  FROM players
 WHERE personId = (
           SELECT personId
             FROM careerSummaries
            WHERE totReb = (
                SELECT MAX(totReb)
                  FROM careerSummaries
            )
       );""",
        '0313': """SELECT firstName,
       lastName
  FROM players
 WHERE personId IN (
           SELECT personId
             FROM rosters
            WHERE teamId = (SELECT teamId
                              FROM teams
                             WHERE nickname = 'Bucks')
       );""",
        '0314': """SELECT number,
       candidates,
       CAST(SUM(votes) AS REAL) / CAST((SELECT SUM(votes) FROM presidential2016) AS REAL) AS votes_percentage
  FROM presidential2016
 GROUP BY number;""",
        '0315': """SELECT number,
       candidates,
       CAST(SUM(votes) AS REAL) / CAST((SELECT SUM(votes) FROM presidential2020) AS REAL) AS votes_percentage
  FROM presidential2020
 GROUP BY number;""",
        '0316': """SELECT 2016 AS year,
       number,
       candidates,
       SUM(votes) AS total_votes
  FROM presidential2016
 GROUP BY number
UNION
SELECT 2020 AS year,
       number,
       candidates,
       SUM(votes) AS total_votes
  FROM presidential2020
 GROUP BY number;""",
        '0317': """SELECT 2016 AS year,
       number,
       candidates,
       CAST(SUM(votes) AS REAL) / CAST((SELECT SUM(votes) FROM presidential2016) AS REAL) AS votes_percentage
  FROM presidential2016
 GROUP BY number
UNION
SELECT 2020 AS year,
       number,
       candidates,
       CAST(SUM(votes) AS REAL) / CAST((SELECT SUM(votes) FROM presidential2020) AS REAL) AS votes_percentage
  FROM presidential2020
 GROUP BY number;""",
        '0318': """SELECT ing_te.town,
       kuo_cheng.Kuo_Cheng,
       ing_te.Ing_Te
  FROM (SELECT town,
               SUM(votes) AS Kuo_Cheng
          FROM presidential2020
         WHERE county = '臺北市' AND
               number = 2
         GROUP BY town
         ) AS kuo_cheng
  LEFT JOIN (SELECT town,
                    SUM(votes) AS Ing_Te
               FROM presidential2020
              WHERE county = '臺北市' AND
                    number = 3
              GROUP BY town
              ) AS ing_te
    ON kuo_cheng.town = ing_te.town;""",
        '0319': """SELECT ing_te.town,
       kuo_cheng.Kuo_Cheng,
       ing_te.Ing_Te
  FROM (SELECT town,
               SUM(votes) AS Kuo_Cheng
          FROM presidential2020
         WHERE county = '臺北市' AND
               number = 2
         GROUP BY town
         ) AS kuo_cheng
  LEFT JOIN (SELECT town,
                    SUM(votes) AS Ing_Te
               FROM presidential2020
              WHERE county = '臺北市' AND
                    number = 3
              GROUP BY town
              ) AS ing_te
    ON kuo_cheng.town = ing_te.town
 WHERE kuo_cheng.Kuo_Cheng > ing_te.Ing_Te;""",
        '0320': """SELECT teams.fullName,
       players.firstName,
       players.lastName,
       careerSummaries.ppg,
       careerSummaries.rpg,
       careerSummaries.apg
  FROM players
  JOIN teams
    ON players.teamId = teams.teamId
  JOIN careerSummaries
    ON players.personId = careerSummaries.personId
 WHERE teams.nickname = 'Lakers'
 ORDER BY players.firstName;"""
    }
    return test_queries[qid]