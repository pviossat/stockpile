from plugins.stockpile.app.requirements.base_requirement import BaseRequirement


class Requirement(BaseRequirement):

    async def enforce(self, link, operation):
        """
        Check if any other agent in operation is using the same ability with given trait
        :param link
        :param operation
        :return: True if it hasn't elevated privileges, false otherwise
        """
        instances_link = [l for l in operation.chain if l.ability.ability_id == link.ability.ability_id and l.paw != link.paw and not l.finish]
        for i in instances_link:
            for uf in i.used:
                if self.enforcements['trait'] == uf.trait:
                    return False
        return True
