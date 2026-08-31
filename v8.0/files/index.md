# Files

- [OpenAPI specification](files.yaml)
- [Upload files to ZFS](operations/uploadFiles/operation.md)
  - To upload one or more files to the Zoho File System (ZFS) in your Zoho CRM account. The API returns an encrypted file ID for each uploaded file, which you can use to attach the file to a file upload field, image upload field, or record image field through the Create or Update Records API. The file is uploaded using multipart/form-data with a required 'file' field containing the binary data of the file to be uploaded. The response includes the file ID, name, status, and other details. Can upload 10 files in a single request by repeating the 'file' field. Maximum file size is 20 MB.
  - [Examples](operations/uploadFiles/examples/)
- [Retrieve a file from ZFS](operations/getFile/operation.md)
  - To retrieve the binary content of a file stored in Zoho File System (ZFS) using its unique file ID. The file ID is provided as a required query parameter 'id'. If the file exists, the API returns the file's binary data along with appropriate headers indicating the MIME type and content disposition for download. If the file ID does not correspond to any file in ZFS, a 204 No Content response is returned. This endpoint is used to download files that have been previously uploaded to ZFS and associated with Zoho CRM records.
  - [Examples](operations/getFile/examples/)
