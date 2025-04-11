WITH session_timestamp as 
(
SELECT
    sessionId,
    ts
FROM {{ source('raw', 'session_timestamp') }} )
SELECT *
FROM session_timestamp
WHERE sessionId IS NOT NULL