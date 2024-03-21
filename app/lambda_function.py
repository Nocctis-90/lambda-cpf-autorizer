import json

def AutenticacaoClienteHandler(event, autenticacaoClienteUC, consultarClienteUC):
    # Verificar se o ID do cliente está presente no evento recebido
    if 'id_cliente' not in event['pathParameters']:
        return {
            'statusCode': 400,
            'body': json.dumps({'mensagem': 'ID do cliente não fornecido'})
        }

    # Recuperar o ID do cliente do evento
    id_cliente = event['pathParameters']['id_cliente']

    # Lógica de autenticação do cliente (exemplo simplificado)
    # Aqui você pode adicionar sua lógica de autenticação de cliente
    # Neste exemplo, vamos apenas retornar um JSON indicando que o cliente foi autenticado com sucesso
    return {
        'statusCode': 200,
        'body': json.dumps({'mensagem': 'Cliente autenticado com sucesso', 'id_cliente': id_cliente})
    }