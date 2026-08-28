# Examples: postDownloadMailMerge

**POST /{moduleApiName}/{recordId}/actions/download_mail_merge**

## Request examples

### `application/json` — SamplePostRequest

Download mail merge request body

```json
{
  "download_mail_merge": [
    {
      "mail_merge_template": {
        "name": "mailmergename"
      },
      "output_format": "pdf",
      "file_name": "testdocument",
      "password": "tester123"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

Example of a successful download mail merge response.

```json
{
  "download_mail_merge": [
    {
      "code": "SUCCESS",
      "message": "download mail merge action initiated successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — Error400

Example of a missing required field error response.

```json
{
  "download_mail_merge": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "mail_merge_template",
        "json_path": "$.download_mail_merge[0].mail_merge_template"
      },
      "message": "Required field is missing",
      "status": "error"
    }
  ]
}
```
