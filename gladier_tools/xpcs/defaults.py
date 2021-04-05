from gladier import GladierBaseTool
from .corr import eigen_corr, apply_qmap


class EigenCorr(GladierBaseTool):

    flow_definition = {
        "Eigen Corr": {
        "Comment": "Eigen Corr",
        "Type": "Action",
        "ActionUrl": "https://api.funcx.org/automate",
        "ActionScope": "https://auth.globus.org/scopes/facd7ccc-c5f4-42aa-916b-a0e270e2c2a9/all",
        "Parameters": {
            "tasks": [{
                "endpoint.$": "$.input.funcx_ep",
                "func.$": "$.input.corr_fxid",
                "payload": {
                "proc_dir.$": "$.input.proc_dir",
                "hdf_file.$": "$.input.output",
                "imm_file.$": "$.input.imm",
                "flags.$": "$.input.flags"
                }
            }]
        },
        "ResultPath": "$.result",
        "WaitTime": 600,
        "End": True
        }
    }

    required_input = [
    'proc_dir',
    'output',
    'imm',
    'flags'
    ]

    flow_input = {
        'proc_dir': '',
        'output': '',
        'imm': '',
        'flags': ''
    }

    funcx_functions = [
        eigen_corr
    ]

class ApplyQmap(GladierBaseTool):
    
    flow_definition = {
        "Comment": "Apply QMap flow",
        "StartAt": "Apply QMap",
        "States": {
            "Apply QMap": {
            "Comment": "Eigen Corr",
            "Type": "Action",
            "ActionUrl": "https://api.funcx.org/automate",
            "ActionScope": "https://auth.globus.org/scopes/facd7ccc-c5f4-42aa-916b-a0e270e2c2a9/all",
            "Parameters": {
                "tasks": [{
                    "endpoint.$": "$.input.funcx_ep",
                    "func.$": "$.input.qmap_fxid",
                    "payload": {
                    "proc_dir.$": "$.input.proc_dir",
                    "input_file.$": "$.input.hdf",
                    "qmap_file.$": "$.input.qmap",
                    "flat_file.$": "$.input.flatfield",
                    "output_file.$": "$.input.output",
                    }
                }]
            },
            "ResultPath": "$.result",
            "WaitTime": 600,
            "End": True
            }
        }
    }

    required_input = [
        'proc_dir',
        'input_file',
        'qmap_file',
        'flat_file',
        'output_file'
    ]

    flow_input = {
        'proc_dir': '',
        'input_file': '',
        'qmap_file': '',
        'flat_file': '',
        'output_file': ''
    }

    funcx_functions = [
        apply_qmap
    ]

