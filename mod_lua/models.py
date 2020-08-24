from django.db import models


class Context(models.Model):
    class Meta:
        verbose_name = "Контекст"
        verbose_name_plural = "Контексты"

    name = models.CharField(verbose_name="Контекст", max_length=50)

    def __str__(self):
        return self.name


class ContextAction(models.Model):
    class Meta:
        verbose_name = "Действие"
        verbose_name_plural = "Действия"
        unique_together = ['context', 'prio']

    context = models.ForeignKey(Context, on_delete=models.CASCADE, verbose_name="Контекст")
    prio = models.IntegerField(verbose_name="Приоритет")
    condition_field = models.CharField(verbose_name="Поле условия", max_length=255, default="Caller-Destination-Number")
    condition_value = models.CharField(verbose_name="Значение условия", max_length=255, null=True, blank=True)
    action = models.CharField(verbose_name="Действие", max_length=255)
    action_value = models.CharField(verbose_name="Данные", max_length=255, null=True, blank=True)

    def __str__(self):
        return "{}({}): {}".format(self.context.__str__(), self.prio, self.action)


class User(models.Model):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    number = models.IntegerField(verbose_name="Номер", unique=True)
    password = models.CharField(verbose_name="Пароль", max_length=50)

    def __str__(self):
        return "{}".format(self.number)


class UserVar(models.Model):
    class Meta:
        verbose_name = "Переменная пользователя"
        verbose_name_plural = "Переменные пользователя"

    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Переменная", max_length=255)
    value = models.CharField(verbose_name="Значение", max_length=255)

    def __str__(self):
        return "{} of {}".format(self.name, self.user.__str__())


class Group(models.Model):
    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    name = models.CharField(verbose_name="Группа", max_length=50)
    members = models.ManyToManyField(User, verbose_name="Пользователи")

    def __str__(self):
        return self.name


class IVR(models.Model):
    class Meta:
        verbose_name = "IVR"
        verbose_name_plural = "IVR's"

    name = models.CharField(verbose_name="IVR", max_length=50)
    greet_long = models.CharField(verbose_name="Приветствие", max_length=100, default="ivr/ivr-welcome_to_freeswitch.wav")
    greet_short  = models.CharField(verbose_name="Приветствие кор.", max_length=100, default="ivr/ivr-welcome_to_freeswitch.wav")
    invalid_sound  = models.CharField(verbose_name="Ошибка ввода", max_length=100, default="ivr/ivr-that_was_an_invalid_entry.wav")
    exit_sound  = models.CharField(verbose_name="Выход", max_length=100, default="voicemail/vm-goodbye.wav")
    timeout  = models.IntegerField(verbose_name="Timeout", default=10000)
    max_failures  = models.IntegerField(verbose_name="Количество попыток", default=3)

    def __str__(self):
        return self.name


class IVREntry(models.Model):

    ACTIONS = (
        ("menu-exit", "Выход"),
        ("menu-sub", "Sub-menu"),
        ("menu-exec-app", "Приложение"),
        ("menu-play-sound", "Звуковой файл"),
        ("menu-back", "Назад"),
        ("menu-top", "Top menu"),
    )
    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    ivr = models.ForeignKey(IVR, name="IVR", on_delete=models.CASCADE)
    action  = models.CharField(verbose_name="Действие", max_length=100, default="menu-exec-app", choices=ACTIONS)
    digit  = models.CharField(verbose_name="Цифры", max_length=100,)
    param  = models.CharField(verbose_name="Параметры", max_length=100, null=True, blank=True)