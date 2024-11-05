def decision_paraguas(esta_lloviendo, tienes_paraguas):
    if esta_lloviendo:
        if tienes_paraguas:
            return "Llévalo contigo."
        else:
            return "Quédate en casa."
    else:
        return "No lleves paraguas."

# Ejemplos de uso
print(decision_paraguas(True, True))    # Está lloviendo y tienes paraguas
print(decision_paraguas(True, False))   # Está lloviendo y no tienes paraguas
print(decision_paraguas(False, True))   # No está lloviendo, pero tienes paraguas
print(decision_paraguas(False, False))  # No está lloviendo y no tienes paraguas
