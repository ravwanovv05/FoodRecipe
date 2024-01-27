from api.models.recipe_rate import RecipeRate


def recipe_rate(dish_id):
    rate_list = RecipeRate.objects.filter(dish_id=dish_id)
    sum_rate = 0

    for rate in rate_list:
        sum_rate += rate.rate
    res = sum_rate / rate_list.count()
    return res



