# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..brains import BRAINSLmkTransform


def test_BRAINSLmkTransform_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputFixedLandmarks=dict(argstr='--inputFixedLandmarks %s',
    ),
    inputMovingLandmarks=dict(argstr='--inputMovingLandmarks %s',
    ),
    inputMovingVolume=dict(argstr='--inputMovingVolume %s',
    ),
    inputReferenceVolume=dict(argstr='--inputReferenceVolume %s',
    ),
    numberOfThreads=dict(argstr='--numberOfThreads %d',
    ),
    outputAffineTransform=dict(argstr='--outputAffineTransform %s',
    hash_files=False,
    ),
    outputResampledVolume=dict(argstr='--outputResampledVolume %s',
    hash_files=False,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = BRAINSLmkTransform.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_BRAINSLmkTransform_outputs():
    output_map = dict(outputAffineTransform=dict(),
    outputResampledVolume=dict(),
    )
    outputs = BRAINSLmkTransform.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
