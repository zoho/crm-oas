# Examples: deleteRole

**DELETE /settings/roles/{role}**

## Response examples

### Status `200` — `application/json` — Success

Successful single role deletion response

```json
{
  "roles": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "4413524000000991004"
      },
      "message": "Role Deleted",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — Error

Missing required parameter during single role deletion

```json
{
  "roles": [
    {
      "status": "error",
      "code": "INVALID_DATA",
      "message": "invalid transferToId",
      "details": {
        "maximum_length": 200,
        "api_name": "name",
        "json_path": "$.roles[0].transfer_to_id"
      }
    }
  ]
}
```
