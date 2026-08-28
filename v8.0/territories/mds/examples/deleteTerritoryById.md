# Examples: deleteTerritoryById

**DELETE /settings/territories/{id}**

## Response examples

### Status `200` — `application/json` — TerritoryDeleteById

Delete territory by URL ID — success response

```json
{
  "territories": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "431581000000798016"
      },
      "message": "Given Territory Removed Successfully",
      "status": "success"
    }
  ]
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

Authentication failure error

```json
{
  "code": "AUTHENTICATION_FAILURE",
  "details": {},
  "message": "Authentication failed",
  "status": "error"
}
```
