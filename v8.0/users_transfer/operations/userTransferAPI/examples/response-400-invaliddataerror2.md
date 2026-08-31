An example error response of a deleted transfer target user.

```json
{
  "transfer": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.transfer.transfer.id",
        "owner_status": "deleted"
      },
      "message": "The user to whom you are trying to transfer is deleted.",
      "status": "error"
    }
  ]
}
```
