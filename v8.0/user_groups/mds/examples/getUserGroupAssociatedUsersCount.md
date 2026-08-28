# Examples: getUserGroupAssociatedUsersCount

**GET /settings/user_groups/actions/associated_users_count**

## Response examples

### Status `200` — `application/json` — Success

Successful response with associated user counts

```json
{
  "associated_users_count": [
    {
      "user_group": {
        "name": "Sales Team Updated",
        "id": "4413474000003538005"
      },
      "count": 2
    },
    {
      "user_group": {
        "name": "Sales Team 1766826714258",
        "id": "4413474000003538020"
      },
      "count": 2
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

### Status `404` — `application/json` — InvalidData

Invalid URL pattern

```json
{
  "code": "INVALID_URL_PATTERN",
  "details": {},
  "message": "The provided group ID is invalid.",
  "status": "error"
}
```
