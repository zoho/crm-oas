# Examples: removeTerritoriesfromUser

**DELETE /users/{user}/territories**

## Response examples

### Status `200` — `application/json` — RemoveTerritoriesExample

Successful territories removal response

```json
{
  "territories": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111121000000088044"
      },
      "message": "Territory removed from the user successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidTerritoryId

Invalid territory ID error

```json
{
  "territories": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.territories[0].id"
      },
      "message": "Invalid Territory Id",
      "status": "error"
    }
  ]
}
```
