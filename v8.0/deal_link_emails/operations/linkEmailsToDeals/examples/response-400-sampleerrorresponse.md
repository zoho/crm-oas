Link Emails to Deals - Error Response

```json
{
  "Emails": [
    [
      {
        "status": "error",
        "code": "MANDATORY_NOT_FOUND",
        "message": "message_id is mandatory",
        "details": {
          "api_name": "message_id",
          "json_path": "Emails[0].message_id"
        }
      }
    ],
    [
      {
        "status": "error",
        "code": "INVALID_DATA",
        "message": "invalid data",
        "details": {
          "api_name": "linked_record.id",
          "json_path": "Emails[1].linked_record.id"
        }
      }
    ]
  ]
}
```
