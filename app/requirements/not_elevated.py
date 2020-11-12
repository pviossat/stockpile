from plugins.stockpile.app.requirements.base_requirement import BaseRequirement


class Requirement(BaseRequirement):

    async def enforce(self, link, operation):
        """
        Check if current agent has not elevated privileges
        :param link
        :param operation
        :return: True if it hasn't elevated privileges, false otherwise
        """
        for agent in operation.agents:
            if agent.paw == link.paw and agent.Privileges[agent.privilege].value >= agent.Privileges['Elevated'].value:
                return False
        return True
