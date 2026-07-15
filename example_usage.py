from client import ClawTeamsEcomOrchestratorClient
client = ClawTeamsEcomOrchestratorClient()
print(client.delegate_goal("increase shoe sales", ["pricing_agent", "support_agent"]))