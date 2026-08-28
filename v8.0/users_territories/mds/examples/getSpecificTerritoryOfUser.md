# Examples: getSpecificTerritoryOfUser

**GET /users/{user}/territories/{territory}**

## Response examples

### Status `200` — `application/json` — GetTerritoryOfUser

Get specific territory of a user

```json
{
  "territories": [
    {
      "id": "111121000000078023",
      "Manager": {
        "id": "111121000000076087"
      },
      "Name": "T3",
      "Reporting_To": {
        "id": "111121000000076087",
        "Name": "zoho crm"
      }
    }
  ],
  "info": {
    "per_page": 200,
    "count": 1,
    "page": 1,
    "more_records": false
  }
}
```

### Status `400` — `application/json` — InvalidUserId

Invalid user ID error

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 1
  },
  "message": "the related id given seems to be invalid",
  "status": "error"
}
```
