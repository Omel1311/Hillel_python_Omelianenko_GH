planetarium = 19
circus = 10
stadium = 6

planet_and_circ = 5
planet_and_stad = 3
circ_and_stad = 1

sick = 3

planet_1 = planetarium - planet_and_circ - planet_and_stad
stadium_1 = stadium - planet_and_stad - circ_and_stad
circus_1 = circus - circ_and_stad - planet_and_circ
all_pupil = sick + circus_1 + planet_1 + stadium_1 + planet_and_circ + planet_and_stad + circ_and_stad

print(f'(спосіб 1) всього {all_pupil} учнів у класі')

print("*" * 70)

pl_and_c_2 = {planet_and_circ}
planet_and_stad_2 = {planet_and_stad}
circ_and_stad_2 = {circ_and_stad}

#  спосіб 2 (з використанням множин)

planet_2 = {planetarium - planet_and_circ - planet_and_stad}
stadium_2 = {stadium - planet_and_stad - circ_and_stad}
circus_2 = {circus - circ_and_stad - planet_and_circ}

all_pupil_1 = sick + sum(circus_2 | planet_2 | stadium_2 | pl_and_c_2 | planet_and_stad_2 | circ_and_stad_2)

print(f'(спосіб 2) всього {all_pupil_1} учнів у класі')

