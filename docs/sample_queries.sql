-- Count the win/rate ratio for each army with possible filtering of games
WITH
   A1 as (
     SELECT "Army1" as "Army", "Army2" as "Opponent", e1."Rank" as "Rank", e2."Rank" as "ORank",
         "Datetime", "Tournament", "TournamentRank", "ScoringType", "GameFormat",
         "VictoryPoints1" as "VP", "TournamentPoints1" as "TP",
         "VictoryPoints2" as "OVP", "TournamentPoints2" as "OTP"
      FROM "Score" 
      JOIN "Elo" as "e1" ON e1."Player"="Player1"
      JOIN "Elo" as "e2" ON e2."Player"="Player2"
      ),
   A2 as (
      SELECT "Army2" as "Army", "Army1" as "Opponent", e2."Rank" as "Rank", e1."Rank" as "ORank",
         "Datetime", "Tournament", "TournamentRank", "ScoringType", "GameFormat",
         "VictoryPoints2" as "VP", "TournamentPoints2" as "TP",
         "VictoryPoints1" as "OVP", "TournamentPoints1" as "OTP"
      FROM "Score"
      JOIN "Elo" as "e1" ON e1."Player"="Player1"
      JOIN "Elo" as "e2" ON e2."Player"="Player2"
      ),
   AA as (SELECT * FROM A1 UNION ALL SELECT * FROM A2),
   ArmyScore as(
      SELECT *,
         CASE
            WHEN "TP">"OTP" THEN 'Win'
            WHEN "TP"<"OTP" THEN 'Loss'
            ELSE 'Draw'
         END as "Result"
      FROM AA
      -- Add the additional filtering here below:
      WHERE "GameFormat" = 'Zgrupowanie' AND "Rank" > 1000 AND "ORank" > 1000
      ),
      
   Wins as (
      SELECT "Army", COUNT(*) as "Wins" FROM ArmyScore WHERE "Result" = 'Win' GROUP BY "Army"
      ),
   Games as (
      SELECT "Army", COUNT(*) as "Games" FROM ArmyScore GROUP BY "Army"
      )

SELECT Games."Army", cast("Wins" as float)/cast("Games" as float) as "WinRate", "Games"
FROM Games 
LEFT JOIN Wins 
ON Wins."Army" = Games."Army" 
WHERE Games."Games" > 10 
ORDER BY "WinRate" DESC;
