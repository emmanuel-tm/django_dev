from django.db import models

# Create your models here.
class Measurement(models.Model):
    '''
    Esta clase hereda de Django models.Model y crea una tabla
    cuyo nombre es 'sensor_data_measurements' y va a almacenar
    los valores flotantes y/o (positivos, negativos, o incluso 0)
    provenientes de un sensor.
    '''
    id = models.BigAutoField(db_column='ID', primary_key=True)
    value = models.FloatField(verbose_name='value', default=0.0000)
    date = models.CharField(verbose_name='date', max_length=40, default='dd-mm-yyyy hh:mm:ss')

    class Meta:
        db_table = 'sensor_data_measurements'

    def __str__(self):
        '''
        Se sobreescribe esta función para poder retornar
        cuando es llamado el objeto, por ejemplo para mostrar
        el id en el admin de Django. 
        '''
        return f'{self.id}'
