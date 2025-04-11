
WITH user_session_channel AS
(
  select 
   sessionId,
   userId,
   channel,
  
 from {{ref ('user_session_channel')}} 
 ),
 session_timestamp as 
 (
  select 
   sessionId,
  ts   
 FROM {{ ref('session_timestamp') }}
 )
SELECT  
usc.sessionId,
usc.userId,
usc.channel, 
st.ts 
FROM user session channel usc 
JOIN session timestamp st 
ON usc.sessionId st.session
