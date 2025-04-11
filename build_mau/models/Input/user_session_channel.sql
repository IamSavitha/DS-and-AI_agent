with user_session_channel as(
        SELECT
                sessionId,
                userId,
                channel,                        
        FROM {{ source('raw','user_session_channel')}}
)                 
SELECT * from user_session_channel
WHERE sessionId is not null
