### `application/json` — CreateDraft

Example request to create email drafts

```json
{
  "__email_drafts": [
    {
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
