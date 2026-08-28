# Examples: getAppointmentById

**GET /Appointments__s/{appointmentId}**

## Response examples

### Status `200` — `application/json` — Success200

Successful retrieval of a single appointment record by ID.


```json
{
  "data": [
    {
      "Owner": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "$currency_symbol": "£",
      "Address": null,
      "Appointment_Start_Time": "2026-01-11T14:30:00+05:30",
      "Cancellation_Reason": null,
      "$field_states": null,
      "Appointment_For": {
        "module": {
          "api_name": "Contacts",
          "id": "111115000000002654"
        },
        "name": "bb",
        "id": "111115000000120715"
      },
      "Rescheduled_To": null,
      "$sharing_permission": "full_access",
      "Reschedule_Reason": null,
      "Job_Sheet_Name__s": "ss",
      "Additional_Information": null,
      "Last_Activity_Time": null,
      "Job_Sheet_Created__s": true,
      "Cancelled_Time": null,
      "Cancellation_Note": null,
      "Modified_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Reschedule_Count": 0,
      "Rescheduled_By": null,
      "Date_1": null,
      "id": "111115000000147219",
      "Rescheduled_Time": null,
      "Remind_At": null,
      "Appointment_End_Time": "2026-01-11T16:30:00+05:30",
      "Status": "Completed",
      "Modified_Time": "2026-01-16T14:00:11+05:30",
      "Service_Name": {
        "name": "service03",
        "id": "111115000000127405"
      },
      "Created_Time": "2026-01-16T14:00:11+05:30",
      "Rescheduled_From": null,
      "Cancelled_By": null,
      "$editable": true,
      "Appointment_Name": "service-jobsheetcomplete",
      "Duration": 120,
      "Job_Sheet_Section__s": "Job Sheet Information",
      "$status": "cv_1",
      "Job_Sheet_Description__s": "done and dusted",
      "Created_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Tag": [],
      "Location": "Business Address",
      "Reschedule_Note": null
    }
  ]
}
```

### Status `400` — `application/json` — InvalidModuleResponse1

INVALID_MODULE error when module API name in the URL is invalid.

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

### Status `404` — `application/json` — InvalidUrlPatternResponse1

INVALID_URL_PATTERN error when the appointment ID in the URL is invalid.


```json
{
  "code": "INVALID_URL_PATTERN",
  "details": {},
  "message": "Please check if the URL trying to access is a correct one",
  "status": "error"
}
```
