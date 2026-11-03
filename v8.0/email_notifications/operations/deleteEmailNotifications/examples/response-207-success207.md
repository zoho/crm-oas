Bulk delete with mixed success and failure results

```json
{
  "email_notifications": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111112000000035041"
      },
      "message": "email_notifications deleted successfully",
      "status": "success"
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
