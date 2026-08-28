# Examples: deassociateUsersFromTerritories

**DELETE /settings/territories/{territory}/users**

## Response examples

### Status `200` — `application/json` — SuccessExample

```json
{
  "users": [
    [
      {
        "code": "SUCCESS",
        "details": {
          "id": "111111000000044193"
        },
        "message": "Given User Removed from the mentioned territory Successfully",
        "status": "success"
      },
      {
        "code": "SUCCESS",
        "details": {
          "id": "111111000000044453"
        },
        "message": "Given User Removed from the mentioned territory Successfully",
        "status": "success"
      }
    ]
  ]
}
```

### Status `400` — `application/json` — UserNotPartOfTerritory

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "message": "Given user is not a member of this territory.",
      "details": {
        "id": "111111000000044473"
      },
      "status": "error"
    },
    {
      "code": "INVALID_DATA",
      "message": "Given user is not a member of this territory.",
      "details": {
        "id": "111111000000084453"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidUserIds

Invalid User ID

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "message": "the given user id given seems to be invalid",
      "details": {
        "id": "111111000000084453"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidTerritoryId

Invalid Territory ID

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "message": "the given id given seems to be invalid",
      "details": {
        "resource_path_index": 2
      },
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
