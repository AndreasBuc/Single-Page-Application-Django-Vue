from django.apps import AppConfig


class QuestionConfig(AppConfig):
    name = 'questions'

    def ready(self):
        import questions.signals
