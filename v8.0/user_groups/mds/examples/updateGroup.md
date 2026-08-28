# Examples: updateGroup

**PUT /settings/user_groups/{group}**

## Request examples

### `application/json` — UpdateGroupExample

Update a user group name, description, and sources

```json
{
  "user_groups": [
    {
      "name": "Updated Sales Team",
      "description": "Updated sales department user group",
      "sources": [
        {
          "type": "users",
          "source": {
            "id": "3652397000000186017"
          }
        },
        {
          "type": "roles",
          "source": {
            "id": "3652397000000026008"
          },
          "subordinates": true
        }
      ]
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — SuccessWithId

User group updated successfully

```json
{
  "user_groups": [
    {
      "code": "SUCCESS",
      "message": "User group updated successfully",
      "status": "success",
      "details": {
        "id": "3652397000009949005"
      }
    }
  ]
}
```

### Status `400` — `application/json` — InvalidData

Invalid group ID in request URL

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "The provided group ID is invalid.",
  "status": "error"
}
```

### Status `400` — `application/json` — SourceError

Invalid source ID in sources array

```json
{
  "user_groups": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.user_groups[0].source[0].id"
      },
      "message": "The User Id given seems to be Invalid",
      "status": "error"
    }
  ]
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
