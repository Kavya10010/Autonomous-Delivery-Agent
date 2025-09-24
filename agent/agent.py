class DeliveryAgent:
    def __init__(self, env, max_time=100, max_fuel=100):
        self.env = env
        self.max_time = max_time
        self.max_fuel = max_fuel
        self.start = env.start
        self.goal = env.goal

    def state(self):
        # State can be extended to include dynamic obstacle info if needed
        return self.start

    def is_goal(self, state):
        return state == self.goal
