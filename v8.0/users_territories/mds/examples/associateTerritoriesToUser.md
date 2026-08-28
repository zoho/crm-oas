# Examples: associateTerritoriesToUser

**PUT /users/{user}/territories**

## Request examples

### `application/json` — AssociateTerritoriesExample

Associate territories with a user

```json
{
  "territories": [
    {
      "id": "111121000000076093"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — AssociateTerritoriesExample

Successful territory association response

```json
{
  "territories": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111121000000076093"
      },
      "message": "Territory associated to the user successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidTerritoryIdErrorResponse

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

### Status `400` — `application/json` — AlreadyAssociatedTerritoryErrorResponse

Duplicate territory association error

```json
{
  "territories": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.territories[0].id"
      },
      "message": "Territory already associated with the user",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — PermissionDeniedError

Permission denied error for territory

```json
{
  "territories": [
    {
      "code": "PERMISSION_DENIED",
      "details": {
        "api_name": "id",
        "json_path": "$.territories[0].id"
      },
      "message": "User does not have update/delete permission for the territory",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — LoggedInUserCannotUpdateTerritories

Logged-in user cannot update their own territories

```json
{
  "code": "NOT_ALLOWED",
  "details": {},
  "message": "Logged in user can't update their territories",
  "status": "error"
}
```
