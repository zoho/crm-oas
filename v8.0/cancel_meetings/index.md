# Cancel Meetings

- [OpenAPI specification](cancel_meetings.yaml)
- [Cancel a Meeting](mds/cancelMeetings.md)
  - To cancel a meeting and send an email regarding the meeting cancellation to the participants. A meeting can only be cancelled if attendees have already been invited and the meeting has not passed its scheduled end time. To check the cancellation status of a meeting, refer to the $event_cancelled key in the response from the [Get Records API](record.yaml#$.paths./module.get).
  - [Examples](mds/examples/cancelMeetings.md)
