# Examples: createEmailDrafts

**POST /{module}/{record}/__email_drafts**

## Request examples

### `application/json` — CreateDraft

Example request to create email drafts

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

### Status `201` — `application/json` — Success

Successful Creation

```json
{
  "__email_drafts": [
    {
      "code": "SUCCESS",
      "message": "Draft created Successfully",
      "status": "success",
      "details": {
        "id": "4f8efdcbaf23fd33c939217d4e14222d6d1cb21e4a45914fb9ba0c31c3c47330"
      }
    }
  ]
}
```

### Status `207` — `application/json` — MixedResults

Batch response with both successful and failed draft updates

```json
{
  "__email_drafts": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "bb08599ae908a3fc514349239ebd0dbf82a1fd0b60a7902244cf0ee6b52a88d1"
      },
      "message": "Draft updated Successfully",
      "status": "success"
    },
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "from",
        "json_path": "$.__email_drafts[1].from"
      },
      "message": "required field not found",
      "status": "error"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "bb08599ae908a3fc514349239ebd0dbf82a1fd0b60a7902244cf0ee6b52a88d1"
      },
      "message": "Draft updated Successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundFrom

Batch - from is required

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

### Status `400` — `application/json` — MandatoryNotFoundRichText

Batch - rich_text is required

```json
{
  "__email_drafts": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "required field not found",
      "status": "error",
      "details": {
        "api_name": "rich_text",
        "json_path": "$.__email_drafts[0].rich_text"
      }
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundToEmail

Batch - to[].email is required

```json
{
  "__email_drafts": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "required field not found",
      "status": "error",
      "details": {
        "api_name": "email",
        "json_path": "$.__email_drafts[0].to[0].email"
      }
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundCcEmail

Batch - cc[].email is required

```json
{
  "__email_drafts": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "required field not found",
      "status": "error",
      "details": {
        "api_name": "email",
        "json_path": "$.__email_drafts[0].cc[0].email"
      }
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundBccEmail

Batch - bcc[].email is required

```json
{
  "__email_drafts": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "required field not found",
      "status": "error",
      "details": {
        "api_name": "email",
        "json_path": "$.__email_drafts[0].bcc[0].email"
      }
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundAttachmentId

Batch - attachments[].id is required

```json
{
  "__email_drafts": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "required field not found",
      "status": "error",
      "details": {
        "api_name": "id",
        "json_path": "$.__email_drafts[0].attachments[0].id"
      }
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundAttachmentFileName

Batch - attachments[].file_name is required

```json
{
  "__email_drafts": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "required field not found",
      "status": "error",
      "details": {
        "api_name": "file_name",
        "json_path": "$.__email_drafts[0].attachments[0].file_name"
      }
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundScheduleTime

Batch - schedule_details.time is required

```json
{
  "__email_drafts": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "required field not found",
      "status": "error",
      "details": {
        "api_name": "time",
        "json_path": "$.__email_drafts[0].schedule_details.time"
      }
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundInventoryTemplate

Batch - inventory_details.inventory_template is required

```json
{
  "__email_drafts": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "required field not found",
      "status": "error",
      "details": {
        "api_name": "inventory_template",
        "json_path": "$.__email_drafts[0].inventory_details.inventory_template"
      }
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataFromEmail

Batch - from is not a valid email

```json
{
  "__email_drafts": [
    {
      "code": "INVALID_DATA",
      "message": "invalid email",
      "status": "error",
      "details": {
        "api_name": "from",
        "json_path": "$.__email_drafts[0].from"
      }
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataReplyToEmail

Batch - reply_to is not a valid email

```json
{
  "__email_drafts": [
    {
      "code": "INVALID_DATA",
      "message": "invalid email",
      "status": "error",
      "details": {
        "api_name": "reply_to",
        "json_path": "$.__email_drafts[0].reply_to"
      }
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataToEmail

Batch - to[].email is not a valid email

```json
{
  "__email_drafts": [
    {
      "code": "INVALID_DATA",
      "message": "invalid email",
      "status": "error",
      "details": {
        "api_name": "email",
        "json_path": "$.__email_drafts[0].to[0].email"
      }
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataPaperType

Batch - inventory_details.paper_type value is invalid

```json
{
  "__email_drafts": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "status": "error",
      "details": {
        "api_name": "paper_type",
        "json_path": "$.__email_drafts[0].inventory_details.paper_type"
      }
    }
  ]
}
```

### Status `400` — `application/json` — InvalidFrom

Batch - from not in allowed address list (API layer)

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

### Status `400` — `application/json` — InvalidModule

Generic - invalid module name

```json
{
  "code": "INVALID_MODULE",
  "message": "the module name given seems to be invalid",
  "status": "error",
  "details": {
    "resource_path_index": 0
  }
}
```

### Status `400` — `application/json` — InvalidRecord

Generic - invalid record ID

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
