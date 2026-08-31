An example error response for attempting to delete your own account.

```json
{
  "transfer_and_delete": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.transfer_and_delete.id"
      },
      "message": "Super Admin cannot be Deleted.",
      "status": "error"
    }
  ]
}
```
