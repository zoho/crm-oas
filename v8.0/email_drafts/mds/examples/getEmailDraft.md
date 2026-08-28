# Examples: getEmailDraft

**GET /{module}/{record}/__email_drafts/{draft}**

## Response examples

### Status `200` — `application/json` — Default

Example response for a single email draft

```json
{
  "__email_drafts": [
    {
      "id": "4f8efdcbaf23fd33c939217d4e14222d6d1cb21e4a45914fb9ba0c31c3c47330",
      "modified_time": "2023-11-09T14:45:25+05:30",
      "created_time": "2023-11-09T14:45:25+05:30",
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
          "user_name": "user4",
          "email": "user4email@zoho.com"
        }
      ],
      "$sharing_permission": "full_access",
      "inventory_details": null,
      "attachments": [
        {
          "file_name": "attachment.txt",
          "service_name": "ZFSAttached",
          "id": "0b9e5596cdd8cafe6a5c09f78f095bd6434c863110a6d1e094285c6ebf9dd0d5",
          "file_size": "8990"
        }
      ],
      "schedule_details": {
        "time": "2023-11-30T18:40:00+05:30"
      },
      "rich_text": true,
      "subject": "Test Draft",
      "content": "This is the email content.",
      "summary": "This is the email content.",
      "owner": {
        "id": "4567890123",
        "name": "Owner Name"
      },
      "source": "",
      "linked_record": null
    }
  ]
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

### Status `400` — `application/json` — InvalidRelatedID

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
