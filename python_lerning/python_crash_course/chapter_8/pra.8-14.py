#pra.8-14
def make_car(maker,type,**car_info):
    car_info['car_maker'] = maker
    car_info['car_type'] = type

    return car_info

car = make_car('subaru','outback',color = 'blue',tow_package = True)
print(car)
