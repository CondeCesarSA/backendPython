from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Physical(models.Model):
    package = models.CharField(max_length=255)
    mount = models.CharField(max_length=255)
    number_of_pins = models.IntegerField()

    def __str__(self):
        return f"{self.package} - {self.mount} - {self.number_of_pins} pins"

class Dimensions(models.Model):
    depth = models.FloatField()
    height = models.FloatField()
    length = models.FloatField()
    width = models.FloatField()

    def __str__(self):
        return f"{self.length} x {self.width} x {self.height} mm (Depth x Width x Height)"

class MeasureBase(models.Model):
    unit = models.CharField(max_length=255)
    value = models.FloatField()

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.value} {self.unit}"

class UnitResistance(MeasureBase):
    UNIT_CHOICES = [
        ('Ohmios', 'Ω'),
        ('Kiloohmios', 'kΩ'),
        ('Megaohmios', 'MΩ'),
        ('Gigaohmios', 'GΩ'),
        ('Teraohmios', 'TΩ'),
        ('Miliohmios', 'mΩ'),
        ('Microohmios', 'µΩ'),
        ('Nanoohmios', 'nΩ'),
        ('Picoohmios', 'pΩ'),
    ]
    unit = models.CharField(max_length=12, choices=[(label, abbrev) for label, abbrev in UNIT_CHOICES])

class UnitVolt(MeasureBase):
    voltage = models.FloatField()
    unit_choices = [
        ('milivoltios', 'mV'),
        ('voltios', 'V'),
        ('kilovoltios', 'kV'),
        ('megavoltios', 'MV'),
    ]
    unit = models.CharField(max_length=12, choices=[(label, abbrev) for label, abbrev in unit_choices])

class UnitCapacitance(MeasureBase):
    UNIT_CHOICES = [
        ('Picofaradio', 'pF'),
        ('Nano faradio', 'nF'),
        ('Microfaradio', 'µF'),
        ('Mili faradio', 'mF'),
        ('Kilo faradio', 'kF'),
    ]

    unit = models.CharField(max_length=12, choices=[(label, abbrev) for label, abbrev in UNIT_CHOICES])

class Technical(models.Model):
    pines = models.IntegerField(default=1)
    resistance = models.ForeignKey(UnitResistance, on_delete=models.CASCADE, null=True, blank=True)
    capacitance = models.ForeignKey(UnitCapacitance, on_delete=models.CASCADE, null=True, blank=True)
    voltage = models.ForeignKey(UnitVolt, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Technical: Pines={self.pines}, Resistance={self.resistance}, Capacitance={self.capacitance}, Voltage={self.voltage}"

class Distributor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Component(models.Model):
    name = models.CharField(max_length=255)
    stock = models.IntegerField()
    moq = models.IntegerField()
    technical = models.OneToOneField(Technical, on_delete=models.CASCADE, related_name="technical")
    dimensions = models.OneToOneField(Dimensions, on_delete=models.CASCADE, related_name='dimensions')
    physical = models.OneToOneField(Physical, on_delete=models.CASCADE, related_name='physical')
    manufacturer = models.OneToOneField(Manufacturer, on_delete=models.CASCADE, related_name='manufacturer')
    distributor = models.OneToOneField(Distributor, on_delete=models.CASCADE, related_name='distributor')

    def __str__(self):
        return f"Component: {self.name}, Stock={self.stock}, MOQ={self.moq}, Technical={self.technical}, Dimensions={self.dimensions}, Physical={self.physical}, Manufacturer={self.manufacturer}, Distributor={self.distributor}"
