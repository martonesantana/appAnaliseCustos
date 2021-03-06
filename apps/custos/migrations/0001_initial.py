# Generated by Django 4.0.1 on 2022-03-15 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
        ('tax', '0001_initial'),
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoCustos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição do Grupo')),
            ],
            options={
                'verbose_name': 'Grupo de Custos',
                'verbose_name_plural': 'Grupos de Custos',
            },
        ),
        migrations.CreateModel(
            name='ItemCustos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição do Item')),
                ('sequencia', models.IntegerField(verbose_name='Sequência Item')),
            ],
            options={
                'verbose_name': 'Item Custo',
                'verbose_name_plural': 'Itens Custos',
            },
        ),
        migrations.CreateModel(
            name='SubGrupoCustos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição do SubGrupo')),
                ('sequencia', models.IntegerField(verbose_name='Sequência Subgrupo')),
                ('grupo_custos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gruposcustos', to='custos.grupocustos', verbose_name='Grupo de Custos')),
            ],
            options={
                'verbose_name': 'SubGrupo de Custos',
                'verbose_name_plural': 'SubGrupos de Custos',
            },
        ),
        migrations.CreateModel(
            name='ProvisaoCustos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição da Provisão')),
                ('valor', models.DecimalField(decimal_places=2, help_text='Informar o percentual sem o símbolo %', max_digits=10, verbose_name='Valor da Provisão')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empresaprovisao', to='empresa.empresa', verbose_name='Empresa')),
            ],
            options={
                'verbose_name': 'Provisão',
                'verbose_name_plural': 'Provisões',
            },
        ),
        migrations.CreateModel(
            name='PrecoItemCustos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidade', models.CharField(max_length=150, verbose_name='Unidade')),
                ('custo_medio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Custo Médio')),
                ('ultima_compra', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Última Compra')),
                ('data_inicio_vigencia', models.DateField(verbose_name='Data de Início da Vigência')),
                ('data_fim_vigencia', models.DateField(verbose_name='Data Final da Vigência')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('empresas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empresas', to='empresa.empresa', verbose_name='Empresa')),
                ('item_custos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='custos.itemcustos', verbose_name='Itens Custos')),
            ],
            options={
                'verbose_name': 'Preço do Item',
                'verbose_name_plural': 'Preços dos Itens',
            },
        ),
        migrations.CreateModel(
            name='ItemProdutos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa', verbose_name='Empresas')),
                ('itens', models.ManyToManyField(to='custos.PrecoItemCustos', verbose_name='Itens Custos')),
                ('produtos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itensprodutos', to='produtos.produtos', verbose_name='Produtos')),
                ('provisoes', models.ManyToManyField(blank=True, null=True, to='custos.ProvisaoCustos', verbose_name='Provisões')),
                ('tributos', models.ManyToManyField(blank=True, null=True, to='tax.Aliquotas', verbose_name='Tributos e Encargos')),
            ],
            options={
                'verbose_name': 'Item Produto',
                'verbose_name_plural': 'Itens dos Produtos',
            },
        ),
        migrations.AddField(
            model_name='itemcustos',
            name='subgrupo_custos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subgruposcustos', to='custos.subgrupocustos', verbose_name='SubGrupos Custos'),
        ),
    ]
