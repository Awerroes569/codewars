from preloaded import ELEMENTS

def fits(symbol, word):
    if not word:
        return False
    if len(symbol) > len(word):
        return False
    for index, character in enumerate(symbol):
        if word[index] != character:
            return False
    return True

def constructElement(symbol):
    symbol = symbol[0].upper()+symbol[1:]
    name = ELEMENTS[symbol]
    result = name+' ('+symbol+')'
    return result

def constructAnswer(elements):
    result = [constructElement(element) for element in elements]
    return result

def constructAnswers(solutions):
    result = [constructAnswer(solution) for solution in solutions]
    return result

def elemental_forms(word):
    if not word:
        return []
    elements = {x.lower() for x in ELEMENTS.keys()}
    word = word.lower()
    solutions = []
    furnace = []

    furnace.append((elements, word, []))

    def cutting(elements, left, processed):
        if not left:
            solutions.append(processed)
            return
        for element in elements:
            if fits(element, left):
                newProcessed = processed[:]
                newProcessed += [element]
                newLeft = left[len(element):]
                furnace.append((elements, newLeft, newProcessed))

    while (furnace):
        first, second, third = furnace.pop(0)
        cutting(first, second, third)

    processedSolutions = constructAnswers(solutions)

    return processedSolutions
