
{% snapshot snapshot_session_summary %}
{{
config(
target_schema='analytics', 
unique_key='sessionId', 
strategy='timestamp', 
updated_at='session_time' 
) 
}}
SELECT 
sessionId,
userId, 
channel, 
event_timestamp, 
session_time 
FROM { { ref('session_summary') }}
{% endsnapshot %}
