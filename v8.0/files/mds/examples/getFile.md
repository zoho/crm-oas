# Examples: getFile

**GET /files**

## Response examples

### Status `400` — `application/json` — MissingIdParameter

Missing id parameter (regular mode)

```json
{
  "status": "error",
  "code": "REQUIRED_PARAM_MISSING",
  "message": "One of the expected parameter is missing",
  "details": {
    "param_name": "id"
  }
}
```

### Status `400` — `application/json` — MissingEmailTemplateAttachId

Missing attach_id parameter

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "required attachment id param not found",
  "details": {
    "param_name": "attach_id"
  }
}
```

### Status `400` — `application/json` — MissingEmailTemplateTemplateId

Missing template_id parameter

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "required template id param not found",
  "details": {
    "param_name": "template_id"
  }
}
```

### Status `400` — `application/json` — MissingEmailTemplateFileId

Missing file_id parameter

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "required file id param not found",
  "details": {
    "param_name": "file_id"
  }
}
```
