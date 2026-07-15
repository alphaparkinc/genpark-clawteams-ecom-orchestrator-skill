class ClawTeamsEcomOrchestratorClient:
    def delegate_goal(self, goal_description: str, sub_agents: list[str]) -> dict:
        plan = {agent: f"Assigned task related to {goal_description}" for agent in sub_agents}
        return {"delegated_plan": plan}