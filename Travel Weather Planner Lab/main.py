distance_mi = 6
is_raining = True
has_bike = False
has_car = False
has_ride_share_app = True
if not distance_mi:
    print(False)
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi > 1 and distance_mi <= 6:
    if has_bike == True and not is_raining:
        print(True)
    else:
        print(False) # False
elif distance_mi > 6:
    if has_car == True or has_ride_share_app == True:
        print(True)
    else:
        print(False)
