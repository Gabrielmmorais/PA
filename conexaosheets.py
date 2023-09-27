from __future__ import print_function

import os.path
from test1 import busca_campos, busca_child
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1vBMQjgNj2cCbIskiFd4z1AsTu0se0NhGDkw51eTZP6Y'
SAMPLE_RANGE_NAME = 'teste!A2:E'



"""Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

try:
    service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    fields = busca_campos(662753948)

    valores = [fields.get('turma', ''), fields.get('data_e_hora_de_in_cio', ''), fields['data_e_hora_de_t_rmino'], fields['turmas'], fields['treinamento']]
    #print(fields)
    #print(valores)

    relation=busca_child(662753948)
    print(relation)

except HttpError as err:
    print(err)



