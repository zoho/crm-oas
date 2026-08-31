# Audit Log Export

- [OpenAPI specification](audit_log_export.yaml)
- [Create an audit log export job](operations/createAuditLogExport/operation.md)
  - To create an asynchronous audit log export job in your Zoho CRM organization. The system schedules the job and returns a unique job ID with a SCHEDULED status code. Use the[Get Audit Log Export API](audit_log_export.yaml#.$./paths./settings/audit_log_export.get) to poll for completion and retrieve the download links.
  - [Examples](operations/createAuditLogExport/examples/)
- [Get audit log export jobs](operations/getAuditLogExports/operation.md)
  - To retrieve the list of all audit log export jobs in your Zoho CRM organization, along with their status, filter criteria, and download links.
  - [Examples](operations/getAuditLogExports/examples/)
- [Get the Status of the Export Audit Log Job](operations/getAuditLogExportsById/operation.md)
  - Retrieves the details of a specific audit log export job in your Zoho CRM organization by its ID, including its status, filter criteria, and download link(s).
  - [Examples](operations/getAuditLogExportsById/examples/)
