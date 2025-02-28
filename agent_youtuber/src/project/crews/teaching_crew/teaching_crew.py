from crewai import Agent, Task, Crew


class TeachingCrew:
    def __init__(self):
        self.agent_config = {
            "teacher": {
                "role": "teacher",
                "goal": "You are a YouTuber teaching a class about video and channel trending",
                "backstory": "You are a YouTuber teaching about video and channel trending"
            }
        }
        
        self.task_config = {
            "describe_topic": {
                "description": "We are mentoring to create the best YouTuber. Today we teach about {topic}",
                "expected_output": "The students will have mastered the topic {topic}"
            }
        }

    def create_teacher(self) -> Agent:
        return Agent(
            role=self.agent_config["teacher"]["role"],
            goal=self.agent_config["teacher"]["goal"],
            backstory=self.agent_config["teacher"]["backstory"],
            verbose=True
        )

    def create_task(self, topic: str) -> Task:
        return Task(
            description=self.task_config["describe_topic"]["description"].format(topic=topic),
            expected_output=self.task_config["describe_topic"]["expected_output"].format(topic=topic),
            agent=self.create_teacher()
        )

    def kickoff(self, input: dict) -> str:
        topic = input.get("topic", "")
        task = self.create_task(topic)
        crew = Crew(
            agents=[self.create_teacher()],
            tasks=[task],
            verbose=True
        )
        result = crew.kickoff()
        return result   