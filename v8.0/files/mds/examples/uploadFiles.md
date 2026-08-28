# Examples: uploadFiles

**POST /files**

## Response examples

### Status `200` — `application/json` — SingleFileUpload

Single file upload

```json
{
  "data": [
    {
      "status": "success",
      "code": "SUCCESS",
      "message": "invoice_2024_Q4.pdf uploaded successfully",
      "details": {
        "name": "invoice_2024_Q4.pdf",
        "id": "ae9c6cd994aa55a0fda90faaff4a2f472b1c94e7"
      }
    }
  ]
}
```

### Status `200` — `application/json` — MultiFileUpload

Multiple files upload

```json
{
  "data": [
    {
      "status": "success",
      "code": "SUCCESS",
      "message": "contract.pdf uploaded successfully",
      "details": {
        "name": "contract.pdf",
        "id": "ae9c6cd994aa55a0fda90faaff4a2f472b1c94e7"
      }
    },
    {
      "status": "success",
      "code": "SUCCESS",
      "message": "signature.png uploaded successfully",
      "details": {
        "name": "signature.png",
        "id": "bf8d7de885bb66b1feb91fbbgg5b3g583c2d85f8"
      }
    }
  ]
}
```

### Status `400` — `application/json` — MissingFileField

Missing 'file' field in request

```json
{
  "code": "failure_in_attachment_handling",
  "details": {},
  "message": "Problem in uploading attachment. kindly upload the file properly",
  "status": "error"
}
```

### Status `400` — `application/json` — EmptyFileField

Empty 'file' field with no data

```json
{
  "code": "failure_in_attachment_handling",
  "details": {},
  "message": "Problem in uploading attachment. kindly upload the file properly",
  "status": "error"
}
```

### Status `400` — `application/json` — TooManyFiles

Exceeds ten-file limit

```json
{
  "code": "INVALID_REQUEST",
  "details": {},
  "message": "unable to process your request. please verify whether you have entered proper method name, parameter and parameter values.",
  "status": "error"
}
```

### Status `415` — `application/json` — FileTooLarge

File exceeds size limit

```json
{
  "code": "FILE_SIZE_MORE_THAN_ALLOWED_SIZE",
  "details": {},
  "message": "Please check if the size of the file is in the correct range",
  "status": "error"
}
```
