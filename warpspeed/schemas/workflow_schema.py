from marshmallow import post_load
from warpspeed.schemas.structure_schema import StructureSchema


class WorkflowSchema(StructureSchema):
    @post_load
    def make_obj(self, data, **kwargs):
        from warpspeed.structures import Workflow

        workflow = Workflow(**data)

        for step in workflow.steps:
            step.structure = workflow

        return workflow
