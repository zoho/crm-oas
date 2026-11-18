DEPENDENT_INDEX_MISMATCH error when Password precedes Confirm Password out of order

```json
{
  "webforms": [
    {
      "code": "DEPENDENT_INDEX_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "password",
          "json_path": "$.webforms[0].form_fields[0].password"
        },
        "api_name": "confirm_password",
        "json_path": "$.webforms[0].form_fields[2].confirm_password"
      },
      "message": "Password and Confirm Password cannot be re-ordered. Expected Order: Password, Confirm Password",
      "status": "error"
    }
  ]
}
```
