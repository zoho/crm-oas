# Examples: uploadRecordPhoto

**POST /{module}/{record}/photo**

## Response examples

### Status `200` — `application/json` — SuccessResponse

Upload record photo success

```json
{
  "code": "SUCCESS",
  "message": "Photo uploaded successfully",
  "status": "success",
  "details": {}
}
```

### Status `400` — `application/json` — InvalidUrlPattern

Upload record photo with invalid URL pattern

```json
{
  "code": "INVALID_URL_PATTERN",
  "message": "Please check if the URL trying to access is a correct one",
  "status": "error",
  "details": {}
}
```

### Status `400` — `application/json` — CannotPerformAction

Upload record photo with no permission

```json
{
  "code": "CANNOT_PERFORM_ACTION",
  "details": {},
  "message": "no permission to perform an action on this record",
  "status": "error"
}
```

### Status `400` — `application/json` — UnderReviewProcess

Upload record photo for record under review process

```json
{
  "code": "NOT_REVIEWED",
  "details": {
    "id": "111111000000091108"
  },
  "message": "cannot upload the record image that is not reviewed yet",
  "status": "error"
}
```

### Status `400` — `application/json` — UnderApprovalProcess

Upload record photo for record under Approval Process

```json
{
  "code": "NOT_APPROVED",
  "details": {
    "id": "111111000000091057"
  },
  "message": "cannot upload the record image that is not approved yet",
  "status": "error"
}
```

### Status `400` — `application/json` — UnderRecordLockingFeature

Upload record photo for locked record

```json
{
  "code": "RECORD_LOCKED",
  "details": {
    "id": "111111000000091019"
  },
  "message": "Sorry, you cannot perform this operation as the record is locked.",
  "status": "error"
}
```

### Status `413` — `application/json` — FileSizeExceeds

Upload record photo with file size exceeded

```json
{
  "code": "FILE_SIZE_EXCEEDS",
  "details": {
    "size": 10485760
  },
  "message": "File exceeded its maximum limit",
  "status": "error"
}
```

### Status `415` — `application/json` — FileResolutionExceeds

Upload record photo with file resolution exceeded

```json
{
  "code": "FILE_RESOLUTION_EXCEEDS",
  "details": {
    "resolution": 16062248
  },
  "message": "File exceeded its maximum limit",
  "status": "error"
}
```

### Status `415` — `application/json` — InvalidFileType

Upload record photo with invalid file type

```json
{
  "code": "INVALID_DATA",
  "details": {},
  "message": "invalid file type",
  "status": "error"
}
```
