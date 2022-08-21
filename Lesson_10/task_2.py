badge = 23
stamp = 35
badge_and_stamp = 16
all_pupil = 52
not_intrested_pupil = all_pupil - ((badge-badge_and_stamp) + (stamp-badge_and_stamp) + badge_and_stamp)
print('*'*70)
print(f'(спосіб 1) Вcього {not_intrested_pupil} шкорярів, які не захоплюються колекціюванням')

#  спосіб 2 (з використанням множин)

badge_1 = {badge - badge_and_stamp}
stamp_1 = {stamp - badge_and_stamp}
badge_and_stamp_1 = {badge_and_stamp}

print('*'*70)

not_intrested_pupil_1 = all_pupil - (sum(badge_1 | stamp_1 | badge_and_stamp_1))
print(f'(спосіб 2) Вcього {not_intrested_pupil_1} шкорярів, які не захоплюються колекціюванням')
