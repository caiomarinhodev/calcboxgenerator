from django.db import models


# Create your models here.

class TimeStamped(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)


class Draw(TimeStamped):
    altura = models.FloatField(blank=True, null=True, default=5.0)
    largura = models.FloatField(blank=True, null=True, default=15.0)

    def __str__(self):
        return 'Altura {} x Largura {}'.format(self.altura, self.largura)

    def __unicode__(self):
        return 'Altura {} x Largura {}'.format(self.altura, self.largura)


class Box(TimeStamped):
    draw = models.ForeignKey(Draw, blank=True, null=True, on_delete=models.CASCADE, related_name='draw')
    comprimento = models.FloatField(blank=True, null=True, default=15.0)
    espessura = models.FloatField(blank=True, null=True, default=0.2)
    laterais_maiores = models.ForeignKey(Draw, blank=True, null=True, on_delete=models.CASCADE,
                                         related_name='laterais_maiores')
    laterais_menores = models.ForeignKey(Draw, blank=True, null=True, on_delete=models.CASCADE,
                                         related_name='laterais_menores')
    fundo_caixa = models.ForeignKey(Draw, blank=True, null=True, on_delete=models.CASCADE,
                                    related_name='fundo_caixa')
    tampa_capa = models.ForeignKey(Draw, blank=True, null=True, on_delete=models.CASCADE,
                                   related_name='tampa_caixa')
    lombada = models.ForeignKey(Draw, blank=True, null=True, on_delete=models.CASCADE,
                                related_name='lombada')
    tampa_fundo = models.ForeignKey(Draw, blank=True, null=True, on_delete=models.CASCADE,
                                    related_name='tampa_fundo')
    cobertura_caixa = models.ForeignKey(Draw, blank=True, null=True, on_delete=models.CASCADE,
                                        related_name='cobertura_caixa')
    cobertura_tampa = models.ForeignKey(Draw, blank=True, null=True, on_delete=models.CASCADE,
                                        related_name='cobertura_tampa')
    cobertura_interna = models.ForeignKey(Draw, blank=True, null=True, on_delete=models.CASCADE,
                                          related_name='cobertura_interna')
    fix = models.ForeignKey(Draw, blank=True, null=True, on_delete=models.CASCADE,
                            related_name='fix')
    cobertura_fix = models.ForeignKey(Draw, blank=True, null=True, on_delete=models.CASCADE,
                                      related_name='cobertura_fix')

    def __str__(self):
        return 'Altura {} x Largura {} x Comprimento {}'.format(self.draw.altura, self.draw.largura, self.comprimento)

    def __unicode__(self):
        return 'Altura {} x Largura {} x Comprimento {}'.format(self.draw.altura, self.draw.largura, self.comprimento)

    def make_draw(self, altura, largura):
        draw = Draw()
        draw.altura = altura
        draw.largura = largura
        draw.save()
        return draw

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, first_create=False):
        if first_create:
            self.laterais_maiores = self.make_draw(self.draw.altura, self.draw.largura + (self.espessura * 2))
            self.laterais_menores = self.make_draw(self.draw.altura, self.draw.largura)
            self.fundo_caixa = self.make_draw(self.comprimento, self.draw.largura)
            self.tampa_capa = self.make_draw(self.comprimento + 1, self.draw.largura + 1.5)
            self.lombada = self.make_draw(self.draw.altura, self.draw.largura + 1.5)
            self.tampa_fundo = self.make_draw(self.comprimento + 1, self.draw.largura + 1.5)
            self.cobertura_caixa = self.make_draw(self.draw.altura + 2, (self.draw.largura * 3) + 5)
            self.cobertura_tampa = self.make_draw(
                self.tampa_capa.altura + self.tampa_fundo.altura + self.lombada.altura + 8,
                self.tampa_capa.largura + 4)
            self.cobertura_interna = self.make_draw(self.cobertura_tampa.altura / 2, self.tampa_capa.largura)
            self.fix = self.make_draw(self.comprimento - 4, self.draw.largura - 4)
            self.cobertura_fix = self.make_draw(self.fix.altura + 2, self.fix.largura + 2)
        return super(Box, self).save(force_insert=force_insert, force_update=force_update, using=using,
                                     update_fields=update_fields)
