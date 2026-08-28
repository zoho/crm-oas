# Examples: removeSpecificTerritoriesfromUser

**DELETE /users/{user}/territories/{territory}**

## Response examples

### Status `200` — `application/json` — RemoveTerritoriesExample

Successful territory removal response

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
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 3
  },
  "message": "Invalid Territory Id",
  "status": "error"
}
```
