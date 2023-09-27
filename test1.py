import requests

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjp7ImlkIjozMTA5NzgsImVtYWlsIjoicHJvY2Vzc29"
                     "zQHZpZXdub3cuY29tLmJyIiwiYXBwbGljYXRpb24iOjMwMDE1MjQ0OX19.qNcXyVtdII-aOwMuR7G2aw0MXg4Z84808X0FA"
                     "WA8hc6CYtV3rX_YEuPzopTTdk_ZDzGh6zGxRYycl3EAbKmidw"
}

url = 'https://api.pipefy.com/graphql'

def busca_campos(id_card):
    payload = {'query': 'query{card(id: ' + str(id_card) + '){child_relations{id name cards{'
                        'id title fields{name value field{id}}}}fields{name value field{id}}}}'}

    response = requests.post(url, json=payload, headers=headers).json()
    fields = response.get('data').get('card').get('fields')
    campos = {}
    for field in fields:
        campos.update({field.get('field').get('id'): field.get('value')})

    return campos

fields=busca_campos(662753948)
#print (fields)

def busca_child(id_card):
    query = """
    query{
        card(id:%s){
            child_relations{
                id
                name
                cards{
                    id
                    title
                    fields{
                        name
                        value
                        field{
                            id
                        }
                    }
                }
            }
        }
    }
    """ % id_card
    payload = {'query': query}
    response = requests.post(url, json=payload, headers=headers).json()
    childs = response.get('data').get('card').get('child_relations')
    relacoes = {}
    for child in childs:
        relacoes.update({str(child.get('id')): child.get('cards')})

    return relacoes

relation=busca_child(662753948)
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



