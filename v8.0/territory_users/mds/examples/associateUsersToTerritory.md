# Examples: associateUsersToTerritory

**PUT /settings/territories/{territory}/users**

## Request examples

### `application/json` — UserAssociationViaRequestBody

Example request body to associate users to a territory

```json
{
  "users": [
    {
      "id": "111111000000042726"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — SuccessExample

Example success response for adding user to Territory

```json
{
  "users": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000044193"
      },
      "message": "Given User added to the mentioned territory Successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateUserAddition

Example error response for adding existing user to Territory

```json
{
  "users": [
    {
      "code": "DUPLICATE_DATA",
      "message": "Given user id already exists for that record",
      "status": "error",
      "details": {
        "api_name": "id",
        "json_path": "$.users[0].id"
      }
    }
  ]
}
```

### Status `400` — `application/json` — LimitExceeded

Example error response for Limit Exceeded

```json
{
  "users": [
    {
      "code": "LIMIT_EXCEEDED",
      "message": "Maximum Users Limit reached for a territory",
      "details": {
        "limit": 100
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidUserAddition

Invalid User Addition

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.users[0].id",
        "owner_status": "deleted"
      },
      "message": "The user to whom you are trying to update is deleted.",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — TerritoryNotYetEnabled

Example For Territory Not yet Enabled

```json
{
  "code": "TERRITORY_NOT_ENABLED",
  "details": {},
  "message": "the territory feature is not enabled",
  "status": "error"
}
```

### Status `403` — `application/json` — TerritoryDisabled

Example For Territory Diabled Error

```json
{
  "code": "TERRITORY_DISABLED",
  "details": {},
  "message": "the territory feature is disabled",
  "status": "error"
}
```

### Status `500` — `application/json` — InternalServerError

Internal Server Error

```json
{
  "code": "INTERNAL_SERVER_ERROR",
  "details": {},
  "message": "",
  "status": "error"
}
```
