# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import InvWarp


def test_InvWarp_inputs():
    input_map = dict(absolute=dict(argstr='--abs',
    xor=[u'relative'],
    ),
    args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inverse_warp=dict(argstr='--out=%s',
    hash_files=False,
    name_source=[u'warp'],
    name_template='%s_inverse',
    ),
    jacobian_max=dict(argstr='--jmax=%f',
    ),
    jacobian_min=dict(argstr='--jmin=%f',
    ),
    niter=dict(argstr='--niter=%d',
    ),
    noconstraint=dict(argstr='--noconstraint',
    ),
    output_type=dict(),
    reference=dict(argstr='--ref=%s',
    mandatory=True,
    ),
    regularise=dict(argstr='--regularise=%f',
    ),
    relative=dict(argstr='--rel',
    xor=[u'absolute'],
    ),
    terminal_output=dict(nohash=True,
    ),
    warp=dict(argstr='--warp=%s',
    mandatory=True,
    ),
    )
    inputs = InvWarp.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_InvWarp_outputs():
    output_map = dict(inverse_warp=dict(),
    )
    outputs = InvWarp.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
