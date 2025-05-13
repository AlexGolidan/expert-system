from experta import *

class Crop(Fact):
    pass

class Symptom(Fact):
    pass

class Diagnosis(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.result = None
        self.probabilities = {}
        self.questions = []
        self.yes_answers = set()

    # Правила для подсолнечника
    @Rule(Crop(crop='подсолнечник'),
          OR(Symptom(symptom='желтые пятна')))
    def detect_aphid_sunflower(self):
        self.result = "Вредитель: тля\nРекомендация: опрыскивание имидаклопридом в период вегетации."

    @Rule(Crop(crop='подсолнечник'),
          OR(Symptom(symptom='скручивание листьев')))
    def detect_aphid_leaf_curl(self):
        self.result = "Вредитель: тля\nРекомендация: опрыскивание имидаклопридом в период вегетации."

    @Rule(Crop(crop='подсолнечник'),
          OR(Symptom(symptom='поврежденные семена')))
    def detect_sunflower_moth(self):
        self.result = "Вредитель: подсолнечниковая огневка\nРекомендация: опрыскивание дельтаметрином в начале цветения."

    @Rule(Crop(crop='подсолнечник'),
          OR(Symptom(symptom='личинки в корзинках')))
    def detect_sunflower_moth_larvae(self):
        self.result = "Вредитель: подсолнечниковая огневка\nРекомендация: опрыскивание дельтаметрином в начале цветения."

    @Rule(Crop(crop='подсолнечник'),
          OR(Symptom(symptom='темные пятна на листьях')))
    def detect_alternaria_sunflower(self):
        self.result = "Болезнь: альтернариоз\nРекомендация: опрыскивание азоксистробином."

    @Rule(Crop(crop='подсолнечник'),
          OR(Symptom(symptom='желтый ореол')))
    def detect_alternaria_halo(self):
        self.result = "Болезнь: альтернариоз\nРекомендация: опрыскивание азоксистробином."

    @Rule(Crop(crop='подсолнечник'),
          OR(Symptom(symptom='мягкие гниющие пятна')))
    def detect_sclerotinia_sunflower(self):
        self.result = "Болезнь: склеротиниоз\nРекомендация: обработка тебуконазолом и удаление пораженных частей."

    @Rule(Crop(crop='подсолнечник'),
          OR(Symptom(symptom='белый налет')))
    def detect_sclerotinia_white(self):
        self.result = "Болезнь: склеротиниоз\nРекомендация: обработка тебуконазолом и удаление пораженных частей."

    # Правила для рапса
    @Rule(Crop(crop='рапс'),
          OR(Symptom(symptom='отверстия в листьях')))
    def detect_cabbage_moth_raps(self):
        self.result = "Вредитель: капустная совка\nРекомендация: опрыскивание Bacillus thuringiensis."

    @Rule(Crop(crop='рапс'),
          OR(Symptom(symptom='гусеницы')))
    def detect_cabbage_moth_larvae(self):
        self.result = "Вредитель: капустная совка\nРекомендация: опрыскивание Bacillus thuringiensis."

    @Rule(Crop(crop='рапс'),
          OR(Symptom(symptom='поврежденные бутоны')))
    def detect_rape_blossom_beetle_buds(self):
        self.result = "Вредитель: рапсовый цветоед\nРекомендация: опрыскивание тиаклопридом до начала цветения."

    @Rule(Crop(crop='рапс'),
          OR(Symptom(symptom='наличие жуков')))
    def detect_rape_blossom_beetle_beetles(self):
        self.result = "Вредитель: рапсовый цветоед\nРекомендация: опрыскивание тиаклопридом до начала цветения."

    @Rule(Crop(crop='рапс'),
          OR(Symptom(symptom='белый налет на стеблях')))
    def detect_white_mold_raps(self):
        self.result = "Болезнь: белая гниль\nРекомендация: обработка боскалидом и удаление пораженных растений."

    @Rule(Crop(crop='рапс'),
          OR(Symptom(symptom='увядание растений')))
    def detect_white_mold_wilt(self):
        self.result = "Болезнь: белая гниль\nРекомендация: обработка боскалидом и удаление пораженных растений."

    @Rule(Crop(crop='рапс'),
          OR(Symptom(symptom='объеденные листья')))
    def detect_rape_sawfly_leaves(self):
        self.result = "Вредитель: рапсовый пилильщик\nРекомендация: опрыскивание лямбда-цигалотрином в период активности личинок."

    @Rule(Crop(crop='рапс'),
          OR(Symptom(symptom='личинки с черной головой')))
    def detect_rape_sawfly_larvae(self):
        self.result = "Вредитель: рапсовый пилильщик\nРекомендация: опрыскивание лямбда-цигалотрином в период активности личинок."

    # Правила для сои
    @Rule(Crop(crop='соя'),
          OR(Symptom(symptom='поврежденные стебли')))
    def detect_stem_weevil_soy(self):
        self.result = "Вредитель: стеблевой долгоносик\nРекомендация: опрыскивание хлорпирифосом + севооборот."

    @Rule(Crop(crop='соя'),
          OR(Symptom(symptom='личинки внутри')))
    def detect_stem_weevil_larvae(self):
        self.result = "Вредитель: стеблевой долгоносик\nРекомендация: опрыскивание хлорпирифосом + севооборот."

    @Rule(Crop(crop='соя'),
          OR(Symptom(symptom='бурые пятна на листьях')))
    def detect_phytophthora_soy(self):
        self.result = "Болезнь: фитофтороз\nРекомендация: обработка металаксилом и севооборот."

    @Rule(Crop(crop='соя'),
          OR(Symptom(symptom='увядание растений')))
    def detect_phytophthora_wilt(self):
        self.result = "Болезнь: фитофтороз\nРекомендация: обработка металаксилом и севооборот."

    @Rule(Crop(crop='соя'),
          OR(Symptom(symptom='мелкие желтые пятна')))
    def detect_spider_mite_soy(self):
        self.result = "Вредитель: паутинный клещ\nРекомендация: опрыскивание абамектином."

    @Rule(Crop(crop='соя'),
          OR(Symptom(symptom='паутина')))
    def detect_spider_mite_web(self):
        self.result = "Вредитель: паутинный клещ\nРекомендация: опрыскивание абамектином."

    @Rule(Crop(crop='соя'),
          OR(Symptom(symptom='серо-белые пятна')))
    def detect_ascochyta_soy(self):
        self.result = "Болезнь: аскохитоз\nРекомендация: обработка хлороталонилом и соблюдение севооборота."

    @Rule(Crop(crop='соя'),
          OR(Symptom(symptom='черные точки')))
    def detect_ascochyta_spots(self):
        self.result = "Болезнь: аскохитоз\nРекомендация: обработка хлороталонилом и соблюдение севооборота."

    def generate_questions(self, crop):
        disease_map = {
            'подсолнечник': {
                'тля': ['желтые пятна', 'скручивание листьев'],
                'подсолнечниковая огневка': ['поврежденные семена', 'личинки в корзинках'],
                'альтернариоз': ['темные пятна на листьях', 'желтый ореол'],
                'склеротиниоз': ['мягкие гниющие пятна', 'белый налет']
            },
            'рапс': {
                'капустная совка': ['отверстия в листьях', 'гусеницы'],
                'рапсовый цветоед': ['поврежденные бутоны', 'наличие жуков'],
                'белая гниль': ['белый налет на стеблях', 'увядание растений'],
                'рапсовый пилильщик': ['объеденные листья', 'личинки с черной головой']
            },
            'соя': {
                'стеблевой долгоносик': ['поврежденные стебли', 'личинки внутри'],
                'фитофтороз': ['бурые пятна на листьях', 'увядание растений'],
                'паутинный клещ': ['мелкие желтые пятна', 'паутина'],
                'аскохитоз': ['серо-белые пятна', 'черные точки']
            }
        }
        self.questions = []
        diseases = disease_map.get(crop, {})
        for disease, symptoms in diseases.items():
            for symptom in symptoms:
                question = f"У {crop} имеются {symptom}? "
                self.questions.append((question, symptom))
        return self.questions

    def calculate_probabilities(self, crop, yes_answers):
        disease_map = {
            'подсолнечник': {
                'тля': ['желтые пятна', 'скручивание листьев'],
                'подсолнечниковая огневка': ['поврежденные семена', 'личинки в корзинках'],
                'альтернариоз': ['темные пятна на листьях', 'желтый ореол'],
                'склеротиниоз': ['мягкие гниющие пятна', 'белый налет']
            },
            'рапс': {
                'капустная совка': ['отверстия в листьях', 'гусеницы'],
                'рапсовый цветоед': ['поврежденные бутоны', 'наличие жуков'],
                'белая гниль': ['белый налет на стеблях', 'увядание растений'],
                'рапсовый пилильщик': ['объеденные листья', 'личинки с черной головой']
            },
            'соя': {
                'стеблевой долгоносик': ['поврежденные стебли', 'личинки внутри'],
                'фитофтороз': ['бурые пятна на листьях', 'увядание растений'],
                'паутинный клещ': ['мелкие желтые пятна', 'паутина'],
                'аскохитоз': ['серо-белые пятна', 'черные точки']
            }
        }

        diseases = disease_map.get(crop, {})
        self.probabilities = {disease: 0 for disease in diseases.keys()}

        total_matches = 0
        for disease, associated_symptoms in diseases.items():
            matches = sum(1 for symptom in associated_symptoms if symptom in yes_answers)
            total_matches += matches
            self.probabilities[disease] = matches

        # Нормализация вероятностей
        if total_matches > 0:
            # Сначала распределяем вероятности пропорционально совпадениям
            for disease in self.probabilities:
                self.probabilities[disease] = (self.probabilities[disease] / total_matches) * 100

            # Проверяем, есть ли 100% вероятность
            max_prob = max(self.probabilities.values())
            if max_prob == 100:
                # Уменьшаем до 99%, остальные остаются 0%
                for disease in self.probabilities:
                    if self.probabilities[disease] == 100:
                        self.probabilities[disease] = 99

            # Округляем вероятности
            for disease in self.probabilities:
                self.probabilities[disease] = round(self.probabilities[disease], 2)

        else:
            # Если совпадений нет, равномерное распределение
            num_diseases = len(self.probabilities)
            if num_diseases > 0:
                base_probability = round(100 / num_diseases, 2)
                for disease in self.probabilities:
                    self.probabilities[disease] = base_probability

        return self.probabilities