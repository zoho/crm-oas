# Examples: getUsers

**GET /users**

## Response examples

### Status `200` — `application/json` — UsersGetResponse

Successful retrieval of a paginated list of users

```json
{
  "users": [
    {
      "role": {
        "name": "CEO",
        "id": "111133000000000861"
      },
      "microsoft": false,
      "locale": "en_US",
      "Modified_By": {
        "name": "Thuvassshhhh test test",
        "id": "111133000000057662"
      },
      "$shift_effective_from": null,
      "$current_shift": {
        "id": "111133000000012345",
        "name": "Morning Shift"
      },
      "alias": "aaaa",
      "id": "111133000000057662",
      "sandboxDeveloper": false,
      "first_name": "Thuvassshhhh",
      "email": "user@example.com",
      "Reporting_To": null,
      "status_reason__s": null,
      "decimal_separator": "Period",
      "created_time": "2025-11-12T11:20:12+05:30",
      "Modified_Time": "2025-12-08T16:53:16+05:30",
      "image_link": "https://profile.csez.zohocorpin.com/file?ID=43318041&fs=thumb",
      "$next_shift": {
        "id": "111133000000023456",
        "name": "Evening Shift"
      },
      "profile": {
        "name": "Administrator",
        "id": "111133000000000497"
      },
      "last_name": "test test",
      "created_by": {
        "name": "Thuvassshhhh test test",
        "id": "111133000000057662"
      },
      "zuid": "43318041",
      "confirm": true,
      "full_name": "Thuvassshhhh test test",
      "phone": null,
      "date_format": "MM/dd/yyyy",
      "status": "disabled",
      "type__s": "Regular User"
    }
  ],
  "info": {
    "per_page": 200,
    "count": 1,
    "page": 1,
    "more_records": false
  }
}
```

### Status `400` — `application/json` — InvalidDataErrorResponse

400 error for an invalid query_id parameter value

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "query_id"
  },
  "message": "Invalid queryId",
  "status": "error"
}
```

### Status `400` — `application/json` — DependentFieldMissingErrorResponse

Missing required dependent parameter triggers a 400 error

```json
{
  "code": "DEPENDENT_PARAM_MISSING",
  "details": {
    "dependee": {
      "param_name": "child_data"
    },
    "param_name": "query_id"
  },
  "message": "Dependent Param missing",
  "status": "error"
}
```
