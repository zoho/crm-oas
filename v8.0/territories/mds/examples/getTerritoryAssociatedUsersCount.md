# Examples: getTerritoryAssociatedUsersCount

**GET /settings/territories/actions/associated_users_count**

## Response examples

### Status `200` — `application/json` — TerritoryAssociatedUsersCountResponse

Successful retrieval of territory-associated user counts


```json
{
  "associated_users_count": [
    {
      "count": 5,
      "territory": {
        "id": "2276164000001054020",
        "name": "zoho"
      }
    },
    {
      "count": 1,
      "territory": {
        "name": "Chennai Leads",
        "id": "431581000000744183"
      }
    }
  ],
  "info": {
    "per_page": 200,
    "count": 2,
    "page": 1,
    "more_records": false
  }
}
```

### Status `400` — `application/json` — TerritoryNotYetEnabled

Territory Management not yet enabled error


```json
{
  "code": "FEATURE_NOT_ENABLED",
  "details": {},
  "message": "Territory Management is not enabled",
  "status": "error"
}
```

### Status `400` — `application/json` — TerritoryDisabled

Territory Management disabled error


```json
{
  "code": "FEATURE_NOT_ENABLED",
  "details": {},
  "message": "Territory Management is disabled",
  "status": "error"
}
```

### Status `401` — `application/json` — AuthenticationFailure

Authentication failure due to invalid or expired OAuth token


```json
{
  "code": "AUTHENTICATION_FAILURE",
  "details": {},
  "message": "Authentication failed",
  "status": "error"
}
```
