Bulk delete failure with INVALID_DATA for all requested IDs

```json
{
  "email_notifications": [
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "111113000000122012"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "111113000000121918"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "111113000000121973"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    },
    {
      "code": "NOT_ALLOWED",
      "details": {
        "id": "111113000000071904"
      },
      "message": "This email notification is associated with at least one of Approval Process/Workflow Rules/Blueprint",
      "status": "error"
    }
  ]
}
```
