# Examples: updateEmailDrafts

**PUT /{module}/{record}/__email_drafts/{draft}**

## Request examples

### `application/json` — UpdateDraft

Example request to update a single email draft

```json
{
  "__email_drafts": [
    {
      "from": "john@example.com",
      "to": [
        {
          "user_name": "John Doe",
          "email": "john.doe@example.com"
        }
      ],
      "reply_to": null,
      "cc": [],
      "bcc": [],
      "inventory_details": null,
      "schedule_details": null,
      "rich_text": true,
      "subject": "Test Subject",
      "content": "<p>Hello!</p>"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success

Successful update

```json
{
  "__email_drafts": [
    {
      "code": "SUCCESS",
      "message": "Draft updated Successfully",
      "status": "success",
      "details": {
        "id": "4f8efdcbaf23fd33c939217d4e14222d6d1cb21e4a45914fb9ba0c31c3c47330"
      }
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFound

Batch error - required field missing

```json
{
  "__email_drafts": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "required field not found",
      "status": "error",
      "details": {
        "api_name": "from",
        "json_path": "$.__email_drafts[0].from"
      }
    }
  ]
}
```

### Status `400` — `application/json` — InvalidFrom

Batch error - invalid from address

```json
{
  "__email_drafts": [
    {
      "code": "INVALID_DATA",
      "message": "Email can't be saved as draft using this from address.Kindly check the allowed from address list",
      "status": "error",
      "details": {
        "api_name": "from"
      }
    }
  ]
}
```

### Status `400` — `application/json` — InventoryNotAllowed

Batch error - inventory_details not allowed in update (API layer)

```json
{
  "__email_drafts": [
    {
      "code": "NOT_ALLOWED",
      "message": "The inventory_details field is not allowed in update draft request.",
      "status": "error",
      "details": {
        "api_name": "inventory_details",
        "json_path": "$.__email_drafts[0].inventory_details"
      }
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDraftId

Generic error - invalid draft ID in URL

```json
{
  "code": "INVALID_DATA",
  "message": "invalid draft id in the url",
  "status": "error",
  "details": {
    "resource_path_index": 3
  }
}
```

### Status `400` — `application/json` — InvalidData

Generic error - invalid path parameter

```json
{
  "code": "INVALID_DATA",
  "message": "the related id given seems to be invalid",
  "status": "error",
  "details": {
    "resource_path_index": 1
  }
}
```

### Status `403` — `application/json` — NoPermission

No permission to access resource

```json
{
  "code": "NO_PERMISSION",
  "message": "Please contact your admin",
  "status": "error",
  "details": {}
}
```
