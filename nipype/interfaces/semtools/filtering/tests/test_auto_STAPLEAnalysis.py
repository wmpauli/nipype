# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..featuredetection import STAPLEAnalysis


def test_STAPLEAnalysis_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputDimension=dict(argstr='--inputDimension %d',
    ),
    inputLabelVolume=dict(argstr='--inputLabelVolume %s...',
    ),
    outputVolume=dict(argstr='--outputVolume %s',
    hash_files=False,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = STAPLEAnalysis.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_STAPLEAnalysis_outputs():
    output_map = dict(outputVolume=dict(),
    )
    outputs = STAPLEAnalysis.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
