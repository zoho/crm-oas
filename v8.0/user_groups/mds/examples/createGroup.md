# Examples: createGroup

**POST /settings/user_groups**

## Request examples

### `application/json` — CreateGroupExample

Create a user group with role and territory sources

```json
{
  "user_groups": [
    {
      "name": "Sales Team",
      "description": "Sales department user group",
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

### Status `201` — `application/json` — SuccessWithId

User group created successfully

```json
{
  "user_groups": [
    {
      "code": "SUCCESS",
      "message": "User group created successfully",
      "status": "success",
      "details": {
        "id": "3652397000009949005"
      }
    }
  ]
}
```

### Status `400` — `application/json` — CreateGroupError

Invalid request body for group creation

```json
{
  "user_groups": [
    {
      "status": "error",
      "code": "DUPLICATE_DATA",
      "message": "A user group with the same name already exists.",
      "details": {
        "api_name": "name",
        "json_path": "$.user_groups[0].name"
      }
    }
  ]
}
```
