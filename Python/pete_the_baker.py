def cakes(recipe, available):
    result = None
    for rk,rv in recipe.items():
        try:
            quantity=available[rk]//rv
            if not result:
               result=quantity
            else:
                result=min(result,quantity)    
        except Exception as e:
            return 0
    return result

