### `application/json` — UpdateDraft

Example request to update email drafts

```json
{
  "__email_drafts": [
    {
      "id": "4f8efdcbaf23fd33c939217d4e14222d6d1cb21e4a45914fb9ba0c31c3c47330",
      "from": "john@example.com",
      "to": [
        {
          "user_name": "John Doe",
          "email": "john.doe@example.com"
        }
      ],
      "reply_to": null,
      "cc": [],
      "bcc": [],
      "inventory_details": null,
      "schedule_details": null,
      "rich_text": true,
      "subject": "Test Subject",
      "content": "<p>Hello!</p>"
    }
  ]
}
```

### `application/json` — LeadsUpdateDraft

Example request to update a Leads email draft

```json
{
  "__email_drafts": [
    {
      "id": "4f8efdcbaf23fd33c939217d4e14222d6d1cb21e4a45914fb9ba0c31c3c47330",
      "from": "user1@example.com",
      "to": [
        {
          "user_name": "user1",
          "email": "user1@example.com"
        }
      ],
      "reply_to": "reply@example.com",
      "cc": [
        {
          "user_name": "user2",
          "email": "user2@example.com"
        }
      ],
      "bcc": [
        {
          "user_name": "user3",
          "email": "user3@example.com"
        }
      ],
      "schedule_details": {
        "time": "2023-03-25T14:00:54+05:30",
        "timezone": null,
        "source": "upTime"
      },
      "rich_text": true,
      "subject": "Test Draft update",
      "content": "this is the updated content"
    }
  ]
}
```

### `application/json` — LeadsUpdateDraftWithId

Sample request body for updating a Leads email draft

```json
{
  "__email_drafts": [
    {
      "id": "4f8efdcbaf23fd33c939217d4e14222d6d1cb21e4a45914fb9ba0c31c3c47330",
      "reply_to": "pat.boyle@zylker.com",
      "from": "patricia.boyle@zylker.com",
      "to": [
        {
          "user_name": "user1",
          "email": "user1@zylker.com"
        }
      ],
      "cc": [
        {
          "user_name": "user2",
          "email": "user2@zylker.com"
        }
      ],
      "bcc": [
        {
          "user_name": "user3",
          "email": "user3@zylker.com"
        }
      ],
      "subject": "Test Draft update",
      "content": "this is the updated content",
      "rich_text": true,
      "schedule_details": {
        "time": "2023-03-25T14:00:54+05:30",
        "timezone": null
      }
    }
  ]
}
```
