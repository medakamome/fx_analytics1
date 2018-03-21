from django.db import models

# Create your models here.
class Main(models.Model):
    """メイン"""
    # 通貨ペア
    symbol = models.CharField('シンボル', max_length=6)
    period = models.IntegerField('時間軸')
    high = models.DecimalField('高値', max_digits=6, decimal_places=5)
    low = models.DecimalField('安値', max_digits=6, decimal_places=5)
    open = models.DecimalField('始値', max_digits=6, decimal_places=5)
    close = models.DecimalField('終値', max_digits=6, decimal_places=5)
    time = models.DateTimeField('日時')

    def __str__(self):
        return self.symbol + self.period + self.time
