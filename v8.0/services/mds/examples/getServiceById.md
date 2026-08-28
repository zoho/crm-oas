# Examples: getServiceById

**GET /Services__s/{id}**

## Response examples

### Status `200` — `application/json` — Success200

Successful retrieval of a service record by ID


```json
{
  "data": [
    {
      "Job_Sheet_Required": "No",
      "Owner": {
        "name": "Madeshwaran G",
        "id": "4671651000000635001",
        "email": "madeshwaran.g@zohocorp.com"
      },
      "Description": null,
      "$currency_symbol": "£",
      "$field_states": null,
      "$photo_id": null,
      "Available_Days": [],
      "Tax": [],
      "$sharing_permission": "full_access",
      "Unavailable_From": "2026-01-14T12:20:35+05:30",
      "Last_Activity_Time": "2026-01-14T16:57:16+05:30",
      "Record_Image": null,
      "Modified_By": {
        "name": "Madeshwaran G",
        "id": "4671651000000635001",
        "email": "madeshwaran.g@zohocorp.com"
      },
      "$state": "save",
      "id": "4671651000000867004",
      "Available_Dates": [],
      "Status": "Not in Use",
      "Modified_Time": "2026-01-14T16:57:16+05:30",
      "Available_Timings": null,
      "Service_Name": "dd",
      "Available_From": "2026-01-01",
      "Created_Time": "2025-12-17T12:20:24+05:30",
      "Available_Till": "2026-01-29",
      "$editable": true,
      "Duration": 120,
      "Job_Sheet_Section__s": null,
      "Price": 44,
      "$status": "cmv_1-1",
      "$formatted_currency": {
        "Price": "44.00"
      },
      "Created_By": {
        "name": "Madeshwaran G",
        "id": "4671651000000635001",
        "email": "madeshwaran.g@zohocorp.com"
      },
      "Tag": [],
      "Availability_Type": "Specific Date Range",
      "Members": [
        {
          "id": "4671651000000867005",
          "Members": {
            "module": "Users",
            "name": "Madeshwaran G",
            "id": "4671651000000635001"
          }
        }
      ],
      "$home_converted_currency": null,
      "Location": "Business Address",
      "Unavailable_Till": null,
      "$has_more": {
        "Members": false
      }
    }
  ]
}
```

### Status `400` — `application/json` — InvalidModuleResponse1

An error response for an invalid module name in the request URL


```json
{
  "code": "INVALID_MODULE",
  "details": {
    "resource_path_index": 0
  },
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — RequiredParamMissingResponse1

An error response for a missing required query parameter


```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "fields"
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
}
```
