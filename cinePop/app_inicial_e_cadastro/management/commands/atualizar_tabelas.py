import requests
from django.core.management.base import BaseCommand
from app_inicial_e_cadastro.models import Categoria, Ator, Avaliacao, Diretor, Filme, Nacionalidade, Usuario

class Command(BaseCommand):
    help = 'Atualiza a tabela de Nacionalidades no banco de dados'

    def handle(self, *args, **kwargs):
        self.atualizar_nacionalidades()

    def atualizar_nacionalidades(self):
        api_key = '02060eb776090fd24272888c1f1cf44e'
        base_url = 'https://api.themoviedb.org/3/configuration/countries'

        params = {
            'api_key': api_key,
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        for country_data in data:
            nacionalidade, created = Nacionalidade.objects.get_or_create(
                id_nacionalidade=country_data.get('iso_3166_1'),
                nacionalidade=country_data.get('english_name', ''),
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Nacionalidade "{nacionalidade.nacionalidade}" adicionada ao banco de dados.'))






