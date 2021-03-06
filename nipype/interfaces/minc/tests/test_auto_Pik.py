# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..minc import Pik


def test_Pik_inputs():
    input_map = dict(annotated_bar=dict(argstr='--anot_bar',
    ),
    args=dict(argstr='%s',
    ),
    auto_range=dict(argstr='--auto_range',
    xor=(u'image_range', u'auto_range'),
    ),
    clobber=dict(argstr='-clobber',
    usedefault=True,
    ),
    depth=dict(argstr='--depth %s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    horizontal_triplanar_view=dict(argstr='--horizontal',
    xor=(u'vertical_triplanar_view', u'horizontal_triplanar_view'),
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    image_range=dict(argstr='--image_range %s %s',
    xor=(u'image_range', u'auto_range'),
    ),
    input_file=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    jpg=dict(xor=(u'jpg', u'png'),
    ),
    lookup=dict(argstr='--lookup %s',
    ),
    minc_range=dict(argstr='--range %s %s',
    ),
    output_file=dict(argstr='%s',
    genfile=True,
    hash_files=False,
    keep_extension=False,
    name_source=[u'input_file'],
    name_template='%s.png',
    position=-1,
    ),
    png=dict(xor=(u'jpg', u'png'),
    ),
    sagittal_offset=dict(argstr='--sagittal_offset %s',
    ),
    sagittal_offset_perc=dict(argstr='--sagittal_offset_perc %d',
    ),
    scale=dict(argstr='--scale %s',
    ),
    slice_x=dict(argstr='-x',
    xor=(u'slice_z', u'slice_y', u'slice_x'),
    ),
    slice_y=dict(argstr='-y',
    xor=(u'slice_z', u'slice_y', u'slice_x'),
    ),
    slice_z=dict(argstr='-z',
    xor=(u'slice_z', u'slice_y', u'slice_x'),
    ),
    start=dict(argstr='--slice %s',
    ),
    terminal_output=dict(nohash=True,
    ),
    tile_size=dict(argstr='--tilesize %s',
    ),
    title=dict(argstr='%s',
    ),
    title_size=dict(argstr='--title_size %s',
    requires=[u'title'],
    ),
    triplanar=dict(argstr='--triplanar',
    ),
    vertical_triplanar_view=dict(argstr='--vertical',
    xor=(u'vertical_triplanar_view', u'horizontal_triplanar_view'),
    ),
    width=dict(argstr='--width %s',
    ),
    )
    inputs = Pik.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Pik_outputs():
    output_map = dict(output_file=dict(),
    )
    outputs = Pik.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
