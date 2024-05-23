import reflex as rx
from ..States.EditedCode import EditedCode
from ..States.GetProblem import GetProblem


class Results(rx.State):

    display_result:str = "Once submitted, you'll see your result here"
    results:bool = False

    async def get_results(self):

        self.display_result = "Loading..."

        editecode = await self.get_state(EditedCode)
        getproblem = await self.get_state(GetProblem)
        if editecode.output.strip().replace(" ", "") == getproblem.each_output.strip().replace(" ", ""): ##remove the spaces so you can compare the outputs regardless of what the user type hen creatng the problem
            self.results = True
            self.display_result = "Congratulations, your code its correct!"
        else:
            self.display_result = "Your code failed, but dont worry you can try again!"