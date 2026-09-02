Partial success with mixed deletion results.

```json
{
  "webhooks": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000066004"
      },
      "message": "webhook deleted successfully",
      "status": "success"
    },
    {
      "code": "NOT_ALLOWED",
      "details": {
        "id": "111111000000057597"
      },
      "message": "webhook is associated with at least one of Approval Process/Workflow Rules/Blueprint",
      "status": "error"
    }
  ]
}
```
