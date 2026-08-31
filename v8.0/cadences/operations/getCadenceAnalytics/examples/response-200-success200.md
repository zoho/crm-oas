Successful Cadence analytics response

```json
{
  "cadences": [
    {
      "module": {
        "api_name": "Leads",
        "id": "111112000000002628"
      },
      "name": "publish cadence",
      "follow_ups": [
        {
          "analytics": {
            "open_tasks_count": 1,
            "failed_tasks_count": 0,
            "subject": "task1",
            "completed_tasks_count": 0,
            "tasks_count": 1
          },
          "parent_follow_up": null,
          "action": {
            "name": "task1",
            "type": "tasks"
          },
          "id": "111112000000094014"
        },
        {
          "analytics": {
            "created_calls_count": 0,
            "cancelled_calls_count": 0,
            "failed_calls_count": 0,
            "completed_calls_count": 0,
            "scheduled_calls_count": 1,
            "subject": "Call scheduled with test",
            "calls_count": 1,
            "overdue_calls_count": 0,
            "missed_calls_count": 0
          },
          "parent_follow_up": {
            "id": "111112000000094014",
            "type": "tasks"
          },
          "action": {
            "name": "Demo",
            "type": "schedule_call"
          },
          "id": "111112000000094026"
        },
        {
          "analytics": {
            "email_count": 0,
            "bounced_email_count": 0,
            "clicked_email_count": 0,
            "replied_email_count": 0,
            "sent_email_count": 0,
            "unsent_email_count": 1,
            "opened_email_count": 0
          },
          "parent_follow_up": {
            "id": "111112000000094026",
            "type": "schedule_call"
          },
          "action": {
            "template": {
              "name": "Template",
              "id": "111112000000080016"
            },
            "name": "1",
            "type": "email_notifications"
          },
          "id": "111112000000094048"
        },
        {
          "analytics": {
            "whatsapp_count": 0,
            "delivered_whatsapp_count": 0,
            "failed_whatsapp_count": 0
          },
          "parent_follow_up": {
            "id": "111111000000115093",
            "type": "email_notifications"
          },
          "action": {
            "message_template": {
              "id": "111111000000115032",
              "title": "templatewhtsapp"
            },
            "name": "cad whtsapp",
            "id": "111111000000115279",
            "type": "whatsapp_message_notification"
          },
          "id": "111111000000115111"
        }
      ],
      "id": "111112000000094004",
      "created_by": {
        "name": "Poongodi89 S",
        "id": "111112000000057662"
      }
    }
  ]
}
```
