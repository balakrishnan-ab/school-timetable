from googleapiclient.http import MediaFileUpload

def upload_to_drive(service, file_path, folder_id=None):
    file_metadata = {'name': os.path.basename(file_path)}
    if folder_id:
        file_metadata['parents'] = [folder_id]
    
    media = MediaFileUpload(file_path, mimetype='text/csv')
    file = service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
    print(f"கோப்பு வெற்றிகரமாக பதிவேற்றப்பட்டது. ID: {file.get('id')}")
