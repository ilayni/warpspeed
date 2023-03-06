from marshmallow import post_load
from galaxybrain.schemas.structure_schema import StructureSchema


class WorkflowSchema(StructureSchema):
    @post_load
    def make_structure(self, data, **kwargs):
        from galaxybrain.structures import Workflow

        workflow = Workflow(**data)

        for step in workflow.steps:
            step.structure = workflow

        return workflow
