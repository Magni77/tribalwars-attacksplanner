from datetime import datetime, timedelta

from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from tribal_wars.planner.attack import Attack
from tribal_wars.planner.serializers import PlannerSerializer
from tribal_wars.planner.units import UnitsVelocity
from tribal_wars.planner.village import Village


class PlannerView(APIView):
    serializer_class = PlannerSerializer

    def post(self, request):
        data = request.data

        results = []
        target = Village(*data['target'])
        for attacker in data['attackers']:
            attacker_village = Village(*attacker['cords'])
            slowest_unit = getattr(UnitsVelocity, attacker['slowest_unit'])
            results.append(
                Attack(
                    attacker_village,
                    target,
                    slowest_unit,
                    datetime.strptime(attacker['arrive_time'], '%Y-%m-%d %H:%M:%S.%f')
                )
            )
        print(results)

        output = []
        for result in results:
            print(result.attack_at, result.duration)
            output.append(
                {
                    'cords': [result.attacker.x, result.attacker.y], 'start': result.attack_at,
                    'duration': result.duration.__str__(), 'arriveAt': result.arrive_time
                },
            )
        print(output)
        return Response({"results": output})
