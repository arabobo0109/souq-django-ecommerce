# Generated by Django 2.1.4 on 2018-12-20 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20181220_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Alternative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Product Alternative',
                'verbose_name_plural': 'Product Alternatives',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='category',
            name='CATParent',
            field=models.ForeignKey(blank=True, limit_choices_to={'CATParent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category'),
        ),
        migrations.AddField(
            model_name='product_alternative',
            name='PALNAlternatives',
            field=models.ManyToManyField(related_name='alternative_products', to='product.Product'),
        ),
        migrations.AddField(
            model_name='product_alternative',
            name='PALNProduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_prodcut', to='product.Product'),
        ),
    ]