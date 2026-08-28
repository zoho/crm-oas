# Examples: getAppointmentsS

**GET /Appointments__s**

## Response examples

### Status `200` — `application/json` — Success200

Successful retrieval of appointment records

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
      "Appointment_Start_Time": "2026-01-16T18:00:00+05:30",
      "Cancellation_Reason": null,
      "$field_states": null,
      "Appointment_For": {
        "module": {
          "api_name": "Contacts",
          "id": "111115000000002654"
        },
        "name": "ll",
        "id": "111115000000120725"
      },
      "Rescheduled_To": null,
      "$sharing_permission": "full_access",
      "Reschedule_Reason": null,
      "Job_Sheet_Name__s": null,
      "Additional_Information": null,
      "Last_Activity_Time": null,
      "Job_Sheet_Created__s": false,
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
      "id": "111115000000147279",
      "Rescheduled_Time": null,
      "Remind_At": null,
      "Appointment_End_Time": "2026-01-16T18:30:00+05:30",
      "Status": "Overdue",
      "Modified_Time": "2026-01-16T16:50:29+05:30",
      "Service_Name": {
        "name": "service06",
        "id": "111115000000127506"
      },
      "Created_Time": "2026-01-16T16:50:29+05:30",
      "Rescheduled_From": null,
      "Cancelled_By": null,
      "$editable": true,
      "Appointment_Name": "service06 - ll",
      "Duration": 30,
      "Job_Sheet_Section__s": "Job Sheet Information",
      "Record_Status__s": "Available",
      "$status": "cv_1",
      "Job_Sheet_Description__s": null,
      "Created_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Tag": [],
      "Location": "Business Address",
      "Reschedule_Note": null
    },
    {
      "Owner": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "$currency_symbol": "£",
      "Address": null,
      "Appointment_Start_Time": "2026-01-16T15:00:00+05:30",
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
      "Job_Sheet_Name__s": null,
      "Additional_Information": null,
      "Last_Activity_Time": null,
      "Job_Sheet_Created__s": false,
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
      "id": "111115000000147238",
      "Rescheduled_Time": null,
      "Remind_At": null,
      "Appointment_End_Time": "2026-01-16T15:30:00+05:30",
      "Status": "Overdue",
      "Modified_Time": "2026-01-16T14:11:13+05:30",
      "Service_Name": {
        "name": "service06",
        "id": "111115000000127506"
      },
      "Created_Time": "2026-01-16T14:11:13+05:30",
      "Rescheduled_From": null,
      "Cancelled_By": null,
      "$editable": true,
      "Appointment_Name": "hh",
      "Duration": 30,
      "Job_Sheet_Section__s": "Job Sheet Information",
      "Record_Status__s": "Available",
      "$status": "cv_1",
      "Job_Sheet_Description__s": null,
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

An error response for an invalid module API name.

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

### Status `400` — `application/json` — InvalidRequestMethodResponse1

An error response for an unsupported HTTP request method

```json
{
  "code": "INVALID_REQUEST_METHOD",
  "details": {},
  "message": "The http request method type is not a valid one",
  "status": "error"
}
```
