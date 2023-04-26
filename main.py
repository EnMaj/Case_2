import local_ru as ru

nalog=True
resident=True
NDFL=0

temp_question=int(input(ru.QUESTION_1_1))
if temp_question>=183:
    print(ru.RESIDENT_TRUE)
else:
    temp_question = input(ru.QUESTION_1_2)
    if temp_question.upper()=="ДА":
        print(ru.RESIDENT_FALSE)
        resident=False
    else:
        print(ru.NALOG_FALSE)
        nalog=False

if nalog==True:
    temp_question=input(ru.QUESTION_2)
    if temp_question.upper()=="НЕТ":
        print(ru.NALOG_FALSE)
        nalog=False
    else:
        temp_question=input(ru.QUESTION_2_1)
        if temp_question.upper()=="ДА":
            NDFL=35
        else:
            temp_question=input(ru.QUESTION_2_2)
            if temp_question.upper()=="ДА":
                NDFL=13
            else:
                temp_question=input(ru.QUESTION_2_3)
                if temp_question.upper()=='ДА':
                    NDFL=9
                else:
                    if resident==True:
                        temp_question=input(ru.QUESTION_2_4)


if nalog==True:
    print(ru.NALOG+str(NDFL)+"%")
    income=int(input(ru.INCOME))
    print(ru.NALOG_FALSE,(income/100)*NDFL)