# Examples: getEmailDrafts

**GET /{module}/{record}/__email_drafts**

## Response examples

### Status `200` — `application/json` — Default

Example response with one draft

```json
{
  "__email_drafts": [
    {
      "id": "4f8efdcbaf23fd33c939217d4e14222d6d1cb21e4a45914fb9ba0c31c3c47330",
      "modified_time": "2023-11-09T14:45:25+05:30",
      "created_time": "2023-11-09T12:30:00+05:30",
      "from": "patricia.boyle@zylker.com",
      "to": [
        {
          "user_name": "user1",
          "email": "user1@zylker.com"
        }
      ],
      "reply_to": "pat.boyle@zylker.com",
      "cc": [
        {
          "user_name": "user2",
          "email": "user2@zylker.com"
        }
      ],
      "bcc": [
        {
          "user_name": "user3",
          "email": "user3@zylker.com"
        }
      ],
      "schedule_details": {
        "time": "2023-11-30T18:40:00+05:30",
        "timezone": "Asia/Calcutta",
        "source": "upTime"
      },
      "subject": "Test Draft Subject",
      "summary": "This is the email content.",
      "$sharing_permission": "full_access",
      "rich_text": true,
      "source": "",
      "inventory_details": null,
      "attachments": [
        {
          "id": "0b9e5596cdd8cafe6a5c09f78f095bd6434c863110a6d1e094285c6ebf9dd0d5",
          "file_name": "attachment.txt",
          "file_size": "8990",
          "service_name": "ZFSAttached"
        }
      ],
      "content": "This is the email content.",
      "linked_record": null,
      "owner": {
        "id": "2309216000000012345",
        "name": "Patricia Boyle"
      }
    }
  ],
  "info": {
    "page": 1,
    "per_page": 10,
    "count": 1,
    "more_records": false
  }
}
```

### Status `400` — `application/json` — InvalidModule

Invalid module name

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

Invalid record ID

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

### Status `400` — `application/json` — InvalidSortBy

sort_by value does not match the allowed pattern

```json
{
  "code": "PATTERN_NOT_MATCHED",
  "message": "Please check whether the input values are correct",
  "status": "error",
  "details": {
    "param_name": "sort_by"
  }
}
```

### Status `400` — `application/json` — InvalidSortOrder

sort_order value does not match the allowed pattern

```json
{
  "code": "PATTERN_NOT_MATCHED",
  "message": "Please check whether the input values are correct",
  "status": "error",
  "details": {
    "param_name": "sort_order"
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
