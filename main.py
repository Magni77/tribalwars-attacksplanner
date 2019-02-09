from datetime import datetime

from attack import Attack
from units import UnitsVelocity
from village import Village

v_michal = Village(471, 451, 'michal ')

v_czarny = Village(476, 456, 'czarny')
v_kinia = Village(465, 451, 'kinia')
v_bogu = Village(467, 447, 'djbogu')
v_kacper = Village(477, 461, 'kacper')

v_attack = Village(469, 456, 'cycba')


attacks = [
    {'attacker': v_michal, 'unit': UnitsVelocity.ram, 'arrive_time': datetime(2019, 2, 11, 7, 0, 1)},
    {'attacker': v_bogu, 'unit': UnitsVelocity.gentry, 'arrive_time': datetime(2019, 2, 11, 7, 0, 1, 500000)},
    {'attacker': v_kacper, 'unit': UnitsVelocity.gentry, 'arrive_time': datetime(2019, 2, 11, 7, 0, 1, 600000)},
    {'attacker': v_czarny, 'unit': UnitsVelocity.gentry, 'arrive_time': datetime(2019, 2, 11, 7, 0, 1, 700000)},
    {'attacker': v_michal, 'unit': UnitsVelocity.gentry, 'arrive_time': datetime(2019, 2, 11, 7, 0, 2)}
]


for attack_data in attacks:
    attack = Attack(attack_data['attacker'], v_attack, attack_data['unit'], attack_data['arrive_time'])
    print(f"{attack.attacker} start at: {attack.attack_at} duration {attack.duration}, arrive at {attack.arrive_time}")


