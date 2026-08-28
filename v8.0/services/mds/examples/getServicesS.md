# Examples: getServicesS

**GET /Services__s**

## Response examples

### Status `200` — `application/json` — Success200

Successful response listing four service records

```json
{
  "data": [
    {
      "Job_Sheet_Required": "No",
      "Owner": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Description": null,
      "$currency_symbol": "£",
      "$field_states": null,
      "$photo_id": null,
      "Available_Days": [],
      "Tax": [],
      "$sharing_permission": "full_access",
      "Unavailable_From": null,
      "Last_Activity_Time": "2026-01-13T15:08:50+04:00",
      "Record_Image": null,
      "Modified_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "id": "111115000000127290",
      "Available_Dates": [],
      "Status": "Available",
      "Modified_Time": "2026-01-13T15:08:50+04:00",
      "Available_Timings": [
        {
          "From": "09:00",
          "To": "16:30"
        }
      ],
      "Service_Name": "service00",
      "Available_From": "2026-01-13",
      "$data_source_details": {},
      "Created_Time": "2026-01-13T10:51:09+04:00",
      "Available_Till": "2026-01-15",
      "$editable": true,
      "Duration": 30,
      "Job_Sheet_Section__s": null,
      "Record_Status__s": "Available",
      "Price": 34,
      "$status": "cmv_1-1",
      "Created_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Tag": [],
      "Availability_Type": "Specific Date Range",
      "Members": [
        {
          "id": "111115000000127292",
          "Members": {
            "module": "Users",
            "name": "madesh",
            "id": "111115000000122075"
          }
        },
        {
          "id": "111115000000127291",
          "Members": {
            "module": "Users",
            "name": "madesh04",
            "id": "111115000000058229"
          }
        }
      ],
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

An error response for an invalid module name


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

Anexample of error response for a missing required parameter


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
