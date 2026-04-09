import os.path
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# கூகுள் டிரைவ் அணுகல் அளவு (Scope)
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def get_drive_service():
    creds = None
    # ஏற்கனவே லாகின் செய்திருந்தால் 'token.pickle' கோப்பில் இருக்கும்
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            
    # லாகின் செய்யவில்லை என்றால் அல்லது அனுமதி முடிந்திருந்தால்
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # credentials.json என்பது நீங்கள் கூகுள் கிளவுட்டில் இருந்து பெற வேண்டியது
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # அடுத்த முறை லாகின் செய்யத் தேவையில்லாமல் சேமித்து வைக்கும்
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('drive', 'v3', credentials=creds)
