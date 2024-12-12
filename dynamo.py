from datetime import datetime, timedelta

now = datetime.now()
list_execucao_7_dias = []
list_execucao_1_dias = []

for item in items:
    data_agendamento = datetime.strptime(item['data_hora_agem'], '%Y-%m-%d:%H:%M:%S').date()
    data_agendamento_mais_7_dias = data_agendamento + timedelta(days=7)
    data_agendamento_mais_1_dias = data_agendamento + timedelta(days=1)

    if data_agendamento_mais_7_dias == (now + timedelta(days=7)).date():
        list_execucao_7_dias.append({
            'runbook_id': item['runbook_id'],
            'agendamento_id': item['agendamento_id'],
            'template': 'sete_dias'
        })

    if data_agendamento_mais_1_dias == (now + timedelta(days=1)).date():
        list_execucao_1_dias.append({
            'runbook_id': item['runbook_id'],
            'agendamento_id': item['agendamento_id'],
            'template': 'um_dia'
        })
