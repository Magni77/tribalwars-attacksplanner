from rest_framework.serializers import Serializer, ListField, ChoiceField, DateTimeField, CharField


class AttackerSerializer(Serializer):
    cords = ListField()
    slowest_unit = ChoiceField(
        [
            'spear', 'sword', 'axe', 'spy',
            'light', 'heavy', 'ram', 'catapult', 'gentry'
        ]
    )
    arrive_time = DateTimeField()


class PlannerSerializer(Serializer):
    target = ListField()
    attackers = AttackerSerializer(many=True)


"""
{
    "target": [470, 452],
    "attackers": [
        {
          "cords": [471, 451],
          "slowest_unit": "ram",
          "arrive_time": "2019-02-09 23:15:27.00"
        }
    ]
}



"""
