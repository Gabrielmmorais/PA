import gspread
from gspread_formatting.dataframe import format_with_dataframe
from gspread_formatting.dataframe import Color
from google.oauth2.service_account import Credentials
from test1 import busca_campos, busca_child

# Autenticar
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file('chave.json', scopes=scope)
client = gspread.authorize(creds)
#planilha = client.open_by_key('1vBMQjgNj2cCbIskiFd4z1AsTu0se0NhGDkw51eTZP6Y').sheet1

fields = busca_campos(662753948)

valores = [fields.get('turma', ''), fields.get('data_e_hora_de_in_cio', ''), fields['data_e_hora_de_t_rmino'], fields['turmas'], fields['treinamento']]
    #print(fields)
    #print(valores)

relation=busca_child(662753948)
print(relation)

turmas=(relation.get("351378542"))
for turma in turmas:
    #print(turma)
    id_turma=turma.get("id")
    campos_turma=busca_campos(id_turma)
    nturma=campos_turma.get("turma")
    rturma=busca_child(id_turma)
    #print(rturma)
    produto=rturma.get("345507680")
    modulos=rturma.get("345508510")
    nproduto=produto[0].get("title")

planilha = client.create(nproduto + " " + nturma + " Lista de presença SBPNL")

planilha.share('sbpnl.listas@gmail.com', perm_type='user', role='writer')

print(planilha.id)
planilha.sheet1.update('A1', nproduto + " " + nturma + " Lista de presença SBPNL" )

lista = ['aluno', 'Mod1', 'Mod2', 'Mod3', 'Mod4', 'Mod5' , 'Mod6', 'Mod7', 'Mod8', 'Mod9', 'Mod10', 'Mod11',
         'Mod12', 'Mod13', 'Mod14', 'Mod15', 'Mod16', 'Mod17', 'Mod18', 'Mod19', 'Mod20']
planilha.sheet1.update('A2:U2', [lista])


def change_background_color(sheet):
    # Define the range A2:U2
    range_to_format = 'A2:U2'
    
    # Define the background color (black)
    background_color = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    
    # Create a format request
    format_request = {
        "backgroundColor": background_color
    }
    
    # Apply the format request to the range
    sheet.format(range_to_format, format_request)