from django.db import transaction
from curso.models import Curso, Disciplina, Docente, AreaCientifica, LinguagemProgramacao, Projeto
import json

def importar_curso(ficheiro_json):
    with open(ficheiro_json, 'r') as file:
        data = json.load(file)

        # Importar os dados do curso
        try:
            with transaction.atomic():
                # Criar uma nova instância de Curso
                curso = Curso.objects.create(
                    apresentacao=data['courseDetail']['presentation'],
                    objetivos=data['courseDetail']['objectives'],
                    competencias=data['courseDetail']['competences']
                )

                # Importação de Áreas Científicas e Disciplinas
                for area in data['courseFlatPlan']:
                    area_cientifica = AreaCientifica.objects.create(
                        nome=area['curricularUnitName'],
                        descricao=f"Descrição para {area['curricularUnitName']}"
                    )

                    # Criar novas instâncias de Disciplina
                    disciplina = Disciplina.objects.create(
                        nome=area['curricularUnitName'],
                        ano=area['curricularYear'],
                        semestre=area['semester'],
                        ects=area['ects'],
                        curricularUnitReadableCode=area['curricularIUnitReadableCode'],
                        area_cientifica=area_cientifica
                    )

                # Criar projetos se existirem no JSON
                if 'projects' in data:
                    for project in data['projects']:
                        Projeto.objects.create(
                            nome=project['nome'],
                            descricao=project['descricao'],
                            curso=curso
                        )

                print("Dados importados com sucesso!")
        except Exception as e:
            print(f"Erro ao importar dados: {e}")
