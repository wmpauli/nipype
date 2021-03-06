# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import PRELUDE


def test_PRELUDE_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    complex_phase_file=dict(argstr='--complex=%s',
    mandatory=True,
    xor=[u'magnitude_file', u'phase_file'],
    ),
    end=dict(argstr='--end=%d',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    label_file=dict(argstr='--labels=%s',
    hash_files=False,
    ),
    labelprocess2d=dict(argstr='--labelslices',
    ),
    magnitude_file=dict(argstr='--abs=%s',
    mandatory=True,
    xor=[u'complex_phase_file'],
    ),
    mask_file=dict(argstr='--mask=%s',
    ),
    num_partitions=dict(argstr='--numphasesplit=%d',
    ),
    output_type=dict(),
    phase_file=dict(argstr='--phase=%s',
    mandatory=True,
    xor=[u'complex_phase_file'],
    ),
    process2d=dict(argstr='--slices',
    xor=[u'labelprocess2d'],
    ),
    process3d=dict(argstr='--force3D',
    xor=[u'labelprocess2d', u'process2d'],
    ),
    rawphase_file=dict(argstr='--rawphase=%s',
    hash_files=False,
    ),
    removeramps=dict(argstr='--removeramps',
    ),
    savemask_file=dict(argstr='--savemask=%s',
    hash_files=False,
    ),
    start=dict(argstr='--start=%d',
    ),
    terminal_output=dict(nohash=True,
    ),
    threshold=dict(argstr='--thresh=%.10f',
    ),
    unwrapped_phase_file=dict(argstr='--unwrap=%s',
    genfile=True,
    hash_files=False,
    ),
    )
    inputs = PRELUDE.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_PRELUDE_outputs():
    output_map = dict(unwrapped_phase_file=dict(),
    )
    outputs = PRELUDE.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
