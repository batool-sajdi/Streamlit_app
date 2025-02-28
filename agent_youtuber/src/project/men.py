from crewai.flow.flow import Flow, start, listen
from dotenv import load_dotenv, find_dotenv
_:bool = load_dotenv(find_dotenv())
from litellm import completion
from project.crews.teaching_crew.teaching_crew import TeachingCrew

class PanaFlow(Flow):
   
    @start()
    def generate_topic(self):
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[{
                "role": "user",
                "content": "Generate a topic most trending for a creative motivation video"
            }]
        )
        self.state['topic'] = response['choices'][0]['message']['content']
        print(f"STEP 1: Generated topic: {self.state['topic']}")
        
    @listen("generate_topic")
    def generate_content(self):
        print("STEP 2: Generating content")
        teaching_crew = TeachingCrew()
        result = teaching_crew.kickoff(
            input={
                "topic": self.state['topic']
            }
        )
        print(f"Generated content: {result}")

def kickoff():
    flow = PanaFlow()
    flow.kickoff()

if __name__ == "__main__":
    kickoff()
