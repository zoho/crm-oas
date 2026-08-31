Successful retrieval of workflow rule action usage metrics

```json
{
  "workflow_rules": [
    {
      "trigger_count": 3,
      "name": "High Value Lead Rule",
      "id": "4876876000013248001",
      "conditions": [
        {
          "instant_actions": {
            "actions": [
              {
                "queue_count": 0,
                "related_details": {
                  "bulk_mail": false,
                  "unopened": 0,
                  "sent_percentage": 100,
                  "opened": 1,
                  "delivered": 1,
                  "unsent": 0,
                  "bounced": 0,
                  "clicked": 0,
                  "sent": 1
                },
                "name": "High revenue Lead added",
                "success_count": 1,
                "failure_count": 0,
                "id": "4876876000016390103",
                "type": "email_notifications",
                "associated_time": "2025-10-16T16:19:58+05:30"
              },
              {
                "name": "To users : Patricia Boyle",
                "success_count": 2,
                "failure_count": 0,
                "id": "4876876000013248016",
                "type": "assign_owner",
                "associated_time": "2025-08-08T22:40:00+05:30"
              }
            ]
          },
          "scheduled_actions": [
            {
              "id": "4876876000016390118",
              "actions": [
                {
                  "queue_count": 0,
                  "related_details": {
                    "bulk_mail": false,
                    "unopened": 0,
                    "sent_percentage": 100,
                    "opened": 1,
                    "delivered": 1,
                    "unsent": 0,
                    "bounced": 0,
                    "clicked": 0,
                    "sent": 1
                  },
                  "name": "High revenue Lead added",
                  "success_count": 1,
                  "failure_count": 0,
                  "id": "4876876000016390103",
                  "type": "email_notifications",
                  "associated_time": "2025-10-16T16:19:58+05:30"
                }
              ]
            }
          ],
          "usage_count": 2,
          "id": "4876876000013248002"
        },
        {
          "instant_actions": {
            "actions": [
              {
                "name": "P1",
                "success_count": 0,
                "tag_id": "4876876000011037076",
                "failure_count": 0,
                "id": "4876876000013248015",
                "type": "add_tags",
                "associated_time": "2025-08-08T22:40:00+05:30"
              }
            ]
          },
          "scheduled_actions": [],
          "usage_count": 0,
          "id": "4876876000013248004"
        }
      ],
      "reset_time": "2025-10-16T16:23:04+05:30"
    }
  ]
}
```
